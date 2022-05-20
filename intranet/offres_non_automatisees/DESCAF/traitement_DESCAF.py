# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_DESCAF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')
            
            commentaire=""

            for row in reader:
                bEcrire=0
                if row[10]=="Prix":
                    bEcrire=0
                elif row[10]=="":
                    bEcrire=0
                else:
                    bEcrire=1
                    #On defini le nom du chateau
                    if 'Blanc' in row[3]:
                       chateau=unidecode(row[8])+' Blanc'
                    else:
                        chateau=unidecode(row[8])


                    #Millésime
                    annee=row[9]

                    #Format de la bouteille
                    if row[7]=='75cl':
                        formatb='BO'
                    elif row[7]=='150cl':
                        formatb='MG'
                    elif row[7]=='300cl':
                        formatb='DM'
                    elif row[7]=='500cl':
                       formatb='JE'
                    elif row[7]=='600cl':
                        formatb='IM'
                    elif row[7]=='1500cl':
                        formatb='NA'
                    elif row[7]=='1800cl':
                        formatb='ME'
                    elif row[7]=='2700cl':
                        formatb='BABY'
                    elif row[7]=='37,5cl':
                        formatb='DE'
                    else:
                        formatb=row[7]

                    #Prix
                    fPrix=repr(row[10])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" EUR","")
                    prix=prix.replace(".",",")

                    #quantité
                    if row[6]=="*":
                        quantite="24"
                        commentaire="1 a 10cs"
                    elif row[6]=="**":
                        quantite="240"
                        commentaire="10 a 50cs"
                    elif row[6]=="***":
                        quantite="720"
                        commentaire="50 a 100cs"
                    elif row[6]=="****":
                        quantite="1600"
                        commentaire="+100 a 500cs"
                    elif row[6]=="*****":
                        quantite="6000"
                        commentaire="+500cs"


                    #Conditionnement
                    conditionnement='CBO12'


                    #tarif officieux
                    officieux='1'
                

                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
