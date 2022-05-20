import csv
import glob


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_SOBOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                commentaire=''
                # Nom du chateau
                chateau=row[3]
                # année
                annee=row[2]
                # quantite
                if '>' in row[9]:
                    quantite=row[9]
                    quantite=quantite.replace('>','')
                    commentaire='Vol quantite :'+' '+row[9]
                else:
                    quantite=row[9]
                # Format de la bouteille et conditionnement
                if row[10]=='Bottle':
                    formatb='BO'
                    if int(quantite)<12:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO12'
                elif row[10]=='Magnum':
                    formatb='MG'
                    if int(quantite)<6:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO6'
                elif row[10]=='Double-Magnum':
                    formatb='DM'
                    if int(quantite)<3:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO3'
                elif row[10]=='Half-Bottle':
                    formatb='DE'
                    if int(quantite)<24:
                        conditionnement='UNITE'
                    else:
                        conditionnement='CBO24DE'
                elif row[10]=='Imperial':
                    formatb='IM'
                    conditionnement='CBO1'
                elif row[10]=='Nabuchadnezzar':
                    formatb='NA'
                    conditionnement='CBO1'
                elif row[10]=='Jeroboam':
                    formatb='JE'
                    conditionnement='CBO1'
                else :
                    formatb=row[10]
                    conditionnement='UNITE'
                # Prix
                prix=row[11].replace(' €','')
                # Commentaire
                commentaire=row[15]+commentaire
                # couleur
                couleur=row[1]
                # appelation
                appelation=row[4]
                # cru
                cru=row[5]
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,couleur,appelation,cru]
                writer.writerow(newRow)
        monFichierEntre.close()
