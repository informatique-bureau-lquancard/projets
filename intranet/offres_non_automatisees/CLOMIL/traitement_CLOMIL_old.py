# coding: utf-8
import csv
import glob
import re
import codecs
import sys
ucodec = sys.getfilesystemencoding()




for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding=ucodec) as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_COMVIG.csv'
        with open(nom_sortie,'w',newline='', encoding=ucodec) as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                current='0'
                if row[5]=='':
                    pass
                elif row[5]==' ':
                    pass
                elif row[5]=='MOUN':
                    pass
                else :
                    # Nom du chateau
                    if row[2]=='Montrachet':
                        chateau=row[0]+' Montrachet Grand Cru'
                    elif row[2]=='Corton Charlemagne':
                        chateau=row[0]+' Corton Charlemagne Cru'
                    elif row[2]=='Corton':
                        chateau=row[0]+' Corton Cru'
                    elif row[2]=='Beaune Greves':
                        chateau=row[0]+' Beaune Greves 1er cru'
                    elif row[2]=='Meursault':
                        chateau=row[0]+' '+row[1]+' '+row[2]
                    elif row[2]=='Puligny Montrachet':
                        chateau=row[0]+' Puligny Montrachet'
                    elif row[2]=='Canon Fronsac':
                        chateau=row[0]+' Fronsac'
                    else:
                        chateau=row[0]
                    # chateau=re.sub(r'[0-9]','',chateau) ??
                    # année
                    if row[3]=='':
                        annee='2014'
                    else:
                        annee=row[3]
                    # quantite
                    quantite=row[5]
                    # Format de la bouteille
                    if row[6]=='blle':
                        formatb='BO'
                    elif row[6]=='bouteilles':
                        formatb='BO'
                    elif row[6]=='CB 9 btles':
                        formatb='BO'
                    elif row[6]=='CB 8 btles':
                        formatb='BO'
                    elif row[6]=='cinquante':
                        formatb='CL'
                    elif row[6]=='Collection des 61 Bouteilles Crus Classés du Médoc en Coffrets-Bois sur-mesures':
                        formatb='BO'
                    elif row[6]=='Magnum':
                        formatb='MG'
                    elif row[6]=='magnum':
                        formatb='MG'
                    elif row[6]=='MAGNUM':
                        formatb='MG'
                    elif row[6]=='Magnums':
                        formatb='MG'
                    elif row[6]=='MAGNUMS':
                        formatb='MG'
                    elif row[6]=='demie':
                        formatb='DE'
                    elif row[6]=='DEMIE':
                        formatb='DE'
                    elif row[6]=='Double Magnum':
                        formatb='DM'
                    elif row[6]=='DOUBLE-MAGNUM':
                        formatb='DM'
                    elif row[6]=='DOUBLE MAGNUM':
                        formatb='DM'
                    elif row[6]=='Imperiale':
                        formatb='IM'
                    elif row[6]=='IMPERIALE':
                        formatb='IM'
                    elif row[6]=='IMPERIALES':
                        formatb='IM'
                    elif row[6]=='JERO':
                        formatb='JE'
                    elif row[6]=='JEROBOAM':
                        formatb='JE'
                    elif row[6]=='Jeroboam':
                        formatb='JE'
                    elif row[6]=='jeroboam':
                        formatb='JE'
                    elif row[6]=='Jéroboam':
                        formatb='JE'
                    elif row[6]=='Mathusalem':
                        formatb='MAT'
                    else:
                        formatb=row[6]

                    # Prix
                    prix=row[4]
                    #conditionnement
                    conditionnement=row[7]
                    test=row[7]
                    #conditionnement et commentaire
                    if conditionnement=='1Petrus 1Lafite 1Latour 1Mouton 1Margaux 1Haut-Brion 1Yquem 1Cheval Blanc 1Mission Ht-Brion':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='4x Petrus 4x Latour 4x Margaux 4x Haut-Brion':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='1Petrus 1Lafite 1Mouton 1Margaux 1Haut-Brion 1Yquem 1Cheval Blanc 1Mission Ht-Brion':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='1Petrus 1Lafite 1Mouton 1Margaux 1Haut-Brion 1Ausone 1Cheval Blanc 1Mission 1Yquem':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 2000 à 2016':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 2004 à 2015':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1980 à 2015':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1983 à 1994':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1979 à 2008':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1979 à 2014':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1945 à 2015':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1985 à 2015':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1945 à 2010':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='COLLECTION 1900 à 2015':
                        conditionnement='COLLEC'
                        current='1'
                    elif conditionnement=='CBO6 CBN1':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='5 Litres CB1':
                        conditionnement='CBO1'
                        current='1'
                    elif conditionnement=='CBO6 CBO3':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='CBO6 RC2018':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='CBO6-CBO3':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='Gift-Box Duclot':
                        conditionnement='GIBO1'
                        current='1'
                    elif conditionnement=='CAO6-12':
                        conditionnement='CC12'
                        current='1'
                    elif conditionnement=='CBO6-12':
                        conditionnement='CBO12'
                        current='1'
                    elif conditionnement=='CBO6 CBO12':
                        conditionnement='CBO12'
                        current='1'
                    elif conditionnement=='CBO6 CBO1':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='CBO6-CBO1':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='CBO3-CBO2':
                        conditionnement='CBO3'
                        current='1'
                    elif conditionnement=='CBO12 CBO6':
                        conditionnement='CBO12'
                        current='1'
                    elif conditionnement=='CBO12-CBO6':
                        conditionnement='CBO12'
                        current='1'
                    elif conditionnement=='CB1':
                        conditionnement='CBO1'
                        current='1'
                    elif conditionnement=='CBO6 -CBO12':
                        conditionnement='CBO12'
                        current='1'
                    elif conditionnement=='CBO1 Gift-Box':
                        conditionnement='CBO1'
                        current='1'
                    elif conditionnement=='CBO6 CBO1Banded':
                        conditionnement='CBO6'
                        current='1'
                    elif conditionnement=='COLLECTION 1985 à 2015':
                        conditionnement='COLLEC'                        
                        current='1'
                    elif conditionnement=='CB 1 Bsourgeoisphelanphe':
                        conditionnement='CBO1'                        
                        current='1'
                    elif conditionnement=='CBO1-CBO12':
                        conditionnement='CBO12'                        
                        current='1'
                    elif conditionnement=='CBO6-CBO12':
                        conditionnement='CBO12'                        
                        current='1'
                    elif conditionnement=='CBO12-CBO6':
                        conditionnement='CBO12'                        
                        current='1'
                    elif conditionnement=='1CBO6':
                        conditionnement='CBO6'                        
                        current='1'
                    elif conditionnement=='COLLECTION 1900 à 2011':
                        conditionnement='COLLEC'                       
                        current='1'
                    elif conditionnement=='Gift-Box':
                        conditionnement='GIBO1'
                        current='1'
                    elif conditionnement=='':
                        conditionnement='UNITE'
                        current='2'
