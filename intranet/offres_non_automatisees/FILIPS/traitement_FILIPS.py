# coding: utf-8
import csv
import glob
import re
import io
import time
from unidecode import unidecode
import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_FILIPS.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

            iChateau = 0

            for row in reader:

                if row[0]=='Bordeaux Rouge':
                    iChateau=1
                    continue;
                elif row[0]=='Bordeaux Blanc':
                    iChateau=2
                    continue;
                elif row[0]=='Bourgogne Rouge':
                    iChateau=3
                    continue;

                chateauBis : str = str(row[2]).replace(" ", "")
                prix : str = str(row[5]).replace(" ", "")

                if(len(chateauBis) == 0 or chateauBis == "Vin" or len(prix) == 0 or prix == "PrixdeVente"):
                    continue

                if iChateau==1:
                    chateau=unidecode(row[2])
                elif iChateau==2:
                    chateau=unidecode(row[2]) +' blanc'
                elif iChateau==3:
                    chateau=unidecode(row[0])+' '+unidecode(row[2])
                else:
                    chateau=unidecode(row[0])+' '+unidecode(row[2])

                # chateau=re.sub(r'[0-9]','',chateau) ??
                # année
                annee : str = row[1]
                
                if "V1" in annee:
                    annee = "20"+annee[1:2]

                annee = ft.formaterAnnee(annee)

                # quantite
                quantite : str = ft.formaterQuantite(str(row[4]))
                
                # Format de la bouteille 
                formatB : str = ft.formaterFormatBouteille(row[3])

                # Prix
                prix : str = ft.formaterPrix(prix)

                #conditionnement
                conditionnement = str(row[8])

                conditionnement = ft.formaterConditionnement(formatB, int(quantite), conditionnement, chateau)

                commentaire="Degre : "+row[9]
            
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatB,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                writer.writerow(newRow)
            monFichierEntre.close()

