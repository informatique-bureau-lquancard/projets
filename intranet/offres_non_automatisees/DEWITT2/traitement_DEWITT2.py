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
        nom_sortie='sortie_DEWITT2.csv'
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
                    # if row[4]=='': # on exclue les lignes sans prix
                    #     chateau = ''
                    #     bEcrire = 0
                    if 'vrac' in row[0] and row[4]=="":
                        bEcrire = 0
                        iVrac = 1
                    elif 'vrac' not in row[0] and row[4]=="":
                        bEcrire = 0
                        iVrac = 0
                    elif iChateau == 1: #on traite les lignes bordeaux
                        chateau=unidecode(row[0])
                        bEcrire = 1

                        chateau = chateau.replace('"','')
                        chateau = chateau.replace(',','')




                    # annee, si vins non millesimé on prend l'année systeme
                    if row[1]=='NV':
                        annee='NV'
                    else:
                        annee=row[1]

                    # Format de bouteille
                    if row[2] == '37,5 cl':
                        formatb = 'DE'
                    elif row[2] == '75 cl':
                        formatb = 'BO'
                    elif row[2] == '150 cl':
                        formatb = 'MG'
                    elif row[2] == '300 cl':
                        formatb = 'DM'
                    elif row[2] == '500 cl':
                        formatb = 'JE'
                    elif row[2] == '600 cl':
                        formatb = 'IM'
                    else:
                        formatb=row[2]

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



                    if "COFFRET" in row[7]:
                        conditionnement="Cof"
                    elif row[7]=="":
                        conditionnement="UNITE"
                    elif row[7]!="":
                        conditionnement=row[7]
                        conditionnement=conditionnement.replace("CART","CC")
                        conditionnement=conditionnement.replace("CO","CC")








                    #Commentaire
                    commentaire=row[10]
                    commentaire = commentaire.replace(',','')





                #écriture de la ligne
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)


            monFichierEntre.close()
