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
        nom_sortie='sortie_VEYLOF2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if row[5]=="":
                    bEcrire=0 
                elif row[5]=="Price/unit":
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=row[1]
                    

                    # annee
                    if row[2]=='NV':
                        annee=time.strftime('%Y')
                    elif "CURVE" in row[1]:
                        annee="2016"
                    else:
                        annee=row[2]

                    # Format de bouteille
                    if row[7]=='Blle':
                        formatb='BO'
                    elif row[7]=='DemiBt':
                        formatb='DE'
                    elif row[7]=='Magnum':
                        formatb='MG'
                    elif row[7]=='DMagn':
                        formatb='DM'
                    elif row[7]=='Imp':
                        formatb='IM'
                    elif row[7]=='Jero':
                        formatb='JE'
                    elif row[7]=='Balt':
                        formatb='BA'
                    elif row[7]=='Nabu':
                        formatb='NA'
                    elif row[7]=='salm.':
                        formatb='SA'
                    elif row[7]=='Baby':
                        formatb='BABY'
                    else:
                        formatb=row[7]

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[5])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    if row[6]=="":
                        quantite="0"
                    elif row[6]!="":
                        quantite=row[6]

                    #on applique le conditionnement par defaut selon le format bouteille et la quantité
                    conditionnement="CBO12"                    



                    #Commentaire
                    commentaire='VERIF CDT & QTE - Degre = '+row[10]


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()