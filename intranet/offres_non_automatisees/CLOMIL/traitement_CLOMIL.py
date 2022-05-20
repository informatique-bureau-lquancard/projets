## coding: utf-8
import csv
import glob
import re
import io
import time


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CLOMIL.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                if "Bordeaux" in row[0]:
                    index_chateau = 2
                elif "Bordeaux Blanc" in row[0]:
                    index_chateau = 3
                elif "Bourgogne" in row[0]:
                    index_chateau = 4
                elif "Champagne" in row[0]:
                    index_chateau = 4
                elif "Vallée du Rhône" in row[0]:
                    index_chateau = 4
                elif "Languedoc" in row[0]:
                    index_chateau = 4
                elif "Roussillon" in row[0]:
                    index_chateau = 4
                elif "Vallée de la Loire" in row[0]:
                    index_chateau = 4
                elif "Afrique du Sud" in row[0]:
                    index_chateau = 4
                elif "Porto" in row[0]:
                    index_chateau = 4
                elif "Alsace" in row[0]:
                    index_chateau = 4
                elif "Arménie Rouge" in row[0]:
                    index_chateau = 4
                elif "Baden Rouge" in row[0]:
                    index_chateau = 4
                elif "Bergerac Blanc" in row[0]:
                    index_chateau = 4
                elif "Bekaa Blanc" in row[0]:
                    index_chateau = 4
                elif "Barossa Rouge" in row[0]:
                    index_chateau = 4
                elif "Californie Rouge" in row[0]:
                    index_chateau = 4
                elif "Castilla y Leon" in row[0]:
                    index_chateau = 4
                elif "Corse" in row[0]:
                    index_chateau = 4
                elif "Jura" in row[0]:
                    index_chateau = 4
                elif "Lyonnais" in row[0]:
                    index_chateau = 4
                elif "Madrid" in row[0]:
                    index_chateau = 4
                elif "Maroc" in row[0]:
                    index_chateau = 4
                elif "Montreux" in row[0]:
                    index_chateau = 4
                elif "Mosel-saar-ruwer Blanc" in row[0]:
                    index_chateau = 4
                elif "Nahe Blanc" in row[0]:
                    index_chateau = 4
                elif "Neusiedlersee  Blanc" in row[0]:
                    index_chateau = 4
                elif "Pfalz Blanc" in row[0]:
                    index_chateau = 4
                elif "PIEDMONT" in row[0]:
                    index_chateau = 4
                elif "Poitou-Charentes" in row[0]:
                    index_chateau = 4
                elif "Priorat Rouge" in row[0]:
                    index_chateau = 4
                elif "Provence" in row[0]:
                    index_chateau = 4
                elif "Rheingau Blanc" in row[0]:
                    index_chateau = 4
                elif "Rheinhessen Blanc" in row[0]:
                    index_chateau = 4
                elif "Ribera del Duero Rouge" in row[0]:
                    index_chateau = 4
                elif "Rioja" in row[0]:
                    index_chateau = 4
                elif "Savoie" in row[0]:
                    index_chateau = 4
                elif "SICILE" in row[0]:
                    index_chateau = 4
                elif "Slovaquie" in row[0]:
                    index_chateau = 4
                elif "Sud Ouest" in row[0]:
                    index_chateau = 4
                elif "Suède" in row[0]:
                    index_chateau = 4
                elif "TOSCANE" in row[0]:
                    index_chateau = 4
                elif "Tras os Montes" in row[0]:
                    index_chateau = 4
                elif "Valais" in row[0]:
                    index_chateau = 4
                elif "Vallée de la Loire Rosé" in row[0]:
                    index_chateau = 4
                elif "Vallée du Rhône Rosé" in row[0]:
                    index_chateau = 4
                elif "VENETIE" in row[0]:
                    index_chateau = 4
                elif row[0]=="":# si vide, il ne faut rien faire finalement
                    index_chateau=-1 # on note -1 pour indiquer qu'on ne traite pas la ligne
                elif row[0]=="Vin": # pour identifier ta ligne d'entête que tu ne as pas traiter non plus
                    index_chateau=-1
                else:
                    # et là on traite les lignes
                    if index_chateau == 2:
                        # construction de ta ligne spécifique au cas 3
                        # et après tu peux énumérer tous tes cas particulier
                        chateau=row[0]
                        chateau=chateau.replace('â','a')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('ô','o')
                        bEcrire=1
                    elif index_chateau == 3 : 
                        if row[2]=='Pessac-Léognan': #on traite le cas spécifique des pessac leognan blanc
                            chateau=row[0]+' Blanc'
                            chateau=chateau.replace('â','a')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('ô','o')
                            bEcrire=1
                        else:
                            chateau=row[0]
                            chateau=chateau.replace('â','a')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('ô','o')
                            bEcrire=1
                    elif index_chateau == 4:
                        if row[1]!='':
                            chateau=row[1]+' '+row[0]
                            chateau=chateau.replace('â','a')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('ô','o')
                            bEcrire=1
                        else:
                            chateau=row[0]+' '+row[2]
                            chateau=chateau.replace('â','a')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('ô','o')
                            bEcrire=1

                    # annee
                    if row[3]=='':
                        annee=time.strftime('%Y')
                    else:
                        annee=row[3]

                    # Format de bouteille
                    if row[4]=='75':
                        formatb='BO'
                    elif row[4]=='70':
                        formatb='BO'
                    elif row[4]=='50':
                        formatb='CL'
                    elif row[4]=='150':
                        formatb='MG'
                    elif row[4]=='300':
                        formatb='DM'
                    elif row[4]=='450':
                        formatb='RE'
                    elif row[4]=='500':
                        formatb='JE'
                    elif row[4]=='600':
                        formatb='IM'
                    elif row[4]=='900':
                        formatb='SA'
                    elif row[4]=='1200':
                        formatb='BA'
                    elif row[4]=='1500':
                        formatb='NA'
                    elif row[4]=='1800':
                        formatb='ME'
                    elif row[4]=='2700':
                        formatb='BABY'
                    elif row[4]=='37.5' or row[4]=='37,5':
                        formatb='DE'
                    else:
                        formatb=row[4]

                    # Prix
                    prix=row[7]

                    
                    #prix=prix.replace(' ','')
                    #prix=prix.replace('€','')
                    #prix=prix.format(prix,2)

                    #quantite
                    quantite=row[6]

                    #conditionnement
                    if row[5]!='':
                        conditionnement=row[5]
                        conditionnement=conditionnement.replace('CBO/','CBO')
                        conditionnement=conditionnement.replace('C/','CC')
                        conditionnement=conditionnement.replace(' ','')
                        conditionnement=conditionnement.replace('JEROBOAM','')
                        conditionnement=conditionnement.replace('CAISSEBOIS','CBO')
                        conditionnement=conditionnement.replace('COFFRET','')
                        conditionnement=conditionnement.replace('COLLECTION','')
                        conditionnement=conditionnement.replace('IMPERIALE','')
                        conditionnement=conditionnement.replace('DOUBLE','')
                        conditionnement=conditionnement.replace('MAGNUM','')
                        vCond = 0
                    else:
                        if formatb=='DE' and int(quantite)<24:
                            conditionnement='UNITE'
                            vCond = 1
                        elif formatb=='DE' and int(quantite)>=24:
                            conditionnement='CBO24DE'
                            vCond = 1
                        elif formatb=='BO' and int(quantite)<12:
                            conditionnement='UNITE'
                            vCond = 1
                        elif formatb=='BO' and int(quantite)>=12:
                            conditionnement='CBO12'
                            vCond = 1
                        elif formatb=='MG' and int(quantite)<6:
                            conditionnement='UNITE'
                            vCond = 1
                        elif formatb=='MG' and int(quantite)>=6:
                            conditionnement='CBO6'
                            vCond = 1
                        elif formatb=='DM' and int(quantite)<3:
                            conditionnement='UNITE'
                            vCond = 1
                        elif formatb=='DM' and int(quantite)>=3:
                            conditionnement='CBO3'
                            vCond = 1
                        elif formatb=='JE':
                            conditionnement='CBO1'
                            vCond = 1
                        elif formatb=='RE':
                            conditionnement='CBO1'
                            vCond = 1
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            vCond = 1
                        elif formatb=='SA' or formatb=='BA' or formatb=='NA' or formatb=='ME' or formatb=='BABY':
                            conditionnement='CBO1'
                            vCond = 1
                        else:
                            conditionnement='UNITE'
                            vCond = 1

                    

                    #Commentaire
                    if vCond==1:
                        commentaire='VERIF CDT - '+row[8]
                    else:
                        commentaire=row[8]


                       

                # écriture de la ligne
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,trou,trou,trou]
                    writer.writerow(newRow)
                    
                    
            monFichierEntre.close()