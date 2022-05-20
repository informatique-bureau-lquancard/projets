import csv
import glob
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ENCVIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau

                if " -" in row[2] or "- " in row[2]:
                    chateau='Verticale '+row[2]
                    tRow=row[2]
                    if ' 19' in row[2]:
                        iVerticale = row[2].find('19')
                    elif ' 20' in row[2]:
                        iVerticale = row[2].find('20')

                    iVerticale = int(iVerticale)
                    Verticale = tRow[iVerticale:]
                    chateau=chateau.replace(Verticale,"")

                else:
                    chateau=row[2]
                    tRow = ""
                    iVerticale = ""
                    Verticale = ""

                chateau = chateau.replace('"','')
                chateau = chateau.replace(',','')

                # année
                if Verticale!="":
                    annee=Verticale[-4:]
                else:
                    annee=row[5]

                # quantite
                quantite=row[8]
                # Format de la bouteille
                if row[6]=='37,5':
                    formatb='DE'
                elif row[6]=='75':
                    formatb='BO'
                elif row[6]=='150':
                    formatb='MG'
                elif row[6]=='300':
                    formatb='DM'
                elif row[6]=='500':
                    formatb='JE'
                elif row[6]=='600':
                    formatb='IM'
                elif row[6]=='900':
                    formatb='SA'
                elif row[6]=='1200':
                    formatb='BA'
                elif row[6]=='1500':
                    formatb='NA'
                elif row[6]=='1800':
                    formatb='ME'
                else :
                    formatb=row[6]
                # conditionnement
                if row[7]=='Unit.':
                    conditionnement='UNITE'
                else:
                    conditionnement=row[7]
                # Prix
                fPrix=repr(row[10])
                fPrix=fPrix.replace("'","")
                fPrix=fPrix.replace("\\","")
                fPrix=fPrix.replace("u202f","")
                fPrix=fPrix.replace(" ","")
                prix=fPrix


                #Commentaire
                if Verticale != "":
                    commentaire=Verticale
                else:
                    commentaire=""

                # appelation
                appelation=row[3]
                # classement
                classement=row[4]

                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
        monFichierEntre.close()
