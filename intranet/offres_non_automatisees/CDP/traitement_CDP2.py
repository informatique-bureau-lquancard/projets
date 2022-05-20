import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CDP.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=' ', quotechar='')
            for row in reader:
                bEcrire=0
                officieux='1'
                if row[1]=="":
                    bEcrire=0
                elif "Euros" in row[7]:
                    bEcrire=0

                else:
                    bEcrire=1
                    # Nom du chateau
                    if row[0]=='Bordeaux Rouge':
                        chateau=unidecode(row[3])

                    elif row[0]=='Bordeaux Blanc':
                        chateau=unidecode(row[3])+' blanc'
                    else:
                        chateau=unidecode(row[1])+' '+unidecode(row[3])
                        
                    # année
                    if row[2]=='' or row[2]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[2]
                        annee=annee.replace('-','')
                    
                    # quantite
                    quantite=row[6]
                    # Format de la bouteille
                    if row[4]=='37.5 cl':
                        formatb='DE'
                    elif row[4]=='37,5 cl':
                        formatb='DE'
                    elif row[4]=='20 cl':
                        formatb='1/4'
                    elif row[4]=='25 cl':
                        formatb='1/4'
                    elif row[4]=='35 cl':
                        formatb='1/4'
                    elif row[4]=='35 cl':
                        formatb='1/4'
                    elif row[4]=='50 cl':
                        formatb='CL'
                    elif row[4]=='63 cl':
                        formatb='BT'
                    elif row[4]=='70 cl':
                        formatb='BT'
                    elif row[4]=='75 cl':
                        formatb='BO'
                    elif row[4]=='1000 cl':
                        formatb='L'
                    elif row[4]=='150 cl':
                        formatb='MG'
                    elif row[4]=='300 cl':
                        formatb='DM'
                    elif row[4]=='500 cl':
                        formatb='JE'
                    elif row[4]=='600 cl':
                        formatb='IM'
                    else :
                        formatb=row[4]
                    # Prix
                    fPrix=repr(row[7])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')



                    #quantité
                    quantite=row[6]
                    #conditionnement et commentaires
                    commentaires=""
                    if row[5]=='':
                        if formatb=='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO24DE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='1/4':
                            conditionnement='UNITE'
                            commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='CL':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='BT':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='L':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO6'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                            else:
                                conditionnement='CBO3'
                                commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='JE':
                            conditionnement='CBO1'
                            commentaires='VERIF CDT'+' - '+unidecode(row[5])
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            commentaires='VERIF CDT'+' - '+unidecode(row[5])
                    elif 'SANS/' in row[5]:
                        conditionnement='UNITE'
                        commentaires='VERIF CDT'+' - '+unidecode(row[5])
                    else:
                        conditionnement=row[5]
                        conditionnement=conditionnement.replace('CBO/','CBO')
                        conditionnement=conditionnement.replace('C/','CC')
                        conditionnement=conditionnement.replace('CO/','CC')
                        conditionnement=conditionnement.replace('CMO/','CC')
                        conditionnement=conditionnement.replace('CBMO/','CBO')
                        conditionnement=conditionnement.replace('CM/','CC')
                        conditionnement=conditionnement.replace('CMAT/','CC')
                        conditionnement=conditionnement.replace('CMO/','CC')
                        conditionnement=conditionnement.replace('CBDMO/','CBO')
                        conditionnement=conditionnement.replace('CBMO/','CBO')
                        conditionnement=conditionnement.replace('CBM/','CBO')
                        conditionnement=conditionnement.replace('CGBO/','CBO')
                        conditionnement=conditionnement.replace('CDM/','CBO')
                        conditionnement=conditionnement.replace('CBDM/','CBO')
                        conditionnement=conditionnement.replace('C50O/','CC')
                        conditionnement=conditionnement.replace('COFFRETBO/','GIBO')
                        conditionnement=conditionnement.replace('COFFRETMO/','GIBO')
                        commentaires='VERIF CDT'+' - '+unidecode(row[5])


                    
                    
 
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,officieux,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