#                       if formatb=='BO':
#                            if int(quantite)<12:
#                                conditionnement='UNITE'
#                                current='2'
#                            else:
#                                conditionnement='CBO12'
#                                current='2'
#                        elif formatb=='DE':
#                            if int(quantite)<24:
#                                conditionnement='UNITE'
#                                current='2'
#                            else:
#                                conditionnement='CBO24DE'
#                                current='2'
#                        elif formatb=='MG':
#                                if int(quantite)<6:
#                                    conditionnement='UNITE'
#                                    current='2'
#                                else:
#                                   conditionnement='CBO6'
#                                   current='2'
#                        elif formatb=='DM':
#                            if int(quantite)<3:
#                               conditionnement='UNITE'
#                               current='2'
#                            else:
#                               conditionnement='CBO3'
#                               current='2'
#                        elif formatb=='JE':
#                            conditionnement='CBO1'
#                            current='2'
#                        elif formatb=='IM':
#                            conditionnement='CBO1'
#                            current='2'
                    conditionnement=conditionnement
                    conditionnement=conditionnement.replace('CO','CC')
                    conditionnement=conditionnement.replace('CCLLEC','COLLEC')
                    conditionnement=conditionnement.replace('COLLECTION 1966 à 2016','COLLEC')
                    conditionnement=conditionnement.replace('COLLECTION 1966 à 2016','COLLEC')
                    conditionnement=conditionnement.replace(' banded','')
                    conditionnement=conditionnement.replace(' Banded','')
                    conditionnement=conditionnement.replace('Banded','')
                    conditionnement=conditionnement.replace('banded','')
                    conditionnement=conditionnement.replace(' Parfait','')
                    conditionnement=conditionnement.replace('CAO','CC')
                    conditionnement=conditionnement.replace('CBO6 ','CBO6')
                    conditionnement=conditionnement.replace('CBO2 ','CBO2')
                    conditionnement=conditionnement.replace('CBO1e','CBO1')
                    conditionnement=conditionnement.replace('CBO1 ','CBO1')
                    conditionnement=conditionnement.replace('CBO1 ','CBO1')
                    conditionnement=conditionnement.replace('CBO1 ','CBO1')
                    conditionnement=conditionnement.replace('CBO1 RC','CBO1')
                    conditionnement=conditionnement.replace(' en 2018','')
                    conditionnement=conditionnement.replace(' en 2001','')
                    conditionnement=conditionnement.replace('CBO6-CBO3-CBO2','CBO6')
                    conditionnement=conditionnement.replace('CB12','CBO12')
                    conditionnement=conditionnement.replace('CBO6s','CBO6')
                    conditionnement=conditionnement.replace('LOT CBO6x5','CBO6')
                    conditionnement=conditionnement.replace('2019','')
                    conditionnement=conditionnement.replace('Coffret-Bois','GIBO1')
                    conditionnement=conditionnement.replace(' RC en 2015','')
                    conditionnement=conditionnement.replace(' x2','')
                    conditionnement=conditionnement.replace(' x 6','')
                    conditionnement=conditionnement.replace('x 6','')
                    conditionnement=conditionnement.replace('CBO6CBO3 CBO1','CBO6')
                    conditionnement=conditionnement.replace(' x 2','')
                    conditionnement=conditionnement.replace('x 2','')
                    conditionnement=conditionnement.replace('x1','')
                    conditionnement=conditionnement.replace('x 1','')
                    conditionnement=conditionnement.replace('x2','')
                    conditionnement=conditionnement.replace('x 3','')
                    conditionnement=conditionnement.replace(' collector','')
                    conditionnement=conditionnement.replace(' x 4','')
                    conditionnement=conditionnement.replace(' x3','')
                    conditionnement=conditionnement.replace(' x 3','')
                    conditionnement=conditionnement.replace(' x 1','')
                    conditionnement=conditionnement.replace(' x1','')
                    conditionnement=conditionnement.replace(' CRD','')
                    conditionnement=conditionnement.replace(' R.C.','')
                    conditionnement=conditionnement.replace(' RC1998','')
                    conditionnement=conditionnement.replace(' RC AVRIL2012 PROOFTAG','')
                    conditionnement=conditionnement.replace(' RC','')
                    conditionnement=conditionnement.replace(' cerclées','')
                    conditionnement=conditionnement.replace(' Coffret-Club','')
                    conditionnement=conditionnement.replace(' Released Château 2018','')
                    conditionnement=conditionnement.replace(' Coffret-Club','')
                    conditionnement=conditionnement.replace(' x5','')
                    conditionnement=conditionnement.replace(' RC2018','')
                    conditionnement=conditionnement.replace(' H.E.','')
                    conditionnement=conditionnement.replace(' T.L.B.','')
                    conditionnement=conditionnement.replace(' RC2019','')
                    conditionnement=conditionnement.replace(' Banded RC en 2018','')
                    conditionnement=conditionnement.replace(' x 4','')
                    conditionnement=conditionnement.replace(' Parfaits','')
                    conditionnement=conditionnement.replace(' RC 2016','')
                    conditionnement=conditionnement.replace(' RC en 2011','')
                    conditionnement=conditionnement.replace(' RC en 1999','')
                    conditionnement=conditionnement.replace(' RC en 2001','')
                    conditionnement=conditionnement.replace('RC en 2011','')
                    conditionnement=conditionnement.replace(' en 1999','')
                    onditionnement=conditionnement.replace(' en 2001','')
                    conditionnement=conditionnement.replace(' Numbered','')
                    conditionnement=conditionnement.replace('collector','')
                    conditionnement=conditionnement.replace('x 4','')
                    conditionnement=conditionnement.replace('x3','')
                    conditionnement=conditionnement.replace('cerclées','')
                    conditionnement=conditionnement.replace('Released Château 2018','')
                    conditionnement=conditionnement.replace('Coffret-Club','')
                    conditionnement=conditionnement.replace(' x 3','')
                    conditionnement=conditionnement.replace(' H.E.','')
                    conditionnement=conditionnement.replace('H.E.','')
                    conditionnement=conditionnement.replace(' T.L.B.','')
                    conditionnement=conditionnement.replace('T.L.B.','')
                    conditionnement=conditionnement.replace(' RC2019','')
                    conditionnement=conditionnement.replace('RC2019','')
                    conditionnement=conditionnement.replace('RC','')
                    conditionnement=conditionnement.replace(' RC','')
                    conditionnement=conditionnement.replace('CBO3 ','CBO3')
                    conditionnement=conditionnement.replace('CBN3 ','CBN3')
                    if current=='0':
                        if conditionnement=='CBO12':
                            current='3'
                        elif conditionnement=='CBO6':
                            current='3'
                        elif conditionnement=='UNITE':
                            current='3'
                        elif conditionnement=='CBO3':
                            current='3'
                        elif conditionnement=='CBO2':
                            current='3'
                        elif conditionnement=='CBO1':
                            current='3'
                        elif conditionnement=='CBN12':
                            current='3'
                        elif conditionnement=='CBN6':
                            current='3'
                        elif conditionnement=='CBN1':
                            current='3'
                        elif conditionnement=='CC12':
                            current='3'
                        elif conditionnement=='CC6':
                            current='3'
                        elif conditionnement=='CBO4':
                            current='3'
                        elif conditionnement=='CBO4':
                            current='3'
                        elif conditionnement=='CBN4':
                            current='3'
                        elif conditionnement=='CBN3':
                            current='3'
                        elif conditionnement=='CBN6':
                            current='3'
                        elif conditionnement=='CBN12':
                            current='3'
                        elif conditionnement=='CC1':
                            current='3'
                        elif conditionnement=='CC3':
                            current='3'
                        elif conditionnement=='GIBO1':
                            current='3'
                        elif conditionnement=='COLLEC':
                            current='3'
                            
                        
                    #commentaires
                    if current=='1':
                        commentaires=row[7]
                    elif current=='2':
                        commentaires=row[7]
                    elif current=='3':
                        commentaires=row[7]
                    elif current=='0':
                        conditionnement='UNITE'
                        commentaires=row[7]
                        
                        #elif conditionnement=='COLLEC','CBO6','CBO12','CBO1','CBO2','CBO3','CBO4','CBO24DE','CBN1','CBN2','CBN3','CBN4','CBN6','CBN12','CC1','CC2','CC3','CC4','CC6','CC12','GIBO1':
   
                        #else:
                            #current='0'
                    #if current=='0':
#                        conditionnement='TEST'
#                        +' '+row[7]
                                            
                                  
                    # Commentaire
#                   commentaires=row[8]
#                   if row[6]=='Bordeaux Not Owc':
#                      commentaire=row[6]+' - '+'Verif cdt'
#                       if row[3]=='75':
#                           formatb='BO'
#                        if int(quantite)<12:
#                           else:
#                               conditionnement='CBN12'
#                       elif row[3]=='150':
#                           formatb='MG'
#                           if int(quantite)<6:
#                            conditionnement='UNITE'
#                           else:
#                               conditionnement='CBN6'
#                       elif row[3]=='300':
#                           formatb='DM'
#                           if int(quantite)<3:
#                               conditionnement='UNITE'
#                           else:
#                               conditionnement='CBN3'
#                       else:
#                           formatb=row[3]
#                           conditionnement=''
#                   else:
#                       commentaire='Verif cdt'
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,trou,trou,trou,test,current]
                    writer.writerow(newRow)
            monFichierEntre.close()
