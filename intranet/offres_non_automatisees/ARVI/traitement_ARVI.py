# -*-coding:Utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
import json
import decimal
#import currencylayer
import datetime

import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

# Quel jourt sommes nous ?
#now = datetime.now()
# et vers timestamp ?
#timestamp = datetime.timestamp(now)

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ARVI.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:

                bAssortiment : bool = False

                # Prix, RAS
                prix : str = unidecode(row[15])

                designation_prix = ["CHF p/bt"]

                # vin, Bordeaux et hors Bordeaux.
                if row[6] == "Bordeaux":
                    vin : str = unidecode(row[2])
                else:
                    vin : str = unidecode(row[3]+' '+row[2])

                vin = vin.upper()


                if(ft.bLigneIncorrecte(prix, designation_prix, vin)):
                    continue

                


                # prix = prix.replace(",",'.')
                # prix = prix.replace("'",'')

                # print(prix)

                # prix = float(prix) * 0.92
                # prix = round ( prix, 2 )

                # prix = prix.replace("'","")
                # prix = float(prix) * 0.92
                # prix = str(prix)
                # prix = prix.replace(".",",")

                # recherche des caisses collections / assotiments
                origin = row[4].upper()
                # assortment_finder = re.findall('[A][S][S][O][R]?[T]?[M]?[E]?[N]?[T]?[S]?',origin)
                # if assortment_finder :
                #     assortment_finder = "TRUE"
                # else:
                #     assortment_finder = "FALSE"

                # millesime, risque de changer quand on aura a mettre NV pour toutes les verticales.
                millesime = row[9]
                if millesime == 'NV' :
                    millesime_finder = re.findall('[0-9][0-9][.]?[0-9][0-9]',vin)
                    if millesime_finder :
                        millesime = millesime_finder[0]
                    else:
                        millesime = 'NV'

                # Recherche du format de bouteille selon assortiment ou non.

                if ("COLLEC" in vin) or ("ASSORT" in vin):

                    formatB : str = "COLLEC"

                    # Ne fonctionne pas quand il y a des bouteilles avec des formats différents
                    # MASSETO MASSETO COLLECTION 2018 (3X 75CL, 1X 150CL, 1X 300CL, 1X 600CL, 1X 1500CL)
                    # if ("75CL" in vin) or ("BOTTLES" in vin) :
                    #     formatB="BO"
                    # elif "150CL" in vin :
                    #     formatB="MG"
                    # else:
                    #     formatB="BO"

                    bAssortiment = True

                else:

                    # print(str(row[1]))

                    formatB  : str = ft.formaterFormatBouteille(str(row[1]))

                    # print(formatB)



                # quantités à 0
                quantite : str = ft.formaterQuantite(str(row[0]))

                if len(quantite) == 0:
                    quantite = 0

                if bAssortiment == True:
                    conditionnement = "COLLEC"
                    
                else:
                    conditionnement : str = ft.conditionnementParDefaut(formatB, int(quantite))

                # Recherche du commentaire dans la chaine chateau.
                if '(' in row[2] :
                    i = vin.find('(')
                    commentaire = vin[int(i):]
                else:
                    commentaire = ''

                commentaire = commentaire.replace(',',' ')
                commentaire = commentaire.strip()

                # Nettoyage de la chaine chateau, ca ne fait pas de mal.
                vin = vin.replace(commentaire,'')
                vin = vin.strip()

            #On fabrique la nouvelle ligne dans l'ordre voulu

                trou=''
                commentaire = commentaire.replace(',','')
                commentaire = commentaire.replace('(','')
                commentaire = commentaire.replace(')','')
                vin = vin.replace(',','')
                vin = vin.replace('(','')
                vin = vin.replace(')','')

                newRow = [vin,millesime,formatB,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
