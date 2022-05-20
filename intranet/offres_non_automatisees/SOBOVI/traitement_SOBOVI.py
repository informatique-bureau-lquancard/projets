import csv
import glob


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_SOBOVI.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                commentaire=''
                # Nom du chateau
                if 'White' in row[0]:
                    chateau=row[2]+' blanc'
                else:
                    chateau=row[2]
                # année
                annee=row[1]
                # quantite
                if row[5]=='>60':
                    quantite='60'
                    commentaire=' Vol. >60 units'
                else:
                    quantite=row[5]
                # Format de la bouteille et conditionnement
                if row[6]=='Bouteille':
                    formatb='BO'
                    if int(quantite)<12:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO12'
                elif row[6]=='Magnum':
                    formatb='MG'
                    if int(quantite)<6:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO6'
                elif row[6]=='Double-Magnum':
                    formatb='DM'
                    if int(quantite)<3:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO3'
                else :
                    formatb=row[6]
                    conditionnement=''
                # Prix
                prix=row[7].replace(' €','')
                # Commentaire
                commentaire=row[10]+commentaire
                # couleur
                couleur=row[0]
                # appelation
                appelation=row[3]
                # cru
                cru=row[4]
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
