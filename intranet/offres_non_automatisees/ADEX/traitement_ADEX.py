import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ADEX.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                # Nom du chateau
                if row[0]=='':
                    bEcrire=0
                elif row[0]!='' and row[1]=='':
                    bEcrire=0
                elif 'RAMEL' in row[0]:
                    bEcrire=0
                else:
                    bEcrire=1
                    chateau=unidecode(row[0])
                    chateau=chateau.replace('é','e')
                    chateau=chateau.replace('è','e')
                    chateau=chateau.replace('ê','e')
                    chateau=chateau.replace('û','u')
                    chateau=chateau.replace('’',' ')
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.strip()
                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    annee=row[1]
                    # quantite
                    quantite=row[2]
                    if row[3]=='CBO6':
                        quantite=str(int(quantite)*6)
                    elif row[3]=='CBN6':
                        quantite=str(int(quantite)*6)
                    elif row[3]=='CBO12':
                        quantite=str(int(quantite)*12)
                    elif row[3]=='CBN12':
                        quantite=str(int(quantite)*12)
                    elif row[3]=='CBO3':
                        quantite=str(int(quantite)*3)
                    elif row[3]=='CBO2':
                        quantite=str(int(quantite)*2)
                    elif row[3]=='OC12':
                        quantite=str(int(quantite)*12)
                    elif row[3]=='OC6':
                        quantite=str(int(quantite)*6)
                    elif row[3]=='CT12':
                        quantite=str(int(quantite)*12)
                    elif row[3]=='CT6':
                        quantite=str(int(quantite)*6)
                    else:
                        quantite=row[2]
                    # Format de la bouteille et conditionnement
                    if row[5]=='75':
                        formatb='BO'
                    elif row[5]=='150':
                        formatb='MG'
                    elif row[5]=='300':
                        formatb='DM'
                    elif row[5]=='500':
                        formatb='JE'
                    elif row[5]=='450':
                        formatb='RE'
                    elif row[5]=='600':
                        formatb='IM'
                    else:
                        formatb=row[5]
                    # Prix
                    fPrix=repr(row[7])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')
                    # conditionnement
                    cond=row[3]
                    if 'CBO' in str(cond):
                        conditionnement=row[3]
                    elif 'CBN' in str(cond):
                        conditionnement=row[3]
                    elif 'CT' in str(cond):
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace('CT','CC')
                    elif 'OC' in str(cond):
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace('OC','CC')
                    else:
                        conditionnement='UNITE'
                    #commentaire
                    commentaire=row[6]
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1:
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
