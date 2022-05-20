import csv
import glob
import re
import time
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_TERTRA.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                bEcrire=0
                if row[12]=='':
                    bEcrire=0
                elif row[12]=='Wine':
                    bEcrire=0
                elif 'Each' in row[10]:
                    bEcrire=0
                else:
                    bEcrire=1
                    # Nom du chateau
                    chateau=unidecode(row[12])
                    chateau=chateau.replace('CHATEAU ','')
                    chateau=chateau.replace('EX CHATEAU','')
                    chateau=chateau.replace(' - Ex-Château','')
                    chateau=chateau.replace(' - Ex-Château Latest Release','')
                    chateau=chateau.replace(' 2016 RELEASE','')
                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    if 'NV' in row[10]:
                        annee=time.strftime('%Y')
                    else:
                        annee=row[10]
                    # quantite
                    if row[8]=='':
                        quantite_fr=0
                    elif 'ENQUIRE' in row[8]:
                        quantite_fr=0
                    else:
                        quantite_fr=row[8]
                        
                    if row[7]=='':
                        quantite_uk=0
                    elif 'ENQUIRE' in row[7]:
                        quantite_uk=0
                    else:
                        quantite_uk=row[7]
                        
                    quantite=int(quantite_fr)+int(quantite_uk)
                    
                    # Format de la bouteille et conditionnement
                    if row[11]=='375ML':
                        formatb='DE'
                        if int(quantite)<24:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO24DE'
                    elif row[11]=='750ML':
                        formatb='BO'
                        if int(quantite)<12:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO12'
                    elif row[11]=='1.5L':
                        formatb='MG'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[11]=='3.0L':
                        formatb='DM'
                        if int(quantite)<6:
                            conditionnement='UNITE'
                        else:
                            conditionnement='CBO6'
                    elif row[11]=='5.0L':
                        formatb='JE'
                        conditionnement='CBO1'
                    elif row[11]=='6.0L':
                        formatb='IM'
                        conditionnement='CBO1'
                    elif row[11]=='9.0L':
                        formatb='SA'
                        conditionnement='CBO1'
                    elif row[11]=='15.0L':
                        formatb='NA'
                        conditionnement='CBO1'
                    else :
                        formatb=row[11]
                        conditionnement=''

                    # Prix
                    fPrix=repr(row[13])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')
                    prix=prix.replace('.',',')
                    prix=prix.replace(' ','')
                    # Commentaire
                    commentaire='Stock Fr/Uk - Verif cdt'
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
