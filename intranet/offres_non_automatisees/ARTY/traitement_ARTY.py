import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ARTY.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'
                if row[4]=='':
                    pass
                elif row[4]=='Wine':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[5]+' '+row[4]
                    if row[5]=='MARGAUX':
                        chateau=chateau.replace('MARGAUX','')
                    else:
                        chateau=chateau.replace('SAUTERNES','')
                        chateau=chateau.replace('POMEROL','')
                        chateau=chateau.replace('PESSAC LEOGNAN','')
                        chateau=chateau.replace('ST JULIEN','')

                    chateau = chateau.strip()
                    chateau = chateau.replace(',','')
                    chateau = chateau.replace('"','')

                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    annee=row[0]
                    # quantite
                    quantite=row[1]
                    # Format de la bouteille
                    if row[2]=='0,75 L':
                        formatb='BO'
                    elif row[2]=='1,5 L' or row[2]=='1,5L':
                        formatb='MG'
                    elif row[2]=='3 L':
                        formatb='DM'
                    elif row[2]=='6 L':
                        formatb='IM'
                    else:
                        formatb=row[2]
                    # Prix
                    fPrix=repr(row[7])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" EUR","")
                    prix=prix.replace(".",",")
                    #conditionnement & commentaire
                    if row[3]=='':
                        if formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaire='VERIF CDT'
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO6'
                                commentaire='VERIF CDT'
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO3'
                                commentaire='VERIF CDT'
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            commentaire='VERIF CDT'
                        else:
                            conditionnement='UNITE'
                            commentaire='VERIF CDT'
                    elif row[3]=='PERFECT':
                        if formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT + PERFECT'
                            else:
                                conditionnement='CBO12'
                                commentaire='VERIF CDT + PERFECT'
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT + PERFECT'
                            else:
                                conditionnement='CBO6'
                                commentaire='VERIF CDT + PERFECT'
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT + PERFECT'
                            else:
                                conditionnement='CBO3'
                                commentaire='VERIF CDT + PERFECT'
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            commentaire='VERIF CDT + PERFECT'
                        else:
                            conditionnement='UNITE'
                            commentaire='VERIF CDT + PERFECT'
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace('OWC/','CBO')
                        conditionnement=conditionnement.replace('OWC','CBO')
                        conditionnement=conditionnement.replace('LOOSE','UNITE')
                        conditionnement=conditionnement.replace('CASE','GIBO1')
                        conditionnement=conditionnement.replace('x','')
                        conditionnement=conditionnement.replace('/','')
                        conditionnement=conditionnement.replace('OC','CC')
                        conditionnement=conditionnement.replace('3 in ','')
                        commentaire=''


                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''

                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
