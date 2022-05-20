import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_WINARO.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[1]=='':
                    pass
                elif row[1]=='APPELLATION':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[0]
                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    annee=row[3]
                    # quantite
                    quantite=row[4]
                    # Format de la bouteille 
                    if row[5]=='750 ml':
                        formatb='BO'
                    elif row[5]=='1500 ml':
                        formatb='MG'
                    elif row[5]=='3000 ml':
                        formatb='DM'
                    elif row[5]=='5000 ml':
                        formatb='JE'
                    elif row[5]=='6000 ml':
                        formatb='IM'
                    else:
                        formatb=row[2]
                    # Prix
                    prix=row[10]
                    prix=prix.replace('€','')
                    prix=prix.replace('.',',')
                    prix=prix.replace(' ','')
                    #conditionnement & commentaire
                    if row[6]=='':
                        conditionnement='UNITE'
                        commentaire='VERIF CDT'
                    else:
                        conditionnement=row[6]
                        conditionnement=conditionnement.replace('OWC 0','CBO')
                        conditionnement=conditionnement.replace('OWC ','CBO')
                        conditionnement=conditionnement.replace('CTO 0','CC')
                        conditionnement=conditionnement.replace('CTO ','CC')
                        commentaire=''
                        
                    
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
