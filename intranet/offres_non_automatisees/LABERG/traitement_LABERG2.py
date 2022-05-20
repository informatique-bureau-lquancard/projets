import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_LABERG2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

            iRegion = 0

            for row in reader:
                if row[0]=='Bordeaux Rouge':
                    iRegion = 1
                    chateau = unidecode(row[1])
                elif row[0]=='Bordeaux Blanc':
                    iRegion = 2
                    chateau = unidecode(row[1])+' blanc'
                elif 'Bourgogne' in row[0]:
                    iRegion = 3
                    chateau = unidecode(row[2])+' '+unidecode(row[1])
                elif 'Champagne' in row[0]:
                    iRegion = 4
                    chateau = 'Champagne '+unidecode(row[2])+' '+unidecode(row[1])
                elif 'Rhône' in row[0]:
                    iRegion = 5
                    chateau = unidecode(row[2])+' '+unidecode(row[1])+' '+unidecode(row[3])
                else:
                    chateau = unidecode(row[2])+' '+unidecode(row[1])

                chateau = chateau.upper()
                # année
                iAnnee=row[4].upper()
                if iAnnee == 'NV' or iAnnee =='' :
                    annnee = '0'
                else:
                    annee = iAnnee

                # Format de la bouteille et conditionnement
                Iform = row[5].replace(' cl','')
                if Iform=='75' or Iform=='70':
                    formatb='BO'
                elif Iform=='150':
                    formatb='MG'
                elif Iform=='300':
                    formatb='DM'
                elif Iform=='450':
                    formatb='RE'
                elif Iform=='500':
                    formatb='JE'
                elif Iform=='600':
                    formatb='IM'
                elif Iform=='37,5' or Iform=='37.5':
                    formatb='DE'
                elif Iform=='50':
                    formatb='CL'
                else:
                    formatb=row[5]

                # Prix
                prix=unidecode(row[7])
                prix = prix.replace(' EUR','')
                prix = prix.replace(' ','')

                # quantite
                quantite=row[6]

                #conditionnement:
                iCond = row[8].upper()
                if iCond == '':
                    iCond = 'UNITE'
                else:
                    iCond = iCond.replace('CTO','CC')
                    iCond = iCond.replace('VC','CC')
                    iCond = iCond.replace('/','')

                RecCond = iCond

                Cond_cleaner = re.findall('[CU][CBN][0-9ONI][0-9T]?[0-9E]?[D]?[E]?',RecCond)

                if Cond_cleaner :
                    conditionnement = Cond_cleaner[0]
                    if formatb == 'DE':
                        conditionnement = re.sub('[D]$','DE',conditionnement)
                    else:
                        conditionnement = re.sub('[D]$','',conditionnement)
                else:
                    conditionnement = iCond

                iComCond = int(len(conditionnement))
                ComCond = iCond[iComCond:]

                #Commentaires

                if 'ASSORTIMENT' in chateau or 'ASSORTMENT' in chateau :
                    # On met dans commentaire le détail des caisses assortiments, cette info est présente dans la chaine chateau.
                    i = int(chateau.find(':'))
                    iNumCol = re.findall('\d+',chateau[:i])
                    if iNumCol :
                        iCom = int(chateau.find(iNumCol[0]))
                    else:
                        iCom = i

                    if ComCond!='':
                        commentaire = row[9]+' - '+chateau[iCom:]+' - '+ComCond
                    else:
                        commentaire = row[9]+' - '+chateau[iCom:]

                    chateau = chateau.replace(chateau[iCom:],'')
                    formatb = 'BO'
                    conditionnement = 'COLLEC'

                else:
                    if ComCond!='':
                        commentaire = row[9]+' - '+ComCond
                    else:
                        commentaire = row[9]

                # On fabrique la nouvelle ligne dans l'ordre voulu
                chateau = chateau.replace('"','')

                chateau = chateau.replace(commentaire,'')
                trou=''
                newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire]
                writer.writerow(newRow)
    monFichierEntre.close()
