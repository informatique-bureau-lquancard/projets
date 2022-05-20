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
        nom_sortie='flash_adex.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')

            iCond = 0
            Offre='test'

            # Parcours du fichier flash_offer.csv
            # on défini les lignes qui nous interressent
            # iOffre = -1 pour les lignes ou l'on ne fait rien.
            for row in reader:
                bEcrire=0
                if 'Bonjour' in row[0]:
                    iOffre=-1
                elif 'proposons' in row[0]:
                    iOffre=-1
                elif row[0]=='':
                    iOffre=-1
                elif 'Cordialement' in row[0]:
                    iOffre=-1
                elif 'Cordialement' in row[0]:
                    iOffre=-1
                elif 'ADEX' in row[0]:
                    iOffre=-1
                elif 'RAMEL' in row[0]:
                    iOffre=-1
                elif '06 14 48 75 73' in row[0] or '06 18 51 82 92' in row[0]:
                    iOffre=-1
                elif 'Guillaume BOUR' in row[0]:
                    iOffre=-1
                elif '@adexwine.com' in row[0]:
                    iOffre=-1
                else:
                    # Stockage des lignes à traiter dans la variable Offre et nettoyage de la chaine
                    iOffre=2
                    if '@' in row[0]:
                        bEcrire=1
                        Offre=repr(row[0])
                        Offre=unidecode(Offre)

                    # Exclusion des lignes vides (retour chariot \n)

                        Offre=Offre.replace("\\n","")
                        Offre=Offre.replace("'","")
                        # Offre=Offre.replace("owc","CBO")
                        # Offre=Offre.replace("cc","CC")  # Valeur a remplacer quand offre flash autre que owc.... (je me comprend)

                        # Savepoint de l'offre clean
                        altOffre=Offre

                        Offre=re.split('@',Offre)
                        nOffre=Offre[0]
                        pOffre=Offre[1]

                        # On détermine le format de bouteille
                        if ' 150 cl ' in nOffre:
                            formatb='MG'
                            nOffre=nOffre.replace(' 150 cl','')
                        elif ' 300 cl ' in nOffre:
                            formatb='DM'
                            nOffre=nOffre.replace(' 300 cl','')
                        elif ' 450 cl ' in nOffre:
                            formatb='RE'
                            nOffre=nOffre.replace(' 450 cl','')
                        elif ' 500 cl ' in nOffre:
                            formatb='JE'
                            nOffre=nOffre.replace(' 500 cl','')
                        elif ' 600 cl ' in nOffre:
                            formatb='IM'
                            nOffre=nOffre.replace(' 600 cl','')
                        elif ' 900 cl ' in nOffre:
                            formatb="SA"
                            nOffre=nOffre.replace(' 900 cl','')
                        elif ' 1200 cl ' in nOffre:
                            formatb="BA"
                            nOffre=nOffre.replace(' 1200 cl','')
                        elif ' 1500 cl ' in nOffre:
                            formatb='NA'
                            nOffre=nOffre.replace(' 1500 cl','')
                        elif ' 1800 cl ' in nOffre:
                            formatb='ME'
                            nOffre=nOffre.replace(' 1800 cl','')
                        elif ' 2700 cl ' in nOffre:
                            formatb='BABY'
                            nOffre=nOffre.replace(' 2700 cl','')
                        elif ' 0,375 cl ' in nOffre:
                            formatb='DE'
                            nOffre=nOffre.replace(' 0,375 cl','')
                        else:
                            formatb='BO'
                            nOffre=nOffre.replace(' 75 cl','')

                        # Mise à jour de Offre
                        #Offre=Offre.replace(formatb,"")

                        if 'owc' in nOffre:
                            fCond=nOffre.find('owc')
                            Cond=nOffre[int(fCond):]
                            eCond=Cond.find(' ')
                            Cond=Cond[:int(eCond)]
                        elif 'CC' in nOffre:
                            fCond=nOffre.find('CC')
                            Cond=nOffre[int(fCond):]
                            eCond=Cond.find(' ')
                            Cond=Cond[:int(eCond)]
                        else:
                            Cond=""


                        # Mise à jour Offre
                        nOffre=nOffre.replace(Cond,"")
                        conditionnement=Cond.replace('owc','CBO')

                        #Recherche du prix dans Offre
                        Prix=pOffre
                        #Prix=pOffre[SPrix:]
                        #Prix=Prix.replace('@','')
                        Prix=Prix.strip()
                        Prix=Prix.replace(' ','')

                        #Offre=Offre.replace(Prix,'')

                        #On Cherche le Millesime dans Offre
                        Millesime=re.findall('[0-9][0-9][0-9][0-9]',nOffre)
                        Millesime=str(Millesime)
                        Millesime=Millesime.replace('[\'','')
                        Millesime=Millesime.replace('\']','')

                        # **** On cherche à isoler le nom du vin ****

                        if 'Domaine' in nOffre :
                            #On cherche le nom du domaine (hors bordeaux)
                            startDomaine=nOffre.find('Domaine')
                            endDomaine=nOffre.find(' @ ')
                            Domaine=nOffre[int(startDomaine):int(endDomaine)]

                            #On actualise Offre
                            nOffre=nOffre.replace(Domaine,'')



                            #On extrait le nom du vin
                            startVin=Offre.find(' ')
                            endVin=Offre.find(Millesime)
                            iVin=Offre[int(startVin):int(endVin)]
                            Vin = Domaine+' '+iVin


                        else :
                            # On recherche le nom du chateau (Bordeaux)
                            sVin=nOffre.find(' ')
                            eVin=nOffre.find(Millesime)
                            iVin=nOffre[int(sVin):int(eVin)]
                            iVin=iVin[2:]
                            #Offre=Offre.replace(iVin,'')

                            #Resultat trouvé
                            Vin=iVin.strip()

                        #Quantités
                        EQte=nOffre.find(' ')
                        csQte=nOffre[:int(EQte)]
                        uCond=re.findall('\d+',Cond)[0]
                        Qte = int(csQte) * int(uCond)

                # **** On construit la ligne ****
                if bEcrire==1:
                    newRow=[Vin,Millesime,formatb,Prix,Qte,conditionnement]
                    # newRow=[Offre,Cond,Vin,Millesime,Qte,altOffre,uCond,Prix,formatb]
                    writer.writerow(newRow)

            monFichierEntre.close()
