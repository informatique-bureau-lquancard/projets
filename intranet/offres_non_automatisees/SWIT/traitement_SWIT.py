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
        nom_sortie='sortie_SWIT.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if row[0]=="":
                    bEcrire=0
                elif "Country" in row[0]:
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    if row[1]=="Bordeaux":
                        chateau=unidecode(row[2])
                    else:
                        chateau=unidecode(row[2])+" "+unidecode(row[3]) 

                    

                    # annee
                    if 'NV' in row[4]:
                        annee=time.strftime('%Y')
                    else:
                        annee=row[4]

                    # Format de bouteille
                    if row[7]=='75cl':
                        formatb='BO'
                    elif row[7]=='1/2bt.':
                        formatb='DE'
                    elif row[7]=='150cl' or row[7]=='150':
                        formatb='MG'
                    elif row[7]=='300cl':
                        formatb='DM'
                    elif row[7]=='600cl':
                        formatb='IM'
                    elif row[7]=='500cl':
                        formatb='JE'
                    elif row[7]=='balt.':
                        formatb='BA'
                    elif row[7]=='nabu.':
                        formatb='NA'
                    elif row[7]=='salm.':
                        formatb='SA'
                    elif row[7]=='Primat':
                        formatb='BABY'
                    else:
                        formatb=row[7]

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[9])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    quantite=row[5]

                    #on applique le conditionnement par defaut selon le format bouteille et la quantité
                    conditionnement=row[8]
                    conditionnement=conditionnement.replace("OWC","CBO")
                    conditionnement=conditionnement.replace("OC","CC")
                    conditionnement=conditionnement.replace("Unit","UNITE")
                    conditionnement=conditionnement.replace(" ","")



                    #Commentaire
                    commentaire=''

                    #tarif hors bordeaux donc officieux
                    officieux="1"


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()