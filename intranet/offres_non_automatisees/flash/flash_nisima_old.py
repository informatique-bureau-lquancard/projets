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
        nom_sortie='flash_nisima.csv'
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
                if 'Bonjour' in row[0]:
                    iOffre=-1
                elif 'propose' in row[0]:
                    iOffre=-1
                elif row[0]=='':
                    iOffre=-1
                elif 'Prix hors taxes' in row[0]:
                    iOffre=-1
                elif 'Cordialement' in row[0]:
                    iOffre=-1
                elif 'Frédéric Villemiane' in row[0]:
                    iOffre=-1
                elif 'Nisima' in row[0]:
                    iOffre=-1
                elif 'Eugene Dandicol' in row[0]:
                    iOffre=-1
                elif '33600 Pessac' in row[0]:
                    iOffre=-1
                elif 'Port : ' in row[0]:
                    iOffre=-1
                elif 'fredisaville@gmail.com' in row[0]:
                    iOffre=-1
                #### On essaye d'identifier les lignes de commentaire ###
                #elif 'blle' in row[0] and 'caisse' not in row[0]:
                    #iOffre=3
                else:
                    if 'cbo' in row[0] or 'carton' in row[0] or 'cartons' in row[0] or 'caisse' in row[0] or 'caisses' in row[0] or 'blle' in row[0]:
                        Offre=repr(row[0])
                        Offre=unidecode(Offre)
                        if Offre=="'\\n'":
                            bEcrire=0
                        elif 'ndeg ' in Offre:
                            bEcrire=0
                        elif ', ' in Offre or 'authentifiees' in Offre or 'capsulees' in Offre or 're etiquetees' in Offre:
                            bEcrire=0
                        #elif iOffre==3:
                            #VarCom=row[0]
                            #bEcrire=1
                        else:
                            VarCom='no comment'
                            #bEcrire=1

                            Offre=Offre.replace("\\n","")
                            #Offre=Offre.replace("'","")

                            # Savepoint de l'offre clean, ça peut servir plus tard pour calculer la quantite
                            altOffre=Offre
                            #if 'blle' in Offre and 'caisse' not in Offre :
                                #bEcrire=0
                                #while iCom < 6 :
                                    #dCom[iCom]=row[0]
                                    #iCom += 1


                            # On prepare la chaine Offre pour nettoyer
                            Offre=Offre.replace("carton de ","CC")
                            Offre=Offre.replace("cartons de ","CC")
                            Offre=Offre.replace("cbo de ","CBO")
                            Offre=Offre.replace("cbo avec ","CBO")
                            Offre=Offre.replace("caisse neutre de ","CBN")
                            Offre=Offre.replace("caisses neutre de ","CBN")
                            Offre=Offre.replace("caisse de ","CBO")

                            #RECHERCHE DU CONDITONNEMENT
                            if 'CBO12' in Offre:
                                Cond='CBO12'
                                rCond=Cond
                            elif 'CBO6' in Offre:
                                Cond='CBO6'
                                rCond=Cond
                            elif 'CBO3' in Offre:
                                Cond='CBO3'
                                rCond=Cond
                            elif 'CBO4' in Offre:
                                Cond='CBO4'
                                rCond=Cond
                            elif 'CC1 ' in Offre:
                                Cond='CC1'
                                rCond=Cond
                            elif 'CC2 ' in Offre:
                                Cond='CC2'
                                rCond=Cond
                            elif 'CC3 ' in Offre:
                                Cond='CC3'
                                rCond=Cond
                            elif 'CC4 ' in Offre:
                                Cond='CC4'
                                rCond=Cond
                            elif 'CC5 ' in Offre:
                                Cond='UNITE'
                                rCond='CC5'
                            elif 'CC6' in Offre:
                                Cond='CC6'
                                rCond=Cond
                            elif 'CC12' in Offre:
                                Cond='CC12'
                                rCond=Cond
                            elif 'CC7' in Offre :
                                Cond='UNITE'
                                rCond='CC7'
                            elif 'CC8' in Offre:
                                Cond='UNITE'
                                rCond='CC8'
                            elif 'CC9' in Offre:
                                Cond='UNITE'
                                rCond='CC9'
                            elif 'CC10' in Offre:
                                Cond='UNITE'
                                rCond='CC10'
                            elif 'CC11' in Offre:
                                Cond='UNITE'
                                rCond='CC11'
                            elif 'CBO1 ' in Offre:
                                Cond='CBO1'
                                rCond=Cond
                            elif 'CBO2 ' in Offre:
                                Cond='CBO2'
                                rCond=Cond
                            elif 'CBO5' in Offre:
                                Cond='UNITE'
                                rCond='CBO5'
                            elif 'CBO7' in Offre:
                                Cond='UNITE'
                                rCond='CBO7'
                            elif 'CBO8' in Offre:
                                Cond='UNITE'
                                rCond='CBO8'
                            elif 'CBO9' in Offre:
                                Cond='UNITE'
                                rCond='CBO9'
                            elif 'CBO10' in Offre:
                                Cond='UNITE'
                                rCond='CBO10'
                            elif 'CBO11' in Offre:
                                Cond='UNITE'
                                rCond='CBO11'
                            elif 'CBO24' in Offre:
                                Cond='CBO24DE'
                                rCond='CBO24'
                            elif 'CBN1 ' in Offre:
                                Cond='CBN1'
                                rCond='CBN1'
                            elif 'CBN2 ' in Offre:
                                Cond='CBN2'
                                rCond='CBN2'
                            elif 'CBN3 ' in Offre:
                                Cond='CBN3'
                                rCond='CBN3'
                            elif 'CBN4' in Offre:
                                Cond='CBN4'
                                rCond='CBN4'
                            elif 'CBN5' in Offre:
                                Cond='CBN'
                                rCond='CBN5'
                            elif 'CBN6' in Offre:
                                Cond='CBN6'
                                rCond='CBN6'
                            elif 'CBN7' in Offre:
                                Cond='CBN'
                                rCond='CBN7'
                            elif 'CBN8' in Offre:
                                Cond='CBN'
                                rCond='CBN8'
                            elif 'CBN9' in Offre:
                                Cond='CBN'
                                rCond='CBN9'
                            elif 'CBN10' in Offre:
                                Cond='CBN'
                                rCond='CBN10'
                            elif 'CBN11' in Offre:
                                Cond='CBN'
                                rCond='CBN11'
                            elif 'CBN12' in Offre:
                                Cond='CBN12'
                                rCond='CBN12'
                            elif 'assortiment' in Offre:
                                Cond='COLLEC'
                                rCond='COLLEC'
                            else:
                                Cond='UNITE'
                                rCond='UNITE'

                            Offre=Offre.replace(str(rCond)+' blles de ','')
                            Offre=Offre.replace(str(rCond)+' blle de ','')
                            Offre=Offre.replace(str(rCond)+' blles ','')
                            Offre=Offre.replace(str(rCond)+' blle','')
                            Offre=Offre.replace(str(rCond)+' double magnum de ','')
                            Offre=Offre.replace(str(rCond)+' magnum de ','')
                            Offre=Offre.replace(str(rCond)+' magnums de ','')
                            Offre=Offre.replace(str(rCond)+' jéroboam de ','')
                            Offre=Offre.replace(str(rCond)+' impériale','')
                            Offre=Offre.replace(str(rCond)+' impérial','')

                            # **** Recherche du prix dans la chaine Offre ****

                            sPrix=Offre.find(' a ')
                            ePrix=Offre.find(' euro')
                            Prix=Offre[int(sPrix):int(ePrix)]
                            Prix=Prix[3:]

                            #Mise à jour de la chaine Offre pour exclure le prix avant la recherche du Millesime.
                            Offre = Offre.replace(Prix,'')

                            # **** Recherche du Millesime ****
                            Millesime=re.findall('[0-9][0-9][0-9][0-9]',Offre)
                            Millesime=str(Millesime)
                            Millesime=Millesime.replace('[\'','')
                            Millesime=Millesime.replace('\']','')

                            # **** On cherche à isoler le nom du vin ****

                            if 'Domaine' in row[0] and 'assortiment' not in row[0]:
                                #On cherche le nom du domaine
                                startDomaine=Offre.find('Domaine')
                                endDomaine=Offre.find(' a ')
                                Domaine=Offre[int(startDomaine):int(endDomaine)]

                                #On extrait le nom du vin
                                startVin=Offre.find(' ')
                                endVin=Offre.find(Millesime)
                                iVin=Offre[int(startVin):int(endVin)]

                                Vin=Domaine+' '+iVin
                                bEcrire=1

                                Offre=Offre.replace(Domaine,'')

                            elif 'Domaine' in row[0] and 'assortiment' in row[0]:
                                startDomaine=Offre.find('Domaine')
                                endDomaine=Offre.find(' a ')
                                Domaine=Offre[int(startDomaine):int(endDomaine)]+' assortiment'

                                Vin=Domaine
                                bEcrire=1


                            elif 'Maison' in row[0]:
                                startMaison=Offre.find('Maison')
                                endMaison=Offre.find(' a ')
                                Maison=Offre[int(startMaison):int(endMaison)]

                                startVin=Offre.find(' ')
                                endVin=Offre.find(Millesime)
                                iVin=Offre[int(startVin):int(endVin)]

                                Vin=Maison+' '+iVin
                                bEcrire=1

                                #On actualise Offre

                                Offre=Offre.replace(Maison,'')

                            else :
                                startVin=Offre.find(' ')
                                endVin=Offre.find(Millesime)
                                iVin=Offre[int(startVin):int(endVin)]

                                Vin=iVin
                                Vin=Vin[1:]
                                bEcrire=1

                            # **** Recherche de la quantité de caisses en utilisant altOffre  car Offre ne contient plus la qte *******
                            endQteCs=altOffre.find(' ')
                            QteCs=altOffre[1:int(endQteCs)]
                            nOffre = Offre.find(' ')
                            Offre = Offre[int(nOffre):]

                            if 'CC' in rCond:
                                Ucond=rCond[2:]
                            elif 'CBO' in rCond or 'CBN' in rCond:
                                Ucond=rCond[3:]
                            elif 'UNITE' in rCond or 'COLLEC' in rCond:
                                Ucond='1'

                            # **** calcul de la quantité de bouteille ****
                            Qte=int(QteCs)*int(Ucond)

                            # **** création de la chaine format ****
                            if 'blle' in altOffre or 'blles' in altOffre :
                                formatb='BO'
                            elif 'magnum' in altOffre or 'magnums' in altOffre:
                                formatb='MG'
                            elif 'double magnum' in altOffre or 'double magnums' in altOffre:
                                formatb='DM'
                            elif 'jéroboam' in altOffre or 'jéroboams' in altOffre:
                                formatb='JE'
                            elif 'impérial' in altOffre or 'impériale' in altOffre:
                                formatb='IM'

                            if iOffre == 3 :
                                while iCom < 6 :
                                    dCom[iCom] = row[0]
                                    iCom += 1
                                    commentaire = dCom
                            else:
                                if Cond=='UNITE':
                                    commentaire='VERIF CDT - '+rCond
                                else:
                                    commentaire=""

                # **** On construit la ligne ****
                if bEcrire==1:
                    trou=''
                    newRow=[Vin,Millesime,formatb,Prix,Qte,Cond,commentaire]
                    writer.writerow(newRow)

            monFichierEntre.close()
