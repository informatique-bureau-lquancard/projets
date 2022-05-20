# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_VINTEX.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:

                color = row[3].upper()

                if row[1] == '' or row[0] == 'VIN' or row[0]=='WINE':
                    bEcrire = 0
                else:
                    bEcrire = 1
                    chateau = unidecode(row[0].upper())
                    if color == 'BLANC' and 'BLANC' not in chateau :
                        chateau = chateau+' '+color


                    annee = row[1]
                    rFormatb = row[7].upper()
                    rFormatb = rFormatb.replace(' ','')

                    if rFormatb == '750ML' or rFormatb=='750':
                        formatb = 'BO'
                    elif rFormatb == '1,5L' or rFormatb == '1500ML' :
                        formatb = 'MG'
                    elif rFormatb == '3L' or rFormatb == '3,00L' :
                        formatb = 'DM'
                    elif rFormatb == '5L' :
                        formatb = 'JE'
                    elif rFormatb == '6L' or rFormatb =='6000ML':
                        formatb = 'IM'
                    elif rFormatb == '375ML' :
                        formatb = 'DE'
                    else :
                        formatb = rFormatb

                    prix = unidecode(row[4]).replace(' EUR','').replace(' ','')

                    findQte = re.findall('\d+',row[6])
                    if not(findQte):
                        uQte = 1
                    elif (findQte is not None):
                        uQte = findQte[0]

                    QteCS = row[5].replace(',','.')
                    QteCS = QteCS.strip()
                    Qte = float(QteCS)*int(uQte)
                    Qte = int(Qte)

                    findCond = re.findall('\D+',row[6])[0]
                    if findCond == 'CB':
                        Cond = 'CBO'+str(uQte)
                    elif findCond =="CRT" or findCond =="CT":
                        Cond = 'CC'+str(uQte)
                    elif findCond =="CBP" :
                        Cond = "CBO"+str(uQte)+"PLA"
                    elif findCond == "CRTP" or findCond =="CTP":
                        Cond = "CC"+str(uQte)+"PLA"
                    elif findCond == "DEMIE" or findCond =="HALF" or findCond == "MAG" or findCond =="BT" or findCond == "DMAG" or findCond ==" DMAG" or findCond =="IMP" :
                        Cond = "UNITE"

                    if Cond == 'CBO24':
                        Cond = 'CBO24DE'

                    if ' #' in chateau :
                        commentaire = 'RFSE'
                        chateau = chateau.replace(' #','')
                    else:
                        commentaire = ''


                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1:
                    chateau = chateau.strip()
                    newRow=[chateau,annee,formatb,prix,Qte,Cond,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
