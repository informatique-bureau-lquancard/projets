# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

iBdx = ['Saint-Emilion','Saint-Estèphe','Haut-Médoc','Pomerol','Saint-Julien','Pessac-Léognan / Graves','Margaux','Saint-Georges-Saint-Emilion','Moulis','Montagne-Saint-Emilion','Bordeaux-Supérieur','Pauillac','Fronsac','Bordeaux (AOC)']


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CHACOM.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                appelation=row[2]
                couleur=row[8]
                if appelation in iBdx and couleur=='Blanc':
                    chateau=unidecode(row[0])
                    chateau=chateau.replace('Annees ','')
                    chateau=chateau.replace('Champagne ','')
                    chateau=re.split('[0-9][0-9][0-9][0-9]',chateau)
                    chateau=chateau[0]+'Blanc'
                else:
                    chateau=unidecode(row[0])
                    chateau=chateau.replace('Annees ','')
                    chateau=chateau.replace('Champagne ','')
                    chateau=re.split('[0-9][0-9][0-9][0-9]',chateau)
                    chateau=chateau[0]

                chateau=chateau.replace('"',"")
                chateau=chateau.replace(',','')
                chateau=chateau.strip()



                # année, on garde seulement la date
                annee = unidecode(row[1])
                annee=annee.replace('Annees ','')
                if annee == 'Non millesime':
                    annee='NV'
                else:
                    annee=annee.replace('Annees ','')

                # Format de la bouteille
                if row[3]=='37.5cl':
                    formatb='DE'
                elif row[3]=='50cl':
                    formatb='CL'
                elif row[3]=='70cl':
                    formatb='BO'
                elif row[3]=='75cl':
                    formatb='BO'
                elif row[3]=='150cl':
                    formatb='MG'
                elif row[3]=='300cl':
                    formatb='DM'
                elif row[3]=='500cl':
                    formatb='JE'
                elif row[3]=='450cl':
                    formatb='RE'
                elif row[3]=='600cl':
                    formatb='IM'
                elif row[3]=='900cl':
                    formatb='SA'
                elif row[3]=='1200':
                    formatb='BA'
                elif row[3]=='1500cl':
                    formatb='NA'
                elif row[3]=='1800cl':
                    formatb='ME'
                else :
                    formatb=row[3]
                # Prix
                prix=row[4]
                # quantite
                quantite=row[5]
                # selon le conditionnement, on change la quantite
                if row[6]=='1':
                    conditionnement='UNITE'
                elif row[6]=='CBO1':
                    conditionnement=row[6]
                elif row[6]=='CBO3':
                    conditionnement=row[6]
                    quantite=str(int(quantite)*3)
                elif row[6]=='CBO6':
                    conditionnement=row[6]
                    quantite=str(int(quantite)*6)
                elif row[6]=='CBO12':
                    conditionnement=row[6]
                    quantite=str(int(quantite)*12)
                elif row[6]=='CBO24':
                    conditionnement=row[6]
                    quantite=str(int(quantite)*24)
                elif row[6]=='6':
                    conditionnement='UNITE'
                    quantite='6'
                elif row[6]=='12':
                    conditionnement='UNITE'
                    quantite='12'
                else:
                    conditionnement=row[6]
                # Commentaire
                commentaire=unidecode(row[7])
                commentaire=commentaire.replace(","," - ")
                commentaire = commentaire.replace('  ',' ')
                # couleur
                couleur=row[8]
                # appelation
                appelation=row[2]
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
