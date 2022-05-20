## coding: utf-8
import csv
import glob
import re
import io
import time
import sys
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_DEWITT3.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')


            iChateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:
                bEcrire=0
                if "BORDEAUX" in row[0] or "BOURGOGNE" in row[0] or "VALLEE DU RHONE" in row[0] or "AUTRES" in row[0] : #on identifie les lignes d'où doit partir le traitement
                    iChateau = 1
                else:
                    if row[4]=='': # on exclue les lignes sans prix
                        chateau = ''
                        bEcrire = 0
                    elif iChateau == 1: #on traite les lignes bordeaux
                        chateau=unidecode(row[0])
                        bEcrire = 1




                    # annee, si vins non millesimé on prend l'année systeme
                    if row[2]=='NV':
                        annee='NV'
                    elif row[2] == '0':
                        anne = 'NV'
                    else:
                        annee=row[2]

                    # Format de bouteille
                    if row[1] == '37,5 cl':
                        formatb = 'DE'
                    elif row[1] == '75 cl':
                        formatb = 'BO'
                    elif row[1] == '150 cl':
                        formatb = 'MG'
                    elif row[1] == '300 cl':
                        formatb = 'DM'
                    elif row[1] == '500 cl':
                        formatb = 'JE'
                    elif row[1] == '600 cl':
                        formatb = 'IM'
                    else:
                        formatb=row[1]

                    # Prix, nettoyage de la chaine prix ascii
                    fPrix=repr(row[4])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" ","")
                    prix=prix.replace("EUR","")


                    #quantite
                    quantite=row[3]

                    #conditionnement
                    if "COFFRET" in row[5]:
                        conditionnement="Cof"
                    elif row[5]=="":
                        conditionnement="UNITE"
                    elif row[5]!="":
                        conditionnement=row[5]
                        conditionnement=conditionnement.replace("CART","CC")
                        conditionnement=conditionnement.replace("CO","CC")
                        conditionnement=conditionnement.replace('GIFTBOX 1','GIBO1')






                    #Commentaire
                    #commentaire=row[8]





                #écriture de la ligne
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement]
                    writer.writerow(newRow)


            monFichierEntre.close()
