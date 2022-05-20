import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8



for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_SODIVI.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[1]=='' or row[1]=='Château':
                    pass
                else:
                    # Nom du chateau
                    if row[3]=='Bourgogne':
                        chateau=unidecode(row[1])+' '+unidecode(row[4])
                    else:
                        chateau=unidecode(row[1])

                    chateau=chateau.replace('CHATEAU ','')
                    chateau=chateau.replace('CHÂTEAU ','')
                    chateau=chateau.replace('Magnum','')
                    chateau=chateau.replace('Demi-bouteille','')
                    chateau=chateau.replace('Rarissime','')
                    chateau=chateau.replace('é','e')
                    chateau=chateau.replace('è','e')
                    chateau=chateau.replace('ê','e')
                    chateau=chateau.replace('û','u')
                    chateau=chateau.replace('’',' ')
                    chateau=chateau.replace('"','')
                    chateau=chateau.replace(',','')

                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    annee=row[0]
                    # quantite
                    quantite=row[9]
                    # Format de la bouteille et conditionnement
                    if row[5]=='0.375 l':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[5]=='0.250 l':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[5]=='0.75 l':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='0.73 l':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='0.72 l':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='0.70 l':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[5]=='1.00 l':
                        formatb='L'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[5]=='1.50 l':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[5]=='3.00 l':
                        formatb='DM'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[5]=='5.00 l':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[5]=='6.00':
                        formatb='IM'
                        conditionnement='CBO1'
                    else :
                        formatb=row[5]
                        conditionnement=''
                    # Prix
                    fPrix=repr(row[10])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')
                    # couleur
                    couleur=row[2]
                    # appelation
                    appelation=row[4]
                    # Commentaire
                    commentaire='Verif cdt - '+unidecode(row[8])
                    commentaire = commentaire.replace(',',' -')
                    commentaire = commentaire.replace('"','')
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
