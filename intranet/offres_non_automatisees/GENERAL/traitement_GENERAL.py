import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

nomProfil : str = "GENERAL"
extensionDebut : str = ".csv"
extensionFin : str = ".csv"

for filename in glob.glob('*' + extensionDebut):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)

        nom_sortie='sortie_' + nomProfil + extensionFin
        
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')
            for row in reader:
                chateau=row[1]
                annee=row[2]
                formatb=row[5]
                prix=row[8]
                quantite=row[7]
                conditionnement=row[6]
                commentaires=row[6]
                if row[2]=='':
                    pass
                else:
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
                    chateau=re.sub(r'[0-9]','',chateau)
                    chateau = chateau.strip()
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
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
                    # Prix, nettoyage de la chaine prix ascii
                    fPrix=repr(row[8])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

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
                    elif row[6]=='OWC':
                        if row[5]=='75 cl':
                            if int(quantite)<12:
                                conditionnement='CBO'
                                commentaires=row[12]+' - '+'Verof cdt'
                            else:
                                conditionnement='CBO12'
                                commentaires=row[12]+' - Verif cdt'
                    elif 'OWC6 & 12' in row[6]:
                        conditionnement='CBO12'
                        commentaires='CBO6 & CBO12 '+row[12]
                    else:
                        conditionnement=row[6]
                        conditionnement=conditionnement.replace(' ','')
                        conditionnement=conditionnement.replace('CB','CBO')
                        conditionnement=conditionnement.replace('owc','CBO')
                        conditionnement=conditionnement.replace('OWC','CBO')
                        conditionnement=conditionnement.replace('ACQ','')
                        conditionnement=conditionnement.replace('CRD','')
                        conditionnement=conditionnement.replace('CT','CC')
                        conditionnement=conditionnement.replace('OC','CC')
                        conditionnement=conditionnement.replace('plat','PLA')
                        conditionnement=conditionnement.replace('flat','PLA')
                        conditionnement=conditionnement.replace('Flat','PLA')
                        conditionnement=conditionnement.replace('(Neutral)','')
                        commentaires=row[12]+' - Verif cdt'

                    if 'RFSE' in chateau :
                        commentaires=commentaires+' '+'RFSE'
                        chateau=chateau.replace('(RFSE)','')

                    # On fabrique la nouvelle ligne dans l'ordre voulu
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires]
                writer.writerow(newRow)
            monFichierEntre.close()
