import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_WILKIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[1]=='' :
                    bEcrire=0
                elif 'Wine' in row[1]:
                    bEcrire=0
                else:
                    # On ne garde que le format bouteille
                    if row[2]=='Bottle':
                        bEcrire = 1
                        formatb='BO'

                        # Nom du chateau
                        chateau=unidecode(row[1])
                        chateau=chateau.replace('Ch ','')
                        chateau=chateau.replace('"','')
                        chateau=chateau.replace(',',' ')
                        chateau=chateau.replace('.',' ')
                        if '(' in chateau  :
                            idetail = chateau.find('(')
                            commentaire = chateau[int(idetail):]
                            chateau = chateau.replace(commentaire,'')
                        elif 'Contains' in chateau :
                            idetail = chateau.find('Contains')
                            commentaire = chateau[int(idetail):]
                            chateau = chateau.replace(commentaire,'')
                        else:
                            commentaire = ''
                        #chateau=re.sub(r'[0-9]','',chateau)

                        chateau= chateau.upper()

                        # année
                        annee=row[0]

                        # Prix
                        #fPrix=repr(row[6])
                        fPrix=unidecode(row[6])
                        fPrix=fPrix.replace('EUR','')
                        fPrix=fPrix.replace(' ','')
                        # fPrix=fPrix.replace("'","")
                        # fPrix=fPrix.replace("EUR ","")
                        # fPrix=fPrix.replace(",","")
                        # fPrix=fPrix.replace(".",",")
                        prix=fPrix

                        # quantite
                        if row[3]!='' and row[4]=='':
                            csqte = int(re.findall('[\d]+',row[3])[0])
                            quantite = csqte * 12
                            conditionnement='CBO12'
                        elif row[3]!='' and row[4]!='':
                            csqte = int(re.findall('[\d]+',row[3])[0])
                            uqte = int(re.findall('[\d]+',row[4])[0])
                            quantite = (csqte * 12)+uqte
                            conditionnement='CBO12'
                        elif row[3]=='' and row[4]!='':
                            quantite = re.findall('[\d]+',row[4])[0]
                            conditionnement = 'UNITE'
                        elif 'assortment' in chateau :
                            quantite = '1'
                            conditionnement = 'COLLEC'

                        # conditionnement
                        # commentaires (on met la quantité et les commentaires)
                        # commentaires='bts :'+row[4]+' - '+'cases : '+row[3]
                        # commentaires=commentaires.replace(')','')
                        # tarif officieux
                        officieux='1'
                    else :
                        bEcrire = 0
                if bEcrire==1:
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
