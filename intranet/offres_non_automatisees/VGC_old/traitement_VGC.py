import csv
import glob
import re
from unidecode import unidecode
import time
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_VGC.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:

                #quantite
                quantite=row[4]

                if len(quantite)==0 or not str(quantite).isnumeric():
                    continue

                # Chateau
                chateau = row[0]
                annee = row[1]

                #Formatb
                formatb=row[2]

                
                #if 'Bordeaux' in chateau:
                #    chateau=unidecode(str(formatb))
                #    chateau=chateau.replace(',','a') 
                #elif 'Bourgogne' in chateau:
                #    chateau=unidecode(str(annee+' '+formatb))
                #    chateau=chateau.replace(',','a') 
                #elif 'Champagne' in chateau:
                #    chateau=unidecode(str(annee+' '+formatb))
                #    chateau=chateau.replace(',','a') 
                #elif 'Rhone' in chateau:
                #    chateau=unidecode(str(annee+' '+formatb))
                #    chateau=chateau.replace(',','a') 
                #else:
                #    chateau=unidecode(str(formatb))
                #    chateau=chateau.replace(',','a') 


                # Annee

                if annee == "0" :
                    annee=time.strftime('%Y')

                #prix
                prix=row[3]



                #conditionnement
                conditionnement=row[5]

                # commentaire
                commentaire=unidecode(row[6])

                #on construit la nouvelle ligne
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                writer.writerow(newRow)
        monFichierEntre.close()
