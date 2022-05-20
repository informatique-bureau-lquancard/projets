import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_BPCWIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                if row[1]=='':
                    pass
                else:
                    if 'CHAMBERTIN' in row[1]:
                        chateau=unidecode(row[0])+' '+unidecode(row[1])+' '+unidecode(row[2])
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ê','e')
                        chateau=chateau.replace('û','u')
                        chateau=chateau.replace('’',' ')
                    elif 'HERMITAGE' in row[1]:
                        chateau=unidecode(row[0])+' '+unidecode(row[1])+' '+unidecode(row[2])
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ê','e')
                        chateau=chateau.replace('û','u')
                        chateau=chateau.replace('’',' ')
                    elif 'MONTRACHET' in row[1]:
                        chateau=unidecode(row[0])+' '+unidecode(row[1])+' '+unidecode(row[2])
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ê','e')
                        chateau=chateau.replace('û','u')
                        chateau=chateau.replace('’',' ')
                    elif 'Beaune' in row[1]:
                        chateau=unidecode(row[0])+' '+unidecode(row[1])+' '+unidecode(row[2])
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ê','e')
                        chateau=chateau.replace('û','u')
                        chateau=chateau.replace('’',' ')
                    else:
                        chateau=unidecode(row[0])
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ê','e')
                        chateau=chateau.replace('û','u')
                        chateau=chateau.replace('’',' ')

                    chateau=re.sub(r'[0-9]','',chateau)

                    # année
                    if '-' in row[3]:
                        i = int(row[3].find('-'))
                        annee = row[3][i+1:]
                    else:
                        annee = row[3]


                    # quantite
                    quantite=row[4]

                    # Format de la bouteille et conditionnement
                    if 'Blle' in row[5] :
                        formatb='BO'
                    elif row[5]=='MAGNUM':
                        formatb='MG'
                    elif row[5]=='D-MAGNUM':
                        formatb='DM'
                    elif row[5]=='JEROBOAM':
                        formatb='JE'
                    elif row[5]=='IMPERIALE':
                        formatb='IM'
                    else:
                        formatb=row[5]

                    # Prix
                    prix=unidecode(row[6])
                    prix=prix.replace('€','')
                    prix=prix.replace(' EUR','')
                    prix=prix.replace(' ','')
                    prix=prix.replace('.',',')

                    #commentaire
                    if i!='':
                        commentaire = row[3]+' '+row[7]
                    else:
                        commentaire=row[7]

                    # conditionnement
                    cond=row[8]
                    if 'CBO' in str(cond):
                        conditionnement=row[8]
                    elif 'CBN' in str(cond):
                        conditionnement=row[8]
                    elif 'CT' in str(cond):
                        conditionnement=row[8]
                        conditionnement=conditionnement.replace('CT','CC')
                    elif 'OC' in str(cond):
                        conditionnement=row[8]
                        conditionnement=conditionnement.replace('OC','CC')
                    else:
                        conditionnement='UNITE'
                        commentaire='VERIF CDT - '+row[8]+' '+row[7]

                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
