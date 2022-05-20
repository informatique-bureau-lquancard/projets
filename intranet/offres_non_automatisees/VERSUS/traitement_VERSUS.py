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
        nom_sortie='sortie_VERSUS.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            iRegion = 0
            trou='' # besoin de le faire une seule fois
            chateau=""
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                #if "" in row[6]:
                    #iRegion=-1 
                #elif row[6]=="PU HT (€)":
                    #iRegion=-1
                #elif row[6]=="Contact us":
                    #iRegion=-1
                if "ALSACE" in row[1]:
                    iRegion=1
                elif "BORDEAUX" in row[1]:
                    iRegion=2
                elif "BOURGOGNE" in row[1]:
                    iRegion=1
                elif "CHAMPAGNE" in row[1]:
                    iRegion=1
                elif "JURA" in row[1]:
                    iRegion=1
                elif "SAVOIE" in row[1]:
                    iRegion=1
                elif "RHÔNE" in row[1]:
                    iRegion=1
                elif "LOIRE" in row[1]:
                    iRegion=1
                elif "PROVENCE" in row[1]:
                    iRegion=1
                elif "LANGUEDOC" in row[1]:
                    iRegion=1
                elif "SUD-OUEST" in row[1]:
                    iRegion=1
                elif "SPIRITUEUX" in row[1]:
                    iRegion=1
                elif row[1]!="" and row[6]=="":
                    bEcrire=0
                elif row[1]=="" and row[6]=="":
                    bEcrire=0
                elif row[5]=="Stock":
                    bEcrire=0
                elif row[6]=="Contact us":
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    if iRegion==1:
                        chateau=unidecode(row[0])+' '+unidecode(row[1])
                    elif iRegion==2:
                        chateau=unidecode(row[1])
                    else:
                        chateau="ERROR"
                    

                    # annee
                    if row[2]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[2]

                    # Format de bouteille
                    if "75cl" or "70cl"in row[3]:
                        formatb="BO"
                    elif "150cl" or "140cl"in row[3]:
                        formatb="MG"
                    elif "37,5cl" in row[3]:
                        formatb="DE"
                    elif "300cl" in row[3]:
                        formatb="DM"
                    elif "500cl" in row[3]:
                        formatb="JE"
                    elif "600cl" in row[3]:
                        formatb="IM"

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[6])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" EUR","")
                    prix=prix.replace(".",",")

                    #quantite
                    quantite=row[5]
                    quantite=quantite.replace("+","")

                    #conditionnement, on nettoie la chaine
                    if "OWC" in row[4]:
                        conditionnement=row[4]
                        conditionnement=conditionnement.replace("OWC","CBO")
                    elif "OC12" in row[4]:
                        conditionnement="CC12"
                    elif "OC6" in row[4]:
                        conditionnement="CC6"
                    elif "OC1" in row[4]:
                        conditionnement="CC1"
                    elif "Neutral" in row[4]:
                        conditionnement="UNITE"
                    else:
                        conditionnement=row[4]

                    



                    #Commentaire
                    commentaire='VERIF CDT - Qte = '+row[4]


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                        
                        
            monFichierEntre.close()