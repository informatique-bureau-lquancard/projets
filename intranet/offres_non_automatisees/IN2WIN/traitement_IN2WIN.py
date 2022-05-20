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
        nom_sortie='sortie_IN2WIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois

            DicoCond = ['CC1','CC2','CC3','CC4','CC6','CC12','CC12DE','CC24','CC24DE','CBO1','CBO2','CBO3','CBO4','CBO6','CBO12','CBO12DE','CBO24DE','GIBO1','UNITE']

            for row in reader:
                bEcrire=0
                if "BURGUNDY " in row[0]:
                    index_chateau = 3
                elif "RHONE" in row[0]:
                    index_chateau = 4
                elif "ALSACE/" in row[0] :#/LOIRE/CHABLIS/MACON/BEAUJOLAIS/JURA/VDP/ SANCERRE " in row[0]:
                    index_chateau = 5
                elif "CHAMPAGNE" in row[0]:
                    index_chateau = 6
                elif "GERMANY/AUSTRIA" in row[0]:
                    index_chateau = 8
                elif "ITALY" in row[0]:
                    index_chateau = 8
                elif "SPAIN" in row[0]:
                    index_chateau = 8
                elif "TOKAY" in row[0]:
                    index_chateau = 8
                elif "PORTO/SHERRY" in row[0]:
                    index_chateau = 8
                elif "AUSTRALIA / US / CHILI/ BRESIL" in row[0]:
                    index_chateau = 8
                elif "EAU DE VIE / COGNAC / ARMAGNAC" in row[0]:
                    index_chateau = 8
                elif row[0]=="":# si vide, il ne faut rien faire finalement
                    index_chateau=-1 # on note -1 pour indiquer qu'on ne traite pas la ligne
                elif row[0]=="CHATEAU" or row[0]=="CHÂTEAU": # pour identifier ta ligne d'entête que tu ne as pas traiter non plus
                    index_chateau=-1
                else:
                    # et là on traite les lignes
                    if row[3] == "":
                        bEcrire = 0
                    elif index_chateau == 3:
                        # construction de ta ligne spécifique au cas 3
                        # et après tu peux énumérer tous tes cas particulier
                        chateau=unidecode(row[2])+' '+unidecode(row[0])
                        bEcrire=1
                    elif index_chateau == 4:
                        chateau=unidecode(row[0])+' '+unidecode(row[2])
                        bEcrire=1
                    elif index_chateau == 5:
                        chateau=unidecode(row[2])+' '+unidecode(row[0])
                        bEcrire=1
                    elif index_chateau == 6:
                        chateau=unidecode(row[2])+' '+unidecode(row[0])
                        bEcrire=1
                    elif index_chateau == 8:
                        chateau=unidecode(row[2])+' '+unidecode(row[0])
                        bEcrire=1
                    else:
                        # construction de ligne en mode normal
                        # On fabrique la nouvelle ligne dans l'ordre voulu
                        chateau=unidecode(row[0])
                        bEcrire=1

                    # annee
                    if row[1]=='NV':
                        annee='NV'
                    else:
                        annee=row[1]

                    # Format de bouteille
                    iFormatb = row[3].upper()
                    iFormatb = iFormatb.strip()
                    iFormatb = iFormatb.replace(' ','')

                    if iFormatb == '75':
                        formatb='BO'
                    elif iFormatb =='75CL':
                        formatb='BO'
                    elif '150CL' in iFormatb :
                        formatb='MG'
                    elif '148CL' in iFormatb:
                        formatb = 'MG'
                    elif '300CL' in iFormatb:
                        formatb='DM'
                    elif '500CL'in iFormatb:
                        formatb='JE'
                    elif '600CL' in iFormatb:
                        formatb='IM'
                    elif '37,5CL' in iFormatb :
                        formatb='DE'
                    elif '50CL' in iFormatb:
                        formatb='CL'
                    elif '70CL' in iFormatb:
                        formatb='BO'
                    elif '900CL' in iFormatb:
                        formatb='SA'
                    elif '100CL' in iFormatb:
                        formatb='L'
                    else:
                        formatb=iFormatb

                    # Prix
                    prix=unidecode(row[5])
                    prix = prix.replace(' ','')
                    prix = prix.replace('EUR','')

                    #quantite
                    quantite=row[4]

                    #conditionnement
                    if '/' in row[6] :
                        recCond = row[6].split('/')
                        recCond = recCond[0]
                        recCom = recCond[1]
                    if '-' in row[6] :
                        recCond = row[6].split('-')
                        recCond = recCond[0]
                        recCom = recCond[1]
                    else :
                        recCond = row[6]

                    recCond = recCond.replace('Carton of ','CC')
                    recCond = recCond.replace('Cartons of ','CC')
                    recCond = recCond.replace('Owc of ','CBO')
                    recCond = recCond.replace(' Half bottles','DE')
                    recCond = recCond.replace('CBO24','CBO24DE')
                    recCond = recCond.replace('Gift Boxes of ','GIBO')
                    recCond = recCond.replace('Unite','UNITE')

                    i = recCond.split(' ',1)

                    if i[0] in DicoCond :
                        conditionnement = i[0]
                        commentaire = recCond.replace(i[0],'')
                    else:
                        conditionnement = 'UNITE'
                        commentaire = 'VERIF CDT - '+recCond

                # écriture de la ligne
                if bEcrire==1 :
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.strip()
                    commentaire = commentaire.replace(',',' -')
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
