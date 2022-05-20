import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_MONTAG.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                chateau=row[0]
                chateau=chateau.replace('é','e')
                chateau=chateau.replace('è','e')
                chateau=chateau.replace('ê','e')
                chateau=chateau.replace('û','u')
                chateau=chateau.replace('’',' ')
                chateau=chateau.replace('Ch. ','')
                # chateau=re.sub(r'[0-9]','',chateau) ??
                # année
                annee=row[3]
                # quantite
                quantite=row[6]
                # Format de la bouteille et conditionnement
                
                if row[4]=='Bouteille':
                    formatb='BO'
                    if int(quantite)<12:
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    else:
                        conditionnement='CBO12'
                        commentaire='Verif cdt'
                elif row[4]=='Magnum':
                    formatb='MG'
                    if int(quantite)<6:
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    else:
                        conditionnement='CBO6'
                        commentaire='Verif cdt'
                elif row[4]=='Double Magnum':
                    formatb='DM'
                    if int(quantite)<3:
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    else:
                        conditionnement='CBO3'
                        commentaire='Verif cdt'
                elif row[4]=='Demie':
                    formatb='DE'
                    if int(quantite)<24:
                        conditionnement='UNITE'
                        commentaire='Verif cdt'
                    else:
                        conditionnement='CBO24DE'
                        commentaire='Verif cdt'
                elif row[4]=='':
                    pass
                else:
                    formatb=row[4]
                    conditionnement=''
                    commentaire=''
                # Prix
                prix=row[7]
                # couleur
                couleur=row[1]
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou,couleur]
                writer.writerow(newRow)
        monFichierEntre.close()
