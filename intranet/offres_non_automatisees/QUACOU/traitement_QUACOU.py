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
        nom_sortie='sortie_QUACOU.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            iRegion = 0
            iChateau = ""
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:

                bEcrire=0
                if "Quatre Couleurs" in row[0]: #Traitement des lignes d'en-tête du fichier -1 car on fait rien
                    iRegion =-1
                elif "8 bis Bld du général Koenig" in row[0]:
                    iRegion =-1
                elif "44100 Nantes" in row[0]:
                    iRegion =-1
                elif "Tel:  33 (2) 51 80 42 70" in row[0]:
                    iRegion =-1
                elif "Fax: 33 (2) 51 80 72 87     E-Mail: Emmanuel@aux4couleurs.com" in row[0]:
                    iRegion =-1
                elif "Offer " in row[0]:
                    iRegion =-1
                elif "Vintage" in row[0]:
                    iRegion =-1
                #if "" in row[0] and "" in row[1]: #on ne traite pas les lignes dont les 2 premieres colonnes sont vides
                    #iRegion =-1
                elif "RHONE" in row[0] : #identification des lignes d'en-tête des régions.
                    iRegion = 1
                elif "ALSACE" in row[0]:
                    iRegion = 1
                elif "ARGENTINE" in row[0]:
                    iRegion = 1
                elif "BORDEAUX - WHITE" in row[0]:
                    iRegion = 2
                elif "BORDEAUX - RED" in row[0]:
                    iRegion = 3
                elif "BOURGOGNE" in row[0]:
                    iRegion = 1
                elif "CHAMPAGNE" in row[0]:
                    iRegion = 1
                elif "ESPAGNE" in row[0]:
                    iRegion = 1
                elif "ITALIE" in row[0]:
                    iRegion = 1
                elif "LANGUEDOC" in row[0]:
                    iRegion = 1
                elif "LOIRE" in row[0]:
                    iRegion = 1
                elif "PORTUGAL" in row[0]:
                    iRegion = 1
                elif "PROVENCE" in row[0]:
                    iRegion = 1
                elif "USA" in row[0]:
                    iRegion = 1
                else:
                    if iRegion == 1:
                        if row[1] !="" and row[2]=="" and row[3]=="" and row[4]=="": #on détecte si il y a une information dans la colonne 1 et pas ailleurs
                            iChateau = unidecode(row[1]) # on stock l'information dans iChateau
                            bEcrire=0 # on écrit pas
                        elif row[5]=="":
                            bEcrire=0
                        else:
                            chateau=iChateau+" "+unidecode(row[1]) #on construit Chateau en concatenant iChateau et row[1]
                            bEcrire=1
                    elif iRegion == 2:
                        if row[0]=="":
                            bEcrire=0
                        else:
                            chateau=unidecode(row[1])+' Blanc'
                            chateau=chateau.replace('MAGNUM','')
                            chateau=chateau.replace('JEROBOAM','')
                            bEcrire=1
                    elif iRegion == 3:
                        if row[5]=="":
                            bEcrire=0
                        else:
                            chateau=unidecode(row[1])
                            chateau=chateau.replace('MAGNUM','')
                            chateau=chateau.replace('JEROBOAM','')
                            bEcrire=1

                    # annee
                    if row[0]=='NV':
                        annee='NV'
                    else:
                        annee=row[0]
                    # Format de bouteille
                    if '75' in row[2]:
                        formatb='BO'
                    elif '150' in row[2]:
                        formatb='MG'
                    elif '300' in row[2]:
                        formatb='DM'
                    elif '500' in row[2]:
                        formatb='JE'
                    elif '600' in row[2]:
                        formatb='IM'
                    elif '37.5' in row[2] or '37,5' in row[2]:
                        formatb='DE'
                    elif '50 cl' in row[2]:
                        formatb='CL'
                    elif '70' in row[2]:
                        formatb='BO'
                    else:
                        formatb=row[2]

                    # Prix
                    fPrix=unidecode(row[5])
                    fPrix=fPrix.replace(" EUR","")
                    prix=fPrix.replace(" ","")
                    #quantite
                    quantite=row[4]
                    #conditionnement
                    if row[6]=='LOOSE':
                        conditionnement='UNITE'
                    else:
                        conditionnement=row[6]
                        conditionnement=conditionnement.replace('OWC','CBO')
                        conditionnement=conditionnement.replace('OCC','CC')
                        vCond=1  #test pour verif cdt
                    #Commentaire
                    commentaire = unidecode(row[10])

                # écriture de la ligne
                if bEcrire==1 :

                    chateau = chateau.replace('     ',' ')
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.strip()

                    if((chateau is None) or (len(chateau) == 0) or (prix is None) or (len(prix) == 0)):
                        continue 

                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
