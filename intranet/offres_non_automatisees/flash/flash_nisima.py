import csv
import xlrd
import glob
import re
from unidecode import unidecode
import time
# coding: utf-8

dCond = ["CBO12","CBO6","CBO3","CBO4","CBO2","CBO1","CBO24DE","CC12","CC6","CC4","CC3","CC2","CC1","CBN12","CBN6","CBN4","CBN3","CBN2","CBN1","COLLEC","GIB1"]
dBO = ["blle","Blle","blles","Blles","btle","Btles","btles","BO","bouteilles","Bouteilles"]
dMG = ["magnum","magnums","Magnum","Magnums"]
dDM = ["double-magnum","double-magnums","double","Double"]
dJE = ["jeroboam","Jeroboam","jeroboams",'Jeroboams']
dIM = ["imperial","imperiale","Imperial","Imperiale"]
dSA = ["salmanazar","Salmanazar"]

for filename in glob.glob('flash_offer.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='flash_nisima.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')


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
                elif 'virus' in row[0]:
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
                    elif 'ndeg ' in Offre :
                        bEcrire=0
                    elif 'Mis en bouteille' in Offre :
                        bEcrire=0
                    elif 'caisse Bordeaux Collection' in Offre :
                        bEcrire = 0
                    elif ' euro' not in Offre :
                        bEcrire = 0
                    else:
                        #bEcrire=1
                        Offre=Offre.replace("\\n","")
                        if 'facturation' not in Offre and '=' not in Offre and 'Dégorgé' not in Offre:
                            # On prepare la chaine Offre pour nettoyer
                            Offre=Offre.replace("carton de ","CC")
                            Offre=Offre.replace("cartons de ","CC")
                            Offre=Offre.replace("carton dorigine de ","CC")
                            Offre=Offre.replace("cartons dorigines de ","CC")
                            Offre=Offre.replace("cartons d'origines de ","CC")
                            Offre=Offre.replace("carton d'origine de ","CC")
                            Offre=Offre.replace("cbo de ","CBO")
                            Offre=Offre.replace("cbo avec ","CBO")
                            Offre=Offre.replace("caisse neutre de ","CBN")
                            Offre=Offre.replace("caisse bois neutre de ","CBN")
                            Offre=Offre.replace("caisses neutre de ","CBN")
                            Offre=Offre.replace("caisse de ","CBO")
                            Offre=Offre.replace("coffrets de ","GIB")
                            Offre=Offre.replace("coffret de ","GIB")
                            Offre=Offre.replace("coffrets bois de ","GIB")
                            Offre=Offre.replace("coffret Bois de ","CC")
                            Offre=Offre.replace("coffret bois de ","CC")
                            Offre=Offre.replace("coffrets Bois de ","CC")
                            Offre=Offre.replace("coffrets bois de ","CC")



                            # **** Recherche du conditionnement ****
                            if 'caisse Bordeaux Collection' in Offre :
                                rCond = 'COLLEC'
                            else:
                                rCond = re.findall('[ ][CG][IBC][BON0-9]+',Offre)[0]
                                rCond = rCond.strip()

                            if rCond in dCond :
                                Cond = rCond
                                Cond = Cond.replace("GIB1","GIBO1")
                                Commentaire = ""
                            else:
                                Cond = "UNITE"
                                Commentaire = rCond

                            # **** Découpage de la chaine Offre pour séparer le prix (pOffre) et le reste (cOffre) ****
                            Offre = Offre.split(' a ')
                            pOffre = Offre[1]
                            cOffre = Offre[0]

                            # **** Recherche du prix dans la chaine pOffre ****
                            Prix = pOffre.split()[0]

                            # **** Recherche du Millesime ****
                            if ' NM ' in cOffre :
                                Millesime = 'NV'
                            else:
                                Millesime=re.findall('[0-9][0-9][0-9][0-9]',cOffre)[0]

                            # **** Découpage de la chaine cOffre pour extraire formats bouteilles, quantités et nom du Vin ****
                            cOffre=cOffre.replace("'","")
                            cOffre=cOffre.replace('"','')
                            cOffre = cOffre.split()

                            # **** Recherche du format dans la chaine fOffre ****
                            if cOffre[2] in dCond :
                                fOffre = cOffre[3]
                            else:
                                fOffre = cOffre[2]

                            if fOffre in dBO :
                                formatb = "BO"
                            elif fOffre in dMG :
                                formatb = "MG"
                            elif fOffre in dDM :
                                formatb = "DM"
                            elif fOffre in dJE :
                                formatb = "JE"
                            elif fOffre in dIM :
                                formatb = "IM"
                            elif fOffre in dSA :
                                formatb = "SA"
                            else:
                                formatb = "ERREUR"

                            # **** Recherche de la quantite la liste cOffre ****
                            csQte = int(cOffre[0])
                            if Cond == 'UNITE' :
                              uQte = re.findall('[1-9]+',rCond)[0]
                            elif Cond == 'COLLEC' :
                              uQte = 1
                            else:
                              uQte = re.findall('[1-9]+',Cond)[0]
                            Qte = csQte * int(uQte)

                            # **** Recherche du nom du Vin ******
                            vOffre = Offre[0]
                            if formatb=="DM":
                                vOffre=vOffre.replace('double magnum','DM')
                                vOffre=vOffre.replace('doubles magnums','DM')

                            if 'Domaine' in vOffre or 'Maison' in vOffre and 'Chateau' not in vOffre:
                                dOffre = vOffre.split(Millesime)[1]
                                isVin = re.findall('[ ][d e]+',vOffre)[0]
                                sVin = int(vOffre.find(isVin))
                                eVin = int(vOffre.find(Millesime))
                                nVin = vOffre[sVin:eVin]
                                nVin = nVin[3:-1]
                                nVin = nVin.strip()
                                Vin = dOffre+' '+nVin
                                Vin = Vin.strip()
                            elif 'Champagne' in vOffre and 'Chateau' not in vOffre:
                                dOffre = vOffre.split(Millesime)[1]
                                isVin = re.findall('[ ][d e]+',vOffre)[0]
                                sVin = int(vOffre.find(isVin))
                                eVin = int(vOffre.find(Millesime))
                                nVin = vOffre[sVin:eVin]
                                nVin = nVin[3:-1]
                                nVin = nVin.strip()
                                Vin = nVin+' '+dOffre
                                Vin = Vin.strip()
                            else:
                                isVin = re.findall('[ ][d e]+',vOffre)[0]
                                sVin = int(vOffre.find(isVin))
                                eVin = int(vOffre.find(Millesime))
                                Vin = vOffre[sVin:eVin]
                                Vin = Vin[3:-1]
                                Vin = Vin.strip()


                            bEcrire=1
                        else:
                            bEcrire = 0

                # **** On construit la ligne ****
                if bEcrire==1:
                    trou=''
                    #newRow = [pOffre,cOffre]
                    newRow=[Vin,Millesime,formatb,Prix,Qte,Cond,Commentaire]
                    writer.writerow(newRow)

            monFichierEntre.close()
