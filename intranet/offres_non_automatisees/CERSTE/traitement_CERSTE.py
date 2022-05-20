import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CERSTE.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                if row[0]=='':
                    pass
                elif row[0]=='Bourgogne et Autres':
                    pass
                elif row[0]=='Produit/millésime':
                    pass
                else:
                    chateau=row[0]
                # chateau=re.sub(r'[0-9]','',chateau) ??
                # année
                if row[2]=='':
                    annee='NV'
                else:
                    annee=row[2]
                # quantite
                quantite=row[1]
                # Format bouteille, conditionnement et commentaire
                if row[5]=='75 CL':
                    formatb='BO'
                    if row[3]=='':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='75CL':
                    formatb='BO'
                    if row[3]=='':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='150 CL':
                    formatb='MG'
                    if row[3]=='':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='150CL':
                    formatb='MG'
                    if row[3]=='':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='300CL':
                    formatb='DM'
                    if row[3]=='':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO3'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='300 CL':
                    formatb='DM'
                    if row[3]=='':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt - '+row[4]
                        else:
                            conditionnement='CBO3'
                            commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='500 CL':
                    formatb='JE'
                    if row[3]=='':
                        conditionnement='CBO1'
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                elif row[5]=='500CL':
                    formatb='JE'
                    if row[3]=='':
                        conditionnement='CBO1'
                        commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='600 CL':
                    formatb='IM'
                    if row[3]=='':
                        conditionnement='CBO1'
                        commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                elif row[5]=='600CL':
                    formatb='IM'
                    if row[3]=='':
                        conditionnement='CBO1'
                        commentaire='Verif cdt - '+row[4]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        commentaire=row[4]
                else:
                    formatb=row[5]
                    conditionnement=row[3]
                    conditionnement=conditionnement.replace(' ','')
                    commentaire=row[4]
                # Prix
                prix=row[6]
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                writer.writerow(newRow)
        monFichierEntre.close()
