## coding: utf-8
import csv
import glob
import re
import io
import time
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_VIALOF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            iChateau = ""
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if "Fine Wines offer" in row[0]:
                    bEcrire=0
                elif row[3]=="":
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    if row[0]!="" and row[3]!="": #on teste si le nom du chateau est présent en colonne 0, puis on stock l'info dans iChateau.
                        iChateau=row[0]
                        chateau=row[0]
                    else:
                        chateau=iChateau


                    # annee
                    if row[1]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[1]

                    # Format de bouteille
                    if row[2]=='0,75 L':
                        formatb='BO'
                    elif row[2]=='0,375 L':
                        formatb='DE'
                    elif row[2]=='1,5 L':
                        formatb='MG'
                    elif row[2]=='3 L':
                        formatb='DM'
                    elif row[2]=='6 L':
                        formatb='IM'
                    elif row[2]=='5 L' or row[2]=='4,5 L':
                        formatb='JE'
                    elif row[2]=='18 L':
                        formatb='BA'
                    elif row[2]=='15 L':
                        formatb='NA'
                    elif row[2]=='9 L':
                        formatb='SA'
                    elif row[2]=='27 L':
                        formatb='BABY'
                    else:
                        formatb=row[2]

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[3])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    quantite='0'

                    #on applique le conditionnement par defaut selon le format bouteille et la quantité
                    if 'OWC of 12' in row[4]:
                        conditionnement='CBO12'
                    elif 'OWC of 6' in row[4]:
                        conditionnement='CBO6'
                    elif 'OWC of 3' in row[4]:
                        conditionnement='CBO3'
                    elif 'OWC of 1' in row[4]:
                        conditionnement='CBO1'
                    elif 'CC of 12' in row[4]:
                        conditionnement='CC12'
                    elif 'CC of 6' in row[4]:
                        conditionnement='CC6'
                    elif 'CC of 3' in row[4]:
                        conditionnement='CC3'
                    elif 'CC of 1' in row[4]:
                        conditionnement='CC1'
                    else:
                        conditionnement='UNITE'



                    #Commentaire
                    commentaire='VERIF CDT - Qte = '+row[4]

                    Officieux = 1




                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,Officieux]
                    writer.writerow(newRow)


            monFichierEntre.close()
