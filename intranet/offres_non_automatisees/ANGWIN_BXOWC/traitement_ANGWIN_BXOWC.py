# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ANGWIN_BXOWC.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'
                Wine=row[2]
                if row[1]=='Estate':
                    bEcrire=0
                else:
                    bEcrire=1
                    # Nom du chateau
                    if row[3]=='White':
                        chaine=unidecode(Wine)+' Blanc'
                    else :
                        chaine=unidecode(Wine)

                    #Split de la chaine
                    chaine=re.split('\d.+',chaine)
                    chateau = chaine[0]

                    # année, on garde seulement la date

                    annee=row[4]
                    # Format de la bouteille
                    if row[5]=='75':
                        formatb='BO'
                    elif row[5]=='150':
                        formatb='MG'
                    elif row[5]=='300':
                        formatb='DM'
                    else:
                        formatb=row[5]

                    # Prix
                    fPrix=repr(row[7])
                    fPrix=unidecode(fPrix)
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    fPrix=fPrix.replace(" EUR","")
                    prix=fPrix

                    # quantite
                    quantite=row[6]

                    # conditionnement
                    conditionnement=row[12]
                    conditionnement=conditionnement.replace('Original wood case - Sold by ','CBO')
                    conditionnement=conditionnement.replace('Orignal wood case - Sold by ','CBO')
                    conditionnement=conditionnement.replace('Original wood case - Soldy by ','CBO')
                    conditionnement=conditionnement.replace('Original wood case -Sold by ','CBO')
                    conditionnement=conditionnement.replace('Original wood case -Sold by ','CBO')
                    conditionnement=conditionnement.replace('Caisse bois d\'origine - Vendu par ','CBO')
                    conditionnement=conditionnement.replace('Caisse bois d\'origine - vendu par ','CBO')
                    conditionnement=conditionnement.replace('Caisse bois d\'origine- vendu par ','CBO')
                    conditionnement=conditionnement.replace('Caisse bois d\'origine- Vendu par ','CBO')
                    # Commentaire
                    commentaire=''

                if bEcrire==1:
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux]
                    writer.writerow(newRow)
            monFichierEntre.close()
