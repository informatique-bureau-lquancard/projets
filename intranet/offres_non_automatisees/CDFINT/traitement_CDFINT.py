# coding: utf-8
import csv
import glob
import re
import codecs


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CDFINT.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[0] == 'Désignation' :
                    bEcrire = 0
                elif row[0] != '' and row[1] == '':
                    bEcrire = 0
                else:
                    bEcrire = 1
                    # Nom du chateau
                    if row[2]=='Blanc':
                        chateau=row[0]+' '+'Blanc'
                    else:
                        chateau=row[0]
                        chateau=chateau.replace('CHATEAU ','')
                        chateau=chateau.replace('37.5cl half bottle','')
                        chateau=chateau.replace('75cl bottle','')
                        chateau=chateau.replace('1.5 l magnum','')
                        chateau=chateau.replace('Double Magnum 3 l','')
                        chateau=chateau.replace('Impériale 6 l','')
                        chateau=chateau.replace('Melchior 18 l','')
                        chateau=chateau.replace('Red ','')
                        chateau=chateau.replace('White ','')
                        chateau=re.sub(r'[0-9]','',chateau)

                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')

                    # année
                    annee=row[5]
                    # quantite
                    quantite=row[8]
                    # Format de la bouteille et conditionnement
                    if row[7]=='0.375':
                        formatb='DE'
                    elif row[7]=='0.500':
                        formatb='CL'
                    elif row[7]=='0.750':
                        formatb='BO'
                    elif row[7]=='1.500':
                        formatb='MG'
                    elif row[7]=='3.000':
                        formatb='DM'
                    elif row[7]=='4.500':
                        formatb='RE'
                    elif row[7]=='6.000':
                        formatb='IM'
                    elif row[7]=='18.000':
                        formatb='ME'
                    else :
                        formatb=row[7]
                    # Prix
                    prix=row[10].replace('.',',')
                    couleur=row[2]
                    appelation=row[3]
                    degre=row[6]


                    if 'CBO 12' in row[9]:
                        conditionnement = 'CBO12'
                    elif 'CBO 6' in row[9] and 'CBO 12' not in row[9] :
                        conditionnement = 'CBO6'
                    elif 'Cart.12' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC12'
                    elif 'Cart. 12' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC12'
                    elif 'Cart.6' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC6'
                    elif 'Cart. 6' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC6'
                    elif 'Carton 6' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC6'
                    elif 'Carton6' in row[9] and 'CB' not in row[9] :
                        conditionnement = 'CC6'
                    elif 'CB3' in row[9] or 'CBO 3' in row[9]:
                        conditionnement = 'CBO3'
                    elif 'T12' in row[9] :
                        conditionnement = 'CC12'
                    elif 'CB1' in row[9]:
                        conditionnement = 'CBO1'
                    elif 'M6' in row[9] and 'CB' not in row[9]:
                        conditionnement = 'CC6'
                    elif row[9]=='':
                        if formatb=='BO':
                            if int(quantite)<12:
                                conditionnement = 'UNITE'
                            else:
                                conditionnement = 'CBO12'
                        elif formatb =='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO24DE'
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement = 'UNITE'
                            else:
                                conditionnement = 'CBO6'
                        elif formatb == 'DM':
                            if int(quantite)<3:
                                conditionnement = 'UNITE'
                            else:
                                conditionnement = 'CBO3'
                        else:
                            conditionnement='CBO1'
                    else:
                        conditionnement = row[9]
                        conditionnement = conditionnement.replace(' ','')
                        conditionnement = conditionnement.replace('Cart.','CC')

                    if row[9]=='':
                        commentaire ='VERIF CDT'
                    else:
                        commentaire = row[9]


                if bEcrire == 1 :
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
