import csv
import glob
import re
from decimal import Decimal
import time
from unidecode import unidecode
# coding: utf-8

import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

nomProfil : str = 'MILLES_REGULIER'
# extensionDebut : str = '.xlsx'
# extensionFin_bis : str = '.xlsx'
extensionFin : str = '.csv'

for filename in glob.glob('*' + extensionFin):

    with open(filename, newline='', encoding='utf-8') as monFichierEntre:

        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_' + nomProfil + extensionFin

        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

            for row in reader:

                vin : str = unidecode(str(row[3])).upper()

                # Prix
                prix : str = ft.formaterPrix(str(row[6]))

                # print("prix : " + prix)

                designation_prix = ["PRIX()"]

                if( ft.bLigneIncorrecte(prix, designation_prix, vin)):
                    continue;

                # Nom du chateau
                vin = vin.replace('Â','A')
                vin = vin.replace('É','E')
                vin = vin.replace('Ü','U')
                vin = vin.replace('ô','o')
                #chateau=re.sub(r'[0-9]','',chateau)

                # année
                annee : str = ft.formaterAnnee(str(row[4]))

                # quantite
                quantite=row[1]
                quantite=quantite.replace(',','.')

                conditionnement  : str = str(row[2])

                if conditionnement == 'CB12':
                    conditionnement='CBO12'
                    quantite=str(float(quantite)*12)
                    quantite=quantite.replace('.0','')

                elif conditionnement == 'CB6':
                    conditionnement='CBO6'
                    quantite=str(float(quantite)*6)
                    quantite=quantite.replace('.0','')

                elif conditionnement == 'CB3':
                    conditionnement='CBO3'
                    quantite=str(float(quantite)*3)
                    quantite=quantite.replace('.0','')

                elif conditionnement == 'CB1':
                    conditionnement='CBO1'
                    quantite=str(float(quantite)*1)
                    quantite=quantite.replace('.0','')

                # Format de la bouteille et conditionnement      
                formatB : str = ft.formaterFormatBouteille(unidecode(str(row[5])))
                
                # Commentaires
                commentaires=unidecode(row[7])+' - '+unidecode(row[9])+' - '+unidecode(row[10])

                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[vin,annee,formatB,prix,quantite,conditionnement,commentaires,trou,trou]

                writer.writerow(newRow)

            monFichierEntre.close()
