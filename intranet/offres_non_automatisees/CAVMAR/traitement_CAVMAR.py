import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CAVMAR.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'

                # Prix
                prix=row[6]

                if(prix in "Prix vente HT Franco"):
                    continue

                # Nom du chateau

                if ' Premiers Grands Crus Classés' in row[0] or 'Bordeaux' in row[0] or 'Sauternes' in row[0]:
                    chateau=unidecode(row[2])
                elif 'Bourgogne' or 'Rhone' in row[0]:
                    chateau=unidecode(row[1])+' '+unidecode(row[2])
                elif 'Champagne' or 'Languedoc' or 'Provence' or 'Alsace' or 'Loire' in row[0]:
                    chateau=unidecode(row[2])+' '+unidecode(row[1])
                elif 'Italie' in row[0]:
                    chateau=unidecode(row[1])
                elif 'Etats-Unis' in row[0]:
                    chateau=unidecode(row[2])
                else:
                    chateau=''

                # chateau=re.sub(r'[0-9]','',chateau) ??
                # année
                if row[3]=='':
                    annee='2014'
                else:
                    annee=row[3]
                # quantite
                quantite=row[5]
                # Format de la bouteille et conditionnement
                if row[4]=='btl.' or '75cl' in row[4] or '70 cl' in row[4]:
                    formatb='BO'
                    if row[9]==' - ':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='CBO - OWC':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='C.O. - OC':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CC12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    else:
                        conditionnement=row[9]
                        conditionnement=re.split(' - ',conditionnement)[0]

                        commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='50 cl':
                    formatb='CL'
                    if row[9]==' - ':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='CBO - OWC':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='C.O. - OC':
                        if int(quantite)<12:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CC12'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    else:
                        conditionnement=row[9]
                        conditionnement=re.split(' - ',conditionnement)[0]

                        commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='mag.':
                    formatb='MG'
                    if row[9]==' - ':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='CBO - OWC':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='C.O. - OC':
                        if int(quantite)<6:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CC6'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    else:
                        conditionnement=row[9]
                        conditionnement=re.split(' - ',conditionnement)[0]

                        commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='d-mag.':
                    formatb='DM'
                    if row[9]==' - ':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO6'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='CBO - OWC':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO3'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='C.O. - OC':
                        if int(quantite)<3:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CC3'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    else:
                        conditionnement=row[9]
                        conditionnement=re.split(' - ',conditionnement)[0]

                        commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='demi.':
                    formatb='DE'
                    if row[9]==' - ':
                        if int(quantite)<24:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO24DE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='CBO - OWC':
                        if int(quantite)<24:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CBO24DE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    elif row[9]=='C.O. - OC':
                        if int(quantite)<24:
                            conditionnement='UNITE'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                        else:
                            conditionnement='CC24'
                            commentaire='Verif cdt -'+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                    else:
                        conditionnement=row[9]
                        conditionnement=re.split(' - ',conditionnement)[0]

                        commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='imp.':
                    formatb='IM'
                    conditionnement='CBO1'
                    commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                elif row[4]=='jérob.':
                    formatb='JE'
                    conditionnement='CBO1'
                    commentaire=row[9]+row[13]+' - '+row[14]+' - '+row[15]+' - '+row[16]
                else:
                    formatb=''
                    conditionnement=''
                    commentaire=''

                conditionnement = conditionnement.replace('.','')
                conditionnement = conditionnement.replace('-','')
                conditionnement = conditionnement.replace('CO','CC')
                conditionnement = conditionnement.replace('Vrac','UNITE')

                # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux,trou,trou,trou]
                writer.writerow(newRow)
        monFichierEntre.close()
