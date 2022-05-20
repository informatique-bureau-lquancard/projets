## coding: utf-8
import csv
import glob
import re
import io
import time
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_OENOE.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 1
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:
                bEcrire=0
                if "Bordeaux Rouge" in row[0]:
                    index_chateau = 1
                elif "Bordeaux Blanc" in row[0]:
                    index_chateau = 2
                elif "Rhône Sud" in row[0]:
                    index_chateau = 3
                elif row[7]=="":# si vide, il ne faut rien faire finalement
                    #index_chateau=-1 # on note -1 pour indiquer qu'on ne traite pas la ligne
                    bEcrire=0
                elif row[0]=="Mill.": # pour identifier ta ligne d'entête que tu ne as pas traiter non plus
                    index_chateau=-1
                else:
                    # et là on traite les lignes
                    if index_chateau == 1:
                        # construction de ta ligne spécifique au cas 3
                        # et après tu peux énumérer tous tes cas particulier
                        chateau=unidecode(row[3])
                        chateau=chateau.replace('â','a')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ô','o')
                        bEcrire=1
                    elif index_chateau == 2:
                        chateau=unidecode(row[3])+' Blanc'
                        chateau=chateau.replace('â','a')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ô','o')
                        bEcrire=1
                    elif index_chateau == 3:
                        chateau=unidecode(row[3])+' '+unidecode(row[5])
                        chateau=chateau.replace('â','a')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ô','o')
                        bEcrire=1
                    else:
                        bEcrire=0

                    chateau = chateau.replace('"',"")
                    chateau = chateau.replace(',','')

                    # annee
                    if row[0]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[0]

                    # Format de bouteille
                    if row[1]=='75 cl' or row[1]=='75 cl ':
                        formatb='BO'
                    elif row[1]=='150 cl' or row[1]=='150 cl ':
                        formatb='MG'
                    elif row[1]=='300 cl ' or row[1]=='300 cl':
                        formatb='DM'
                    elif row[1]=='500 cl' or row[1]=='500 cl ':
                        formatb='JE'
                    elif row[1]=='600 cl' or row[1]=='600 cl ':
                        formatb='IM'
                    elif row[1]=='37,5 cl ' or row[1]=='37,5 cl':
                        formatb='DE'
                    elif row[1]=='50 cl' or row[1]=='37,5 cl':
                        formatb='CL'
                    elif row[1]=='70 cl ' or row[1]=='37,5 cl':
                        formatb='BO'
                    else:
                        formatb=row[1]

                    # Prix
                    fprix = repr(row[7])
                    prix=unidecode(fprix)
                    prix=prix.replace(' EUR','')
                    prix=prix.replace('.',',')
                    prix=prix.replace(' ','')
                    prix=prix.replace('\'','')

                    #quantite
                    quantite=unidecode(row[2])
                    quantite = quantite.replace(' ','')

                    #conditionnement
                    iCond=0
                    if 'CB NEUTRE' in row[6]:
                        Uconditionnement = re.findall('[\d]',row[6])
                        if not Uconditionnement :
                            conditionnement = 'CBN'
                        else:
                            conditionnement = 'CBN'+Uconditionnement[0]
                    elif row[6]=="":
                        iCond=1
                        if formatb=='BO':
                            if int(quantite)<=12:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO12'
                        elif formatb=='MG':
                            if int(quantite)<=6:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO6'
                    else:
                        iCond=0
                        conditionnement=row[6]
                        conditionnement=conditionnement.replace('CB ','CBO')
                        conditionnement=conditionnement.replace('CT ','CC')
                        conditionnement=conditionnement.replace('MAG','')

                    #Commentaire
                    if iCond == 0:
                        commentaire=row[8]
                    elif iCond == 1:
                        commentaire = 'VERIF CDT'




                # écriture de la ligne
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)


            monFichierEntre.close()
