import csv
import glob
import re
import io
import time
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_NISIMA2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

            iRegion=0

            for row in reader:
                bEcrire=0
                if "Nombres" in row[0]:
                    iRegion=-1
                elif "BORDEAUX" in row[0]:
                    iRegion=1
                elif "BOURGOGNE" in row[0]:
                    iRegion=2
                elif "CHAMPAGNES" in row[0]:
                    iRegion=3
                elif  "RHÔNE" in row[0]:
                    iRegion=3
                elif "ALSACE" in row[0]:
                    iRegion=3
                elif "LOIRE" in row[0]:
                    iRegion=3
                elif "JURA" in row[0]:
                    iRegion=3
                elif "ETRANGERS" in row[0]:
                    iRegion=3
                elif "LANGUEDOC" in row[0]:
                    iRegion=1
                elif "ALCOOLS" in row[0]:
                    iRegion=1
                else:
                    if row[0]!="" and row[1]=="":
                        bEcrire=0
                    elif row[0]=="" and row[1]=="":
                        bEcrire=0
                    else:
                        bEcrire=1
                        if iRegion==1:
                            chateau=unidecode(row[3])
                        elif iRegion==2:
                            if "panachée" in row[4]:
                                chateau=unidecode(row[3])+' '+unidecode(row[5])+' caisse panachée'
                            else:
                                chateau=unidecode(row[3])+' '+unidecode(row[5])+' '+unidecode(row[4])
                        elif iRegion==3:
                            chateau=unidecode(row[3])+' '+unidecode(row[4])


                        #chateau=chateau.replace('Château','')
                        #chateau=chateau.replace('é','e')
                        #chateau=chateau.replace('è','e')
                        #chateau=chateau.replace('"','')


                        # année
                        if row[2]=="NV" or row[2]=="" or row[2]=="NM":
                            aTime=time.strftime('%Y')
                            annee=int(aTime)-2
                        else:
                            annee=row[2]

                        # quantite
                        quantite=row[0]

                        # conditionnement
                        Cond=row[7]
                        if "Caisse bois d'origine de " in row[7]:
                            Tcond="CBO"
                            Sncols=Cond[25:]
                            Sncols=Sncols.strip()
                            Encols=Sncols.find(" ")
                            Ncols=Sncols[:Encols]
                        elif "Carton de " in row[7]:
                            Tcond="CC"
                            Sncols=Cond[9:]
                            Sncols=Sncols.strip()
                            Encols=Sncols.find(" ")
                            Ncols=Sncols[:Encols]
                        else:
                            Tcond="UNITE"
                            Ncols=""


                        aCond=['CBO1','CC1','CBO2','CC2','CBO3','CC3','CBO4','CC4','CBO6','CC6','CBO12','CC12']
                        rCond=Tcond+Ncols
                        if rCond in aCond:
                            conditionnement=rCond
                        else:
                            conditionnement='UNITE'



                        # Format de la bouteille
                        if "75" in row[1]:
                            formatb="BO"
                        elif "150" in row[1]:
                            formatb="MG"
                        elif "300" in row[1]:
                            formatb="DM"
                        elif "37,5" in row[1]:
                            formatb="DE"
                        elif "250" in row[1]:
                            formatb="DM"
                        elif "500" in row[1]:
                            formatb="JE"
                        elif "600" in row[1]:
                            formatb="IM"
                        else:
                            formatb=row[1]


                        # Prix
                        fPrix=repr(row[8])
                        fPrix=fPrix.replace("'","")
                        fPrix=fPrix.replace("\\","")
                        fPrix=fPrix.replace("u202f","")
                        prix=unidecode(fPrix)
                        prix=prix.replace(' EUR','')

                         # Prix discount
                        dPrix=repr(row[9])
                        dPrix=dPrix.replace("'","")
                        dPrix=dPrix.replace("\\","")
                        dPrix=dPrix.replace("u202f","")
                        discount=unidecode(dPrix)
                        discount=discount.replace(' EUR','')


                        if iRegion==2 and "panachée" in row[4]:
                            commentaires=unidecode(row[4])+' - PV si rglt a fact : '+discount
                            commentaires=commentaires.replace(' caisse bois d''origine panachee comprenant :', '')
                        else:
                            commentaires='PV si rglt a fact : '+discount


                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire==1:
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires]
                    writer.writerow(newRow)
            monFichierEntre.close()
