import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8


import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

dico_horsbdx = ['Bourgogne rouge','Bourgogne blanc','Coteaux Bourguignon']

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_MILLE1.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[7]=='':
                    pass
                elif row[7]=='.':
                    pass
                else:
                    appellation = row[8]
                    #chateau=unidecode(row[3])
                    if appellation in dico_horsbdx :
                        # Nom du chateau
                        chateau=unidecode(row[7])+' '+unidecode(row[3])
                        #chateau=re.sub(r'[0-9]','',chateau)
                    else :
                        chateau=unidecode(row[3])

                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.upper()


                    # année
                    if row[0]=='NV' or row[0]=='' or row[0]==' ':
                        annee='NV'
                    else:
                        annee=row[0]

                    # conditionnement formatb et quantite
                    quantite=row[1]

                    quantite = ft.formaterQuantite(quantite)

                    if row[2]=='par 6 Bouteilles':
                        formatb='BO'
                        conditionnement='CBO6'
                        quantite=row[1]
                    elif row[2]=='par 6 bouteilles':
                        formatb='BO'
                        conditionnement='CBO6'
                        quantite=row[1]
                    elif row[2]=='par 6 Demi-bouteilles':
                        formatb='DE'
                        conditionnement='CBO6'
                        quantite=row[1]
                    elif row[2]=='par 12 Demi-bouteilles':
                        formatb='DE'
                        conditionnement='CBO12'
                        quantite=row[1]
                    elif row[2]=='par 6 Magnums':
                        formatb='BO'
                        conditionnement='CBO6'
                        quantite=row[1]
                    elif row[2]=='par 6 magnums':
                        formatb='BO'
                        conditionnement='CBO6'
                        quantite=row[1]
                    elif row[2]=='par 12 Bouteilles':
                        formatb='BO'
                        conditionnement='CBO12'
                        quantite=row[1]
                    elif row[2]=='par 12 bouteilles':
                        formatb='BO'
                        conditionnement='CBO12'
                        quantite=row[1]
                    # elif row[2]=='Bouteille':
                    #     formatb='BO'
                    #     conditionnement='UNITE'
                    #     commentaire='Verif cdt'
                    elif row[2]=='Magnum':
                        formatb='MG'
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    elif row[2]=='par 3 Magnums':
                        formatb='MG'
                        conditionnement='CBO3'
                    elif row[2]=='Dble magnum':
                        formatb='DM'
                        conditionnement='CBO3'
                        commentaire='Verif cdt'
                    elif row[2]=='Demi-bouteille':
                        formatb='DE'
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    elif row[2]=='par 3 Bouteilles':
                        formatb='BO'
                        conditionnement='CBO3'
                    elif row[2]=='ImpÈriale':
                        formatb='IM'
                        conditionnement='CBO1'
                        commentaire='Verif cdt'
                        quantite=str(int(quantite)*1)
                    elif row[2]=='Bouteille':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[2]=='MAGNUM':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[2]=='DMAG':
                        formatb='DM'
                        if int(quantite)<3:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO3'
                    elif row[2]=='DEMI':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[2]=='JEROBOAM':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[2]=='JÈroboam':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[2]=='IMPERIALE':
                        formatb='IM'
                        conditionnement='CBO1'
                    elif row[2]=='Mathusalem':
                        formatb='MAT'
                        conditionnement='CBO1'
                    elif row[2]=='SALMANAZAR':
                        formatb='SA'
                        conditionnement='CBO1'
                    else :
                        formatb=row[2]
                        conditionnement=''
                    # Prix
                    prix=row[5]
                    #prix=row[6].replace('.',',')
                    #prix=row[6].replace('€','')
                    #prix=row[6].replace(' ','')
                    # Commentaires
                    commentaires = unidecode(row[9])
                    #commentaires=unidecode(row[8])+' - '+unidecode(row[9])+' - '+unidecode(row[10])
                    commentaires = commentaires.replace(',','')
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()

























































































