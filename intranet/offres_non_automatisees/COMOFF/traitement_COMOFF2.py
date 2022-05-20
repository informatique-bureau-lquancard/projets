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
        nom_sortie='sortie_COMOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if "GRANDS CRUS" in row[0]:
                    bEcrire=0
                elif row[0]=="":
                    bEcrire=0
                elif row[0]=="Appellation":
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=unidecode(row[1])


                    # annee
                    if row[5]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[5]

                    # Format de bouteille
                    formatb='BO'

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[6])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    quantite=0

                    #conditionnement
                    conditionnement='CBO12'

                    #Commentaire
                    commentaire='QTE CBO6 : '+row[7]+' '+' QTE CBO12 :'+row[8]




                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)


            monFichierEntre.close()
