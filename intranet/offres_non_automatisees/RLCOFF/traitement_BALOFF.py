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
        nom_sortie='sortie_BALOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if row[0]=="BORDEAUX GRANDS CRUS OFFER":
                    index_chateau=-1 
                elif row[0]=="":
                    index_chateau=-1
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=row[1]
                    

                    # annee
                    if row[3]=='NV':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[3]

                    # Format de bouteille
                    if row[6]=='bt.' or row[6]=='Blle.':
                        formatb='BO'
                    elif row[6]=='1/2bt.':
                        formatb='DE'
                    elif row[6]=='mag.':
                        formatb='MG'
                    elif row[6]=='d.mag.':
                        formatb='DM'
                    elif row[6]=='impé.':
                        formatb='IM'
                    elif row[6]=='jéro.':
                        formatb='JE'
                    elif row[6]=='balt.':
                        formatb='BA'
                    elif row[6]=='nabu.':
                        formatb='NA'
                    elif row[6]=='salm.':
                        formatb='SA'
                    elif row[6]=='Primat':
                        formatb='BABY'
                    else:
                        formatb=row[6]

                    # Prix , on nettoie la chaine prix
                    fPrix=repr(row[4])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(' EUR','')

                    #quantite
                    value=row[5]
                    value=value.replace(',','.')
                    value=value.replace(' ','')
                    value=value.replace('+','')
                    value=value.replace('-','')
                    value=value.replace('>','')
                    quantite='0'


                    if '-' in row[5]:
                        qMax=row[5]
                        qMax=qMax.replace(' ','')
                        qInd=qMax.find('-')
                    else:
                        qInd=0

                    for index in range(qInd, len(value)):
                        if value[index] in '0123456789.':
                            quantite=value[qInd:]

                    #on applique le conditionnement par defaut selon le format bouteille et la quantité
                    conditionnement=''
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



                    #Commentaire
                    commentaire='VERIF CDT - Qte = '+row[5]


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()