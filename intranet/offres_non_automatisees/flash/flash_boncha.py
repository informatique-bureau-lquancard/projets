import csv
import xlrd
import glob
import re
from unidecode import unidecode
import time
# coding: utf-8

for filename in glob.glob('flash_offer.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='flash_boncha.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')

            iOffre = 0
            trou = 0
            iCond = 0
            iCom = 0
            dCom = {}


            for row in reader:
                #on élimine les lignes qui ne servent à rien
                bEcrire=0
                if 'I can offer:' in row[0]:
                    iOffre=-1
                elif 'Subject to final' in row[0]:
                    iOffre=-1
                elif 'Best regards' in row[0]:
                    iOffre=-1
                elif row[0]=='Jean':
                    iOffre=-1
                elif 'Bonneval' in row[0]:
                    iOffre=-1
                elif 'Les Verreries' in row[0]:
                    iOffre=-1
                elif 'BOUIN' in row[0]:
                    iOffre=-1
                elif 'Tel: ' in row[0]:
                    iOffre=-1
                elif 'Mob: ' in row[0]:
                    iOffre=-1
                elif 'jean@bonchateau.com' in row[0]:
                    iOffre=-1
                elif 'www.bonchateau.com' in row[0]:
                    iOffre=-1
                else:
                    Offre=repr(row[0])
                    Offre=unidecode(Offre)
                    Offre=Offre.replace("'\\n","")
                    if Offre=="'":
                        bEcrire=0
                    elif 'EUR ' not in Offre:
                        bEcrire=0
                        Offre = Offre.replace("'","")
                        Domaine = Offre
                    elif '@' in Offre:
                        bEcrire=1
                        Offre=re.split('@',Offre)
                        nOffre=Offre[0]
                        #nOffre = nOffre.replace("'","")
                        pOffre=Offre[1]
                        pOffre = pOffre.replace("'","")

                        eQte = nOffre.find(' ')
                        Qte = nOffre[:int(eQte)]

                        if 'btle ' in nOffre or 'btles ' in nOffre :
                            nOffre = nOffre.replace(Qte+' btle ','')
                            nOffre = nOffre.replace(Qte+' btles ','')
                            formatb ='BO'
                        elif 'mag ' in nOffre or 'mags ' in nOffre :
                            nOffre = nOffre.replace(Qte+' mag ','')
                            nOffre = nOffre.replace(Qte+' mags ','')
                            formatb = 'MG'
                        elif 'Mag ' in nOffre or 'Mags ' in nOffre :
                            nOffre = nOffre.replace(Qte+' mag ','')
                            nOffre = nOffre.replace(Qte+' mags ','')
                            formatb = 'MG'

                        if ' 19' and ' 20' not in nOffre :
                            Millesime = 'NV'
                        else:
                            Millesime = re.findall('[0-9][0-9][0-9][0-9]',nOffre)[0]

                        endCru = nOffre.find(' '+Millesime)
                        iCru = nOffre[:int(endCru)]

                        Vin = Domaine+' '+iCru

                        endPrix = pOffre.find('EUR ')
                        Prix = pOffre[:int(endPrix)]
                        Prix = Prix.replace(" ","")
                        Prix = Prix.replace(".",",")


                        pOffre = pOffre.split('EUR ')
                        cOffre = pOffre[1]
                        cOffre = cOffre.strip()
                        if 'OC' in cOffre :
                            sCond = cOffre.find('OC')
                            if ' ' in cOffre :
                                eCond = cOffre.find(' ')
                                Cond = cOffre[int(sCond):int(eCond)]
                            else:
                                Cond = cOffre[int(sCond):]

                            Cond = Cond.replace('OC','CC')

                        elif 'OWC' in cOffre :
                            sCond = cOffre.find('OWC')
                            if ' ' in cOffre :
                                eCond = cOffre.find(' ')
                                Cond = cOffre[int(sCond):int(eCond)]
                            else:
                                Cond = cOffre[int(sCond):]

                            Cond = Cond.replace('OWC','CBO')

                        else:
                            Cond = 'UNITE'

                        commentaire = cOffre

                    elif 'cl ' in Offre:
                        bEcrire=0   #Deuxieme type d'offre flash à gérer....(il faudra spliter différemment)



                    # **** On construit la ligne ****
                    if bEcrire==1:
                        trou=''
                        newRow=[Vin,Millesime,formatb,Prix,Qte,Cond,commentaire]
                        writer.writerow(newRow)

            monFichierEntre.close()
