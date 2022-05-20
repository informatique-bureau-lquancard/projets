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
        nom_sortie='sortie_VINONE.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if "APPELATION" in row[0]:
                    bEcrire=0 
                elif row[0]=="":
                    bEcrire=0 
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=unidecode(row[1])+' '+unidecode(row[0])
                    

                    # annee
                    if row[2]=='':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[2]

                    # Format de bouteille
                    if row[5]=='0,75':
                        formatb='BO'
                    elif row[5]=='0,375':
                        formatb='DE'
                    elif row[5]=='1,5':
                        formatb='MG'
                    elif row[5]=='3':
                        formatb='DM'
                    elif row[5]=='6':
                        formatb='IM'
                    elif row[5]=='5':
                        formatb='JE'
                    elif row[5]=='12':
                        formatb='BA'
                    elif row[5]=='15':
                        formatb='NA'
                    elif row[5]=='18':
                        formatb='ME'
                    elif row[5]=='9':
                        formatb='SA'
                    elif row[5]=='27':
                        formatb='BABY'
                    else:
                        formatb=row[5]

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[6])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    quantite=row[4]


                    #on applique le conditionnement par defaut selon le format bouteille et la quantité
                    if row[3]=='':
                        if formatb=='DE' and int(quantite)<24:
                            conditionnement='UNITE'
                        elif formatb=='DE' and int(quantite)>=24:
                            conditionnement='CBO24DE'
                        elif formatb=='BO' and int(quantite)<12:
                            conditionnement='UNITE'
                        elif formatb=='BO' and int(quantite)>=12:
                            conditionnement='CBO12'
                        elif formatb=='MG' and int(quantite)<6:
                            conditionnement='UNITE'
                        elif formatb=='MG' and int(quantite)>=6:
                            conditionnement='CBO6'
                        elif formatb=='DM' and int(quantite)<3:
                            conditionnement='UNITE'
                        elif formatb=='DM' and int(quantite)>=3:
                            conditionnement='CBO3'
                        elif formatb=='JE' and int(quantite)>=1:
                            conditionnement='CBO1'
                        elif formatb=='IM' and int(quantite)>=1:
                            conditionnement='CBO1'
                        elif formatb=='CL' and int(quantite)<12:
                            conditionnement='UNITE'
                        elif formatb=='CL' and int(quantite)>=12:
                            conditionnement='CBO12'
                        else:
                            conditionnement='UNITE'
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace(' ','')
                        conditionnement=conditionnement.replace('CTO','CC')



                    #Commentaire
                    if row[3]=='':
                        commentaire='VERIF CDT'
                    else:
                        commentaire=''


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()