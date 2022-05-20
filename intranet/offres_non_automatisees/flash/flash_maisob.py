import csv
import xlrd
import glob
import re
from unidecode import unidecode
import time
# coding: utf-8

dCond = ["CBO12","CBO6","CBO3","CBO4","CBO2","CBO1","CBO24DE","CC12","CC6","CC4","CC3","CC2","CC1","CBN12","CBN6","CBN4","CBN3","CBN2","CBN1"]
dBO = ["blle","Blle","blles","Blles","btle","Btles","btles","BO","bouteilles","Bouteilles"]
dMG = ["magnum","magnums","Magnum","Magnums"]
dDM = ["double-magnum","double-magnums","double","Double"]
dJE = ["jeroboam","Jeroboam","jeroboams",'Jeroboams']
dIM = ["imperial","imperiale","Imperial","Imperiale"]

dVin = ["CHATEAU","DOMAINE","MAISON"]

dApp = ["Saint Emilion","Pauillac","Saint Julien","Haut Medoc","Margaux","Pessac Leognan","Listrac Médoc","Saint Estephe","Pomerol","Côtes de Bourg","Medoc","Moulis en Medoc","Moulis en Medoc","Côtes de Castillon","Castillon","Sauternes","Graves","Lalande de Pomerol","Fronsac","Bordeaux Cotes de Francs","Bordeaux","Sainte Foy Bordeaux"]

for filename in glob.glob('flash_offer.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='flash_maisob.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')


            for row in reader:
                #on élimine les lignes qui ne servent à rien
                bEcrire=0
                if 'Bonjour' in row[0]:
                    iOffre=-1
                elif 'proposons' in row[0]:
                    iOffre=-1
                elif row[0]=='':
                    iOffre=-1
                elif 'Photos' in row[0]:
                    iOffre=-1
                elif 'Offre sauf vente' in row[0]:
                    iOffre=-1
                elif 'Prix en euros' in row[0]:
                    iOffre=-1
                elif 'Départ Bordeaux' in row[0]:
                    iOffre=-1
                elif '—' in row[0]:
                    iOffre=-1
                elif 'Clément Brillaud' in row[0]:
                    iOffre=-1
                elif '06 29 46 13 29' in row[0]:
                    iOffre=-1
                elif 'MAISON B' in row[0]:
                    iOffre=-1
                elif '96 Cours du Médoc' in row[0]:
                    iOffre=-1
                elif '33300 Bordeaux' in row[0]:
                    iOffre=-1
                elif '05 47 47 74 73' in row[0]:
                    iOffre=-1
                elif 'www.maison-b.com' in row[0]:
                    iOffre=-1
                else:
                    Offre=repr(row[0])
                    Offre = unidecode(Offre)
                    bOffre = Offre[0:1]
                    lOffre = len(Offre)
                    eOffre = Offre[lOffre-1]
                    if bOffre == "'" and eOffre=="'":
                        Offre = Offre[1:-1]

                    Offre=Offre.strip()

                    Ignore = re.findall("[\\\\][n]?",Offre)[0]
                    if Offre == Ignore or Offre == Ignore+Ignore :
                        bEcrire=0
                    elif Offre=='\\ufeff"':
                        bEcrire=0
                    else:
                        Offre=Offre.replace('\\n','')
                        iVin = Offre.split()[0]
                        iApp = Offre.split('-')[0]
                        if iVin in dVin:
                            iOffre = 1
                        elif iApp in dApp:
                            iOffre = 2
                        else:
                            iOffre = 3
                        bEcrire=1


                # **** On construit la ligne ****
                if bEcrire==1:
                    trou=''
                    #newRow = [Offre]
                    newRow=[Offre,iOffre,iApp]
                    writer.writerow(newRow)

            monFichierEntre.close()
