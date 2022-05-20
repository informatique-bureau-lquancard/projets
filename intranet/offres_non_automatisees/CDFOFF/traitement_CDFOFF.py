# coding: utf-8
import csv
import glob
import re
import codecs
import time
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CDFOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                bEcrire=0
                if 'Désignation' in row[0]:
                    bEcrire=0
                elif 'Name' in row[0]:
                    bEcrire=0
                else:
                    bEcrire=1
                    # Nom du chateau
                    if 'White' in row[1]:
                        chateau=row[0]+' '+'Blanc'
                    else:
                        chateau=row[0]
                        chateau=chateau.replace('CHATEAU ','')
                        chateau=chateau.replace('37.5cl half bottle','')
                        chateau=chateau.replace('75cl bottle','')
                        chateau=chateau.replace('1.5 l magnum','')
                        chateau=chateau.replace('Double Magnum 3 l','')
                        chateau=chateau.replace('Impériale 6 l','')
                        chateau=chateau.replace('Melchior 18 l','')
                        chateau=chateau.replace('Red ','')
                        chateau=chateau.replace('White ','')
                        chateau=re.sub(r'[0-9]','',chateau)
                    # année
                    annee=row[4]
                    # quantite
                    quantite=row[6]
                    # Format de la bouteille et conditionnement

                    if '0,75' in row[5]:
                        formatb='BO'
                    elif '1,5' in row[5]:
                        formatb='MG'
                    elif row[5]=='3' or row[5]=='3,000':
                        formatb='DM'
                    elif row[5]=='0,375':
                        formatb='DE'
                    elif row[5]=='5' or row[5]=='5,000':
                        formatb='JE'
                    elif row[5]=='6' or row[5]=='6,000':
                        formatb='IM'
                    elif row[5]=='15' or row[5]=='15,000':
                        formatb='NA'
                    else:
                        formatb=unidecode(row[5])



                    #conditionnement
                    if 'CBO 12' in row[7]:
                        conditionnement='CBO12'
                    elif 'CBO 6' in row[7] and 'CBO 12' not in row[7]:
                        conditionnement='CBO6'
                    elif 'Cart.12' in row[7] and 'CB' not in row[7]:
                        conditionnement='CC12'
                    elif 'Cart.6' in row[7] and 'Cart.12' not in row[7] and 'CB' not in row[7]:
                        conditionnement='CC6'
                    elif 'Cart.6' in row[7]:
                        conditionnement='CC6'
                    else:
                        conditionnement='UNITE'


                    #commentaire
                    if conditionnement=='UNITE':
                        commentaire=row[7]
                    else:
                        commentaire=''




                    # Prix
                    if row[8]=='':
                        bEcrire=0
                    else:
                        bEcrire=1
                        prix=row[8].replace('.',',')

                    officieux = 1

                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux]
                    writer.writerow(newRow)
            monFichierEntre.close()
