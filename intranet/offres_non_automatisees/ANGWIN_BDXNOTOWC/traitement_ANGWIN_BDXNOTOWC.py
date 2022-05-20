# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ANGWIN_BDXNOTOWC.csv'
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

                    # quantite
                    quantite=row[6]

                    # Format de la bouteille & conditionnement par defaut
                    if row[5]=='75':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='37.5':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[5]=='50':
                        formatb='CL'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='150':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[5]=='300':
                        formatb='DM'
                        if int(quantite)<3:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO3'
                    elif row[5]=='500':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[5]=='600':
                        formatb='IM'
                        conditionnement='CBO1'
                    else:
                        formatb=row[5]
                        conditionnement='UNITE'

                    #Commentaires
                    commentaire='Verif cdt - '+row[12]+' '+row[13]+' '+row[14]

                    # Prix
                    fPrix=repr(row[7])
                    fPrix=unidecode(fPrix)
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    fPrix=fPrix.replace(" EUR","")
                    prix=fPrix



                if bEcrire==1:
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux]
                    writer.writerow(newRow)
            monFichierEntre.close()
