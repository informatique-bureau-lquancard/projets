import csv
import glob
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_'+'TRANSV.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[0]=='':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[0]
                    chateau=chateau.replace('MAGNUM','')
                    chateau=chateau.replace('MAG','')
                    chateau=chateau.replace('1/2 BT','')
                    chateau=chateau.replace('JERO','')
                    # année
                    annee=row[2]
                    # quantite
                    if 'C12' in row[5]:
                        quantite=int(row[4])*12
                    elif 'C6' in row[5]:
                        quantite=int(row[4])*6
                    elif 'CB12' in row[5]:
                        quantite=int(row[4])*12
                    elif 'CB6' in row[5]:
                        quantite=int(row[4])*6
                    else:
                        quantite=row[4]
                    # Format de la bouteille
                    if row[6]=='0,375':
                        formatb='DE'
                    elif row[6]=='0,75':
                        formatb='BO'
                    elif row[6]=='0.75':
                        formatb='BO'
                    elif row[6]=='1,5':
                        formatb='MG'
                    elif row[6]=='1.5':
                        formatb='MG'
                    elif row[6]=='3':
                        formatb='DM'
                    elif row[6]=='5':
                        formatb='JE'
                    elif row[6]=='6':
                        formatb='IM' 
                    elif row[6]=='9':
                        formatb='SA'
                    elif row[6]=='12':
                        formatb='BA'
                    elif row[6]=='15':
                        formatb='NA'
                    elif row[6]=='18':
                        formatb='ME'
                    else :
                        formatb=row[6]
                    # conditionnement
                    if row[5]=='Bouteille':
                        conditionnement='UNITE'
                    elif row[5]=='Demi':
                        conditionnement='UNITE'
                    elif row[5]=='Magnum':
                        conditionnement='UNITE'
                    elif row[5]=='Jéro':
                        conditionnement='UNITE'
                    else:
                        if row[7]=='cs neutre':
                            conditionnement=row[5]
                            conditionnement=conditionnement.replace('CB','CBN')
                        else:
                            conditionnement=row[5]
                            conditionnement=conditionnement.replace('CB','CBO')
                            conditionnement=conditionnement.replace('C6','CC6')
                            conditionnement=conditionnement.replace('C12','CC12')
#                    if formatb=='DE':
#                            conditionnement='UNITE'
#                        else:
#                            conditionnement='CBO24DE'
#                    elif formatb=='BO':
#                        if int(quantite)<12:
#                            conditionnement='UNITE'
#                        else:
#                            conditionnement='CBO12'
#                    elif formatb=='MG':
#                        if int(quantite)<6:
#                            conditionnement='UNITE'
#                        else:
#                            conditionnement='CBO6'
#                    elif formatb=='DM':
#                        if int(quantite)<3:
#                            conditionnement='UNITE'
#                        else:
#                            conditionnement='CBO3'
#                    elif formatb=='JE':
#                        conditionnement='CBO1'
#                    elif formatb=='IM':
#                        conditionnement='CBO1'
#                    elif formatb=='SA':
#                        conditionnement='CBO1'
#                    elif formatb=='BA':
#                        conditionnement='CBO1'
#                    elif formatb=='NA':
#                        conditionnement='CBO1'
#                    elif formatb=='ME':
#                        conditionnement='CBO1'
#                    else:
#                        conditionnement=''
                    # Prix
                    prix=row[3]
                    # commentaire
                    commentaire=row[7]+' - '+row[8]
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
