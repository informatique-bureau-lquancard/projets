# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_BOUOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                #On defini le nom du chateau
                if 'BORDEAUX BLANC' in row[0]:
                    chateau=unidecode(row[2])+' Blanc'
                elif 'PESSAC LEOGNAN' in row[0]:
                    if row[1]=='BLANC':
                        chateau=unidecode(row[2])+' Blanc'
                    else:
                        chateau=row[2]
                elif row[0]=='GRAVES BLANC':
                    chateau=unidecode(row[2])+' Blanc'
                else:
                    chateau=unidecode(row[2])

                if '-' in row[5]:
                    chateau = 'Verticale '+chateau
                    collection = 1
                elif '/' in row[5]:
                    chateau = 'Verticale '+chateau
                else:
                    collection = 0



                #Millésime
                if '-' in row[5] :
                    annee = row[5].split('-')
                    annee = annee[-1]
                    commentaire = unidecode(row[5])
                elif '/' in row[5] :
                    annee = row[5].split('/')
                    annee = annee[-1]
                    commentaire = unidecode(row[5])
                elif 'à' in row[5]:
                    annee = row[5].split('à')
                    annee = annee[-1]
                    commentaire = unidecode(row[5])
                else :
                    annee = row[5]
                    commentaire = ''

                annee = annee.strip()

                full_annee = len(annee)
                if int(full_annee) < 4 :
                    if annee[0] == '1' or annee[0] =='0' :
                        annee = '20'+annee
                    else :
                        annee = '19'+annee




                #Format de la bouteille
                if row[6]=='0,75':
                    formatb='BO'
                elif row[6]=='1,5':
                    formatb='MG'
                elif row[6]=='3':
                    formatb='DM'
                elif row[6]=='5':
                    formatb='JE'
                elif row[6]=='6':
                    formatb='IM'
                elif row[6]=='15':
                    formatb='NA'
                elif row[6]=='18':
                    formatb='ME'
                elif row[6]=='27':
                    formatb='BABY'
                elif row[6]=='0,375':
                    formatb='DE'
                else:
                    formatb=row[6]

                #Prix
                prix=unidecode(row[11])
                prix=prix.replace(' ','')
                prix=prix.replace('EUR','')
                prix = prix.strip()

                #quantité
                quantite=row[10]
                quantite=quantite.replace(' ','')
                quantite=quantite.replace('<','')
                quantite=quantite.replace('>','')

                #Conditionnement
                conditionnement=row[7]+row[8]
                conditionnement=conditionnement.replace('CB','CBO')


                #tarif officieux
                officieux='1'


                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
