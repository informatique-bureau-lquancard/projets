# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

nomProfil : str = "ALIOFF"
extensionDebut : str = ".csv"
extensionFin : str = ".csv"

for filename in glob.glob('*' + extensionDebut):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_' + nomProfil + extensionFin
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            
            for row in reader:

                #On defini le nom du chateau
                vin : str = row[2]
                vin = vin.strip()

                #prix
                prix : str = ft.formaterPrix(str(row[4]))

                prix = prix.replace('/', '')

                designation_prix = ["PRICEBT"]

                if( ft.bLigneIncorrecte(prix, designation_prix, vin)):
                    continue;

                if(prix == "Priceunit"):
                    continue

                #année
                annee = ft.formaterAnnee(str(row[3]))

                #format bouteille
                formatB : str

                if row[3]=='Champagne':
                    if row[6]=='0,75':
                        formatB='BO'
                    elif row[6]=='1,5':
                        formatB='MG'
                    elif row[6]=='3':
                        formatB='JEROCH'
                    elif row[6]=='6':
                        formatB='MAT'
                else:
                    formatB = ft.formaterFormatBouteille(str(row[1]))

                #Quantité
                quantite = ft.formaterQuantite(row[0])

                #conditionnement
                conditionnement = ft.conditionnementParDefaut(formatB, int(quantite))

                #commentaire
                commentaire='VERIF CDT'

                #officieux
                officieux='1'

                trou=''

                newRow=[vin,annee,formatB,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
