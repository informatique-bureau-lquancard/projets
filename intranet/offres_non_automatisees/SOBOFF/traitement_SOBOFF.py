import csv
import glob
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_SOBOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[2]=='':
                    bEcrire=0
                else:
                    bEcrire=1
                    commentaire=''
                    # Nom du chateau
                    if 'Blanc' in row[4] or 'BLANC' in row[4]:
                        chateau=unidecode(row[3])+' blanc'
                    else:
                        chateau=unidecode(row[3])
                    # année
                    annee=row[2]
                    # quantite
                    if '>' in row[6]:
                        quantite=row[6]
                        quantite=quantite.replace('>','')
                        commentaire='Vol quantite :'+' '+row[6]
                    else:
                        quantite=row[6]
                    # Format de la bouteille et conditionnement
                    if row[7]=='Bouteille' or row[7]=='Bottle':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[7]=='Half-Bottle':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[7]=='Magnum':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[7]=='Double-Magnum':
                        formatb='DM'
                        if int(quantite)<3:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO3'
                    elif row[7]=='Jeroboam':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[7]=='Imperial':
                        formatb='IM'
                        conditionnement='CBO1'
                    elif row[7]=='Nabuchadnezzar':
                        formatb='NA'
                        conditionnement='CBO1'
                    else :
                        formatb=row[7]
                        conditionnement='UNITE'
                    # Prix
                    fPrix=repr(row[8])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')
                    prix=prix.replace('.',',')
                    prix=prix.replace(' ','')

                    # Commentaire
                    if row[13]!="":
                        commentaire=unidecode(row[12])+'En prop.'
                    else:
                        commentaire=unidecode(row[12])
                    # couleur
                    couleur=row[1]
                    # appelation
                    appelation=row[4]

                    Officieux = '1'
                    # cru
                    cru=row[5]
                if bEcrire==1:
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    commentaire = commentaire.replace(',',' -')
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
