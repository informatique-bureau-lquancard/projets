import csv
import glob
import re
# coding: utf-8


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CEPAGE.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[1]=='' or row[1]=='MILLESIME':
                    pass
                else :
                    # Nom du chateau
                    chateau=row[0]

                    # année
                    annee=row[1]

                    # Format de la bouteille
                    if '75 cl' in row[4]:
                        formatb='BO'
                    elif '150 cl' in row[4]:
                        formatb='MG'
                    elif '300 cl' in row[4]:
                        formatb='DM'
                    elif '500 cl' in row[4]:
                        formatb='JE'
                    elif '600 cl' in row[4]:
                        formatb='DM'
                    else:
                        formatb=row[4]

                    #Prix
                    prix=row[2]

                    #Quantite en caisse, on traite le conditionnemment avec
                    if 'CBO de 3' in row[5]:
                        quantite=int(row[3])*3
                        conditionnement='CBO3'
                    elif 'CBO de 6' in row[5]:
                        quantite=int(row[3])*6
                        conditionnement='CBO6'
                    elif 'CBO de 12' in row[5]:
                        quantite=int(row[3])*12
                        conditionnement='CBO12'
                    elif 'CBO de 8' in row[5]:
                        quantite=row[3]
                        conditionnement='COLLEC'
                    else:
                        quantite=row[3]
                        conditionnement='UNITE'

                    #commentaire
                    commentaire=row[6]
                    
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
