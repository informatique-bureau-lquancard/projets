import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_'+filename
        with open(nom_sortie,'w',newline='') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                if row[4]=='Burgundy':
                    chateau=row[1]+' '+row[3]
                    chateau=chateau.replace('Château','')
                    chateau=chateau.replace('é','e')
                    chateau=chateau.replace('è','e')
                    chateau=chateau.replace('"','')
                else:
                    chateau=row[1]
                    chateau=chateau.replace('Château','')
                    chateau=chateau.replace('é','e')
                    chateau=chateau.replace('è','e')
                    chateau=chateau.replace('"','')
                #chateau=re.sub(r'[0-9]','',chateau)
                # année
                annee=row[2]
                # quantite
                quantite=row[7]
                quantite=quantite.replace('<','')
                quantite=quantite.replace('>','')
                # Format de la bouteille et conditionnement
                if row[5]=='37,5cl':
                    formatb='DE'
                elif row[5]=='75 cl':
                    formatb='BO'        
                elif row[5]=='150 cl':
                    formatb='MG'
                elif row[5]=='300 cl':
                    formatb='DE'
                elif row[5]=='500 cl':
                    formatb='JE'
                elif row[5]=='600 cl':
                    formatb='IM'
                else :
                    formatb=row[5]
                # Prix
                prix=row[8]
                prix=row[8].replace('.',',')
                prix=row[8].replace('€','')
                prix=row[8].replace(' ','')
                #conditionnement
                conditionnement=row[6]
                if row[6]=='':
                    if row[5]=='37,5cl':
                        if int(quantite)<24:
                            conditionnement='UNITE'
                            commentaires=row[12]+' - '+'Verif cdt'
                        else:
                            conditionnement='CBO24DE'
                            commentaires=row[12]+' - '+'Verif cdt'
                    elif row[5]=='75 cl':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaires=row[12]+' - '+'Verif cdt'
                        else:
                            conditionnement='CBN12'
                            commentaires=row[12]+' - '+'Verif cdt'
                    elif row[5]=='150 cl':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaires=row[12]+' - '+'Verif cdt'
                        else:
                            conditionnement='CBN6'
                            commentaires=row[12]+' - '+'Verif cdt'
                    elif row[5]=='300 cl':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaires=row[12]+' - '+'Verif cdt'
                        else:
                            conditionnement='CBN3'
                            commentaires=row[12]+' - '+'Verif cdt'
                    elif row[5]=='500 cl':
                        conditionnement='CBO1'
                        commentaires=row[12]+' - '+'Verif cdt'
                    elif row[5]=='600 cl':
                        conditionnement='CBO1'
                        commentaires=row[12]+' - '+'Verif cdt'
                else:
                    conditionnement=row[6]
                    conditionnement=conditionnement.replace(' ','')
                    conditionnement=conditionnement.replace('owc','CBO')
                    conditionnement=conditionnement.replace('OWC','CBO')
                    conditionnement=conditionnement.replace('ACQ','')
                    conditionnement=conditionnement.replace('CRD','')
                    conditionnement=conditionnement.replace('CT','CC')
                    conditionnement=conditionnement.replace('OC','CC')
                    conditionnement=conditionnement.replace('CB12','CBO12')
                    conditionnement=conditionnement.replace('plat','PLA')
                    conditionnement=conditionnement.replace('flat','PLA')
                    conditionnement=conditionnement.replace('Flat','PLA')
                commentaires=''
                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires]
                writer.writerow(newRow)
            monFichierEntre.close()
