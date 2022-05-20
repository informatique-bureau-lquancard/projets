## coding: utf-8
import csv
import glob
import re
import io
import time
import sys
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_OENALI.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            for row in reader:
                ##################################################################
                ## Initilisation des variables,                                 ##
                ## Si changement dans l'ordre des colonnes du fichier d'entrée, ##
                ## faire la modification ci-dessous                             ##
                ##################################################################
                dFaux_amis = ['LAGRANGE','LATOUR']
                Appellation = unidecode(row[0]).upper()
                Vin = unidecode(row[1]).upper()
                Class = unidecode(row[3]).upper()
                Millesime = row[4].upper()
                iPrix = unidecode(row[6]).upper()
                Qte = row[7].upper()
                Format_bouteille = row[8].upper()
                Degre = Format_bouteille.upper()
                Regie = row[10].upper()
                iCond = unidecode(row[11]).upper()

                #################################################################
                ##                          START                              ##
                #################################################################

                bEcrire=0
                iSpec = 0  #identification du cas ou le conditionnement est dans une autre colonne

                if "BORDEAUX" in Appellation:
                    bEcrire=0
                    iRegion="BORDEAUX"
                elif "VIGNOBLE DE LA LOIRE" in Appellation:
                    bEcrire=0
                    iRegion="LOIRE"
                elif "VIGNOBLE DU RHONE" in Appellation:
                    bEcrire=0
                    iRegion="RHONE"
                elif "VIGNOBLE DU LANGUEDOC" in Appellation:
                    bEcrire=0
                    iRegion="LANGUEDOC"
                elif iPrix =='' or 'PRIX' in iPrix :
                    bEcrire=0
                    iRegion=""
                else:
                    bEcrire=1
                    if iRegion=="BORDEAUX":
                        if 'BLANC' in Appellation:
                            chateau=Vin+' BLANC'
                        else:
                            chateau=Vin
                    elif iRegion=="LOIRE" or "RHONE" :
                        if 'BLANC' in Appellation:
                            chateau=Vin+' '+Class+' BLANC'
                        else:
                            chateau=Vin+' '+Class
                    else:
                        if 'BLANC' in Appellation:
                            chateau=Vin+' BLANC'
                        else:
                            chateau=Vin

                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.strip()
                    chateau = chateau.upper()

                    for f in dFaux_amis :
                        if f in chateau :
                            chateau = chateau+' '+Appellation

                    # annee, si vins non millesimé on prend l'année systeme
                    if Millesime=='NV':
                        annee='NV'
                    else:
                        annee=Millesime

                    # Format de bouteille
                    if Format_bouteille == '0,375':
                        formatb = 'DE'
                    elif Format_bouteille == '0,75':
                        formatb = 'BO'
                    elif Format_bouteille == '1,5':
                        formatb = 'MG'
                    elif Format_bouteille == '3':
                        formatb = 'DM'
                    elif Format_bouteille == '5':
                        formatb = 'JE'
                    elif Format_bouteille == '6':
                        formatb = 'IM'
                    elif Format_bouteille == '9':
                        formatb = 'SA'
                    elif Format_bouteille == '12':
                        formatb = 'BA'
                    elif Format_bouteille == '15':
                        formatb = 'NA'
                    elif Format_bouteille == '18':
                        formatb = 'ME'
                    elif Format_bouteille == '27':
                        formatb = 'BABY'
                    else:
                        formatb=Format_bouteille

                    prix=iPrix
                    prix=prix.replace(" ","")
                    prix=prix.replace("EUR","")

                    #quantite
                    quantite=Qte

                    #conditionnement
                    cond_finder = re.findall('[CU][BAN][0-9I][ 0-9]?[AN]?[ T]?[P]?[L]?[A]?[T]?',iCond)[0]
                    if cond_finder :
                        conditionnement = cond_finder
                        conditionnement = conditionnement.replace('CB','CBO')
                        conditionnement = conditionnement.replace('CA','CC')
                        conditionnement = conditionnement.replace(' A PLAT','PLA')
                        conditionnement = conditionnement.replace('UNIT','UNITE')
                    else:
                        conditionnement = 'UNITE'

                    #Commentaire
                    commentaire = Regie

                #écriture de la ligne
                if bEcrire==1 :
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
