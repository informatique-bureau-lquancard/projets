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
        nom_sortie='sortie_SICHE2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if row[0]=="Nouveau":
                    index_chateau=-1
                elif row[0]=="":
                    index_chateau=-1
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=row[1]


                    # annee
                    if row[0]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[0]

                    # Format de bouteille
                    if '0.75 L' in row[2]:
                        formatb='BO'
                    elif '1.5 L' in row[2]:
                        formatb='MG'
                    elif '3 L' in row[2]:
                        formatb='DM'
                    elif '5 L' in row[2]:
                        formatb='JE'
                    elif '6 L' in row[2]:
                        formatb='IM'
                    elif '0.375 L' in row[2]:
                        formatb='DE'
                    else:
                        formatb=''

                    # conditionnement
                    if 'CT A PLAT de 6' in row[2]:
                        conditionnement='CC6PLA'
                    elif 'CT COUCHE de 6' in row[2]:
                        conditionnement='CC6PLA'
                    elif 'CT de 6' in row[2]:
                        conditionnement='CC6'
                    elif 'CB 12 1/2' in row[2]:
                        conditionnement='CBO12DE'
                    elif 'CB 24 1/2' in row[2]:
                        conditionnement='CBO24DE'
                    elif 'CT de 3' in row[2]:
                        conditionnement='CC3'
                    elif 'CB de 6' in row[2] or 'CB h.brion de 6' in row[2]:
                        conditionnement='CBO6'
                    elif 'CB de 3' in row[2]:
                        conditionnement='CBO3'
                    elif 'CB de 1 ' in row[2]:
                        conditionnement='CBO1'
                    elif 'CB de 12' in row[2]:
                        conditionnement='CBO12'
                    elif 'CB A PLAT de 6' in row[2]:
                        conditionnement='CBO6PLA'
                    else:
                        conditionnement='UNITE'




                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[4])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    if '12' in row[2]:
                        quantite=int(row[3])*12
                    elif '6' in row[2]:
                        quantite=int(row[3])*6
                    elif '3' in row[2]:
                        quantite=int(row[3])*3
                    elif '24' in row[2]:
                        quantite=int(row[3])*24
                    elif 'CB de 1' in row[2] or 'CT de 1' in row[2]:
                        quantite=row[3]
                    elif 'CB de 2' in row[2] or 'CT de 2' in row[2]:
                        quantite=int(row[3])*2
                    else:
                        quantite=row[3]



                    #Commentaire
                    commentaire='Prix plancher '+row[7]




                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)


            monFichierEntre.close()
