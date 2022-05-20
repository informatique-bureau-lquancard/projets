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
        nom_sortie='sortie_LDVOFF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                if row[5]=="":
                    bEcrire=0
                elif row[0]=="VIN":
                    bEcrire=0
                elif row[0]=="AOC":
                    bEcrire=0
                else:
                    # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                    bEcrire=1
                    chateau=unidecode(row[0])
                    

                    # annee
                    if row[1]=='NV' or row[1]=='NM':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[1]

                    # Format de bouteille
                    if row[2]=='75cL':
                        formatb='BO'
                    elif row[2]=='70cL':
                        formatb='BO'
                    elif row[2]=='50cL':
                        formatb='CL'
                    elif row[2]=='37,5cL':
                        formatb='DE'
                    elif row[2]=='150cL':
                        formatb='MG'
                    elif row[2]=='300cL':
                        formatb='DM'
                    elif row[2]=='600cL':
                        formatb='IM'
                    elif row[2]=='500cL':
                        formatb='JE'
                    elif row[2]=='1200cL':
                        formatb='BA'
                    elif row[2]=='1500cL':
                        formatb='NA'
                    elif row[2]=='1800cL':
                        formatb='ME'
                    elif row[2]=='900cL':
                        formatb='SA'
                    elif row[2]=='Primat':
                        formatb='BABY'
                    else:
                        formatb=row[2]

                    # Prix , on nettoie la chaine prix
                    if row[5]==' ★ ':
                        prix=0
                    else:
                        fPrix=repr(row[5])
                        fPrix=fPrix.replace("'","")
                        fPrix=fPrix.replace("\\","")
                        fPrix=fPrix.replace("u202f","")
                        prix=unidecode(fPrix)
                        prix=prix.replace(' EUR','')

                    #quantite
                    value=row[6]
                    value=value.replace(',','.')
                    value=value.replace(' ','')
                    value=value.replace('+','')
                    value=value.replace('-','')
                    value=value.replace('>','')
                    value=value.replace('★','')
                    quantite=0


                    if '-' in row[6]:
                        qMax=row[6]
                        qMax=qMax.replace(' ','')
                        qInd=qMax.find('-')
                    else:
                        qInd=0

                    for index in range(qInd, len(value)):
                        if value[index] in '0123456789.':
                            quantite=unidecode(value[qInd:])
                            quantite=quantite.replace(' ','')

                    #nettoyage de la chaine conditionnement
                    conditionnement=row[8]
                    conditionnement=conditionnement.replace(' ','')
                    conditionnement=conditionnement.replace('/','')
                    conditionnement=conditionnement.replace('0','')
                    conditionnement=conditionnement.replace('CT','CC')
                    conditionnement=conditionnement.replace('CB','CBO')
                    conditionnement=conditionnement.replace('btl','UNITE')
                    conditionnement=conditionnement.replace('BTL','UNITE')
                    



                    #Commentaire
                    commentaire='Special :  '+unidecode(row[9])


                       

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()