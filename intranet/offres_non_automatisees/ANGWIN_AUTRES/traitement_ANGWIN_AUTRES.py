# -*- coding: utf-8 -*-
import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ANGWIN_AUTRES.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[1]=='Estate':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[3]
                    chateau=chateau.replace('é','e')
                    chateau=chateau.replace('è','e')
                    chateau=chateau.replace('ô','o')
                    chateau=chateau.replace('â','a')
                    # année, on garde seulement la date
                    if row[5]=='NA':
                        annee='2014'
                    elif row[5]=='SA':
                        annee='2014'
                    elif row[5]=='':
                        annee='2014'
                    else:
                        annee=row[5]
                    # quantite
                    quantite=row[7]
                    # Format de la bouteille & conditionnement par defaut
                    if row[6]=='75':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='50':
                        formatb='CL'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='37.5':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO24DE'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='62':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='70':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='150':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='1.5':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt - '+row[12]
                    elif row[6]=='300':
                        formatb='DM'
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[12]
                        else:
                            conditionnement='CBO3'
                            commentaire='Verif cdt - '+row[12]
                    else:
                        formatb=row[6]
                        conditionnement='UNITE'
                        commentaire='Verif cdt - '+row[12]
                    # Prix
                    prix=row[8]
                    prix=prix.replace('€','')
                    prix=prix.replace('.',',')

                    #tarif officieux
                    officieux='1'
                    
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
