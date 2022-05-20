import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ENSEI2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[2]=='':
                    pass
                elif row[2]=='Château':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[2]
                    chateau=chateau.replace('Â','A')
                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    annee=row[1]
                    # quantite
                    quantite=row[4]
                    quantite=quantite.replace('*','')
                    # Format de la bouteille 
                    if row[3]=='Bouteille':
                        formatb='BO'
                    elif row[3]=='bouteille':
                        formatb='BO'
                    elif row[3]=='Magnums':
                        formatb='MG'
                    elif row[3]=='magnums':
                        formatb='MG'
                    elif row[3]=='Demi':
                        formatb='DE'
                    else:
                        formatb=''
                    # Prix
                    prix=row[5]
                    prix=prix.replace('€','')
                    prix=prix.replace('.',',')
                    prix=prix.replace(' ','')
                    #conditionnement et commenatire
                    if row[7]=='':
                        if formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT - '+row[8]
                            else:
                                conditionnement='CBO12'
                                commentaire='VERIF CDT - '+row[8]
                        if formatb=='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT - '+row[8]
                            else:
                                conditionnement='CBO24DE'
                                commentaire='VERIF CDT - '+row[8]
                        if formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT - '+row[8]
                            else:
                                conditionnement='CBO6'
                                commentaire='VERIF CDT - '+row[8]
                        else:
                            conditionnement='UNITE'
                            commentaire='VERIF CDT - '+row[8]
                    else:
                        conditionnement=row[7]
                        conditionnement=conditionnement.replace('OWC','CBO')
                        commentaire=row[8]
                            
                    
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
