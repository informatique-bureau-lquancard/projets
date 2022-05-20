# coding: utf-8
import csv
import glob
import re
from unidecode import unidecode
import json
import decimal
import requests
import requests


# récupération du taux de change GBP vs EUR
url = 'https://api.exchangeratesapi.io/latest?base=GBP'
req = requests.get(url)
dico = req.json()
j_rates = dico.get('rates')
eur_rate = j_rates.get('EUR')


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CRSFW.csv'

        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
              bEcrire = 0
              if 'Price' not in row[7]:
                bEcrire = 1
                if row[2]!='':
                  vin = unidecode(row[2])+' '+unidecode(row[1])
                else:
                  vin = unidecode(row[1])

                vin = vin.upper()
                vin = vin.replace(',','')
                vin = vin.strip()

                annee = row[0]

                size = row[5].upper()
                if '75CL' or 'BT' in size:
                  formatb = 'BO'
                elif '150CL' in size:
                  formatb = 'MG'
                elif '3L' in size:
                  formatb = 'DM'
                elif '37.5CL' in size:
                  formatb = 'DE'
                elif '5L' in size:
                  formatb = 'JE'
                elif '6L' in size :
                  formatb = 'IM'
                elif '9L' in size:
                  formatb = 'SA'
                elif '12L' in size:
                  formatb = 'BA'
                elif '15L' in size:
                  formatb = 'NA'
                elif '18L' in size:
                  formatb = 'ME'
                elif '27L' in size:
                  formatb = 'BABY'

                fprix = unidecode(row[7])
                fprix = fprix.replace('PS','')
                fprix = fprix.replace(' ','')
                fprix = fprix.replace(',','.')
                fprix = float(fprix)

                prix = fprix * eur_rate
                prix = str(prix)
                prix = prix.replace('.',',')

                # on determine si on est CBO ou en UNITE
                if 'CS' in size :
                  find_uCond = size.split('X')[0]
                  uCond = find_uCond.replace('CS(','')
                  quantite = int(row[4])*int(uCond)
                  conditionnement = 'CBO'+uCond
                else:
                  quantite = row[4]
                  conditionnement = 'UNITE'



                if bEcrire == 1 :
                  newRow=[vin,annee,formatb,prix,quantite,conditionnement]
                  writer.writerow(newRow)
    monFichierEntre.close()
