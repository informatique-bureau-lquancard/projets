import csv
import glob
import re
from unidecode import unidecode

# coding: utf-8


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_PASTER.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar=';')
            for col in reader:
                current='0'
                if col[2]=='':
                    pass
                elif col[5]=='VINTAGE':
                    pass
                elif col[7]=='Sold out':
                    pass
                else :
                    # Nom du chateau
                    if col[1]=='Bordeaux Blanc':
                        chateau=col[0]+' Blanc'
                    elif col[1]=='Pessac-Léognan Blanc':
                        chateau=col[0]+' Blanc'
                    else:
                        chateau=col[0]
                    chateau=chateau.replace('â','a')
                    # chateau=re.sub(r'[0-9]','',chateau) ??

                    # année
                    annee=col[2]

                    # Format de la bouteille
                    formatb=col[6]
                    formatb=formatb.replace('Btle','BO')

                    # Prix
                    prix=col[8]

                    # quantite et conditionnement
                    quantite=col[7]
                    quantite=quantite.replace('sold out','0')
                    quantite=quantite.replace(' ','')
                    quantite=quantite.replace('+','')
                    if quantite=='Btles':
                        quantite='1'
                        conditionnement='UNITE'
                        commentaire='VERIF QTE - Free bottles only'
                    elif quantite=='0':
                        conditionnement='UNITE'
                        commentaire='SOLD OUT'
                    else:
                        if formatb=='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO24DE'
                                commentaire='VERIF CDT'
                        elif formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaire='VERIF CDT'                               
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO6'
                                commentaire='VERIF CDT'                        
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                                commentaire='VERIF CDT'
                            else:
                                conditionnement='CBO3'
                                commentaire='VERIF CDT'
                        elif formatb=='JE':
                            conditionnement='CBO1'
                            commentaire='VERIF CDT'
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            commentaire='VERIF CDT'
                        else:
                            conditionnement=''
                            commentaire=''
                                                     

                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                writer.writerow(newRow)
        monFichierEntre.close()
