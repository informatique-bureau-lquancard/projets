import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_NISIMA2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                if row[0]=='':
                    pass
                elif row[0]=='Mill.':
                    pass
                else:
                    # Nom du chateau
                    if row[3]=='Champagne':
                        chateau=row[1]+' '+row[2]
                        chateau=chateau.replace('Château','')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('"','')
                        chateau=chateau.replace('ô','')
                        #chateau=re.sub(r'[0-9]','',chateau)
                        # année
                        annee=row[0]
                        # quantite et conditionnement
                        quantite=row[5]
                        if row[6]=='cb12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CBO12'
                        elif row[6]=='cb6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb 1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1 mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1d.mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1dmag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Imp':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1imperiale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Impériale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jero':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jeroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Jéroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jéroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb2':
                            quantite=str(int(quantite)*2)
                            conditionnement='CBO2'
                        elif row[6]=='cb24demi':
                            quantite=str(int(quantite)*2)
                            conditionnement='CBO24DE'
                        elif row[6]=='cb3':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3 mag':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3d.mg':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3dmags':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3mgs':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CBO4'
                        elif row[6]=='cb5':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='cb5mag':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='cb6 mag':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mag':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mg':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mgs':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='CBO':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO'
                        elif row[6]=='CBO':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO'
                        elif row[6]=='cn1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1imperiale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1magnum':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='cn6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='co1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='co12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='co6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='ct 1/2':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct.2 mg':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct10':
                            quantite=str(int(quantite)*10)
                            conditionnement='UNITE'
                        elif row[6]=='ct11':
                            quantite=str(int(quantite)*11)
                            conditionnement='UNITE'
                        elif row[6]=='ct12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='ct1dmg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct1mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct2':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2 double mag':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2mag':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2mags':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct3':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3blles':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3mag':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3mags':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct4mag':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct4mags':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct5':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='ct6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='ct7':
                            quantite=str(int(quantite)*7)
                            conditionnement='UNITE'
                        elif row[6]=='ct8':
                            quantite=str(int(quantite)*8)
                            conditionnement='UNITE'
                        elif row[6]=='cto12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='cto12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='COLLEC':
                            quantite=row[5]
                            conditionnement='COLLEC'
                        else:
                            quantite=row[5]
                            conditionnement='UNITE'
                            commentaires='Verif cdt - PV si rglt a fact : '+row[9]+' - '+row[4]
                        # Format de la bouteille
                        if row[8]=='demi blle':
                            formatb='DE'
                        elif row[8]=='1/2blles':
                            formatb='DE'
                        elif row[8]=='blle':
                            formatb='BO'
                        elif row[8]=='blle ':
                            formatb='BO'
                        elif row[8]=='blles':
                            formatb='BO'
                        elif row[8]=='blles':
                            formatb='BO'        
                        elif row[8]=='double mag':
                            formatb='DM'
                        elif row[8]=='dmg':
                            formatb='DM'
                        elif row[8]=='dmag':
                            formatb='DM'
                        elif row[8]=='dmags':
                            formatb='DM'
                        elif row[8]=='imp':
                            formatb='IM'
                        elif row[8]=='Imp':
                            formatb='IM'
                        elif row[8]=='imperiale':
                            formatb='IM'
                        elif row[8]=='impériale':
                            formatb='IM'
                        elif row[8]=='jéroboam':
                            formatb='JE'
                        elif row[8]=='jeroboam':
                            formatb='JE'
                        elif row[8]=='mg':
                            formatb='MG'
                        elif row[8]=='mag':
                            formatb='MG'
                        elif row[8]=='mgs':
                            formatb='MG'
                        elif row[8]=='mags':
                            formatb='MG'
                        elif row[8]=='magnum':
                            formatb='MG'
                        elif row[8]=='magnums':
                            formatb='MG'
                        else :
                            formatb=row[8]
                        # Prix
                        prix=row[7]
                        prix=row[7].replace('.',',')
                        prix=row[7].replace('€','')
                        prix=row[7].replace(' ','')
                        commentaires='PV si rglt a fact : '+row[8]+' - '+row[4]     
                    #Gestion domaine de la romanee conti
                    elif row[1]=='Domaine de la Romanée Conti ':
                        #traitement exception pour CSDRC
                        if row[3]=='':
                            chateau=row[1]+'caisse panachee'
                            chateau=chateau.replace('Château','')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('"','')
                            chateau=chateau.replace('ô','')
                            #annee CSDRC 
                            annee=row[0]
                            #quantite CSDRC
                            quantite=row[5]
                            #formatb CSDRC
                            if row[8]=='demi blle':
                                formatb='DE'
                            elif row[8]=='1/2blles':
                                formatb='DE'
                            elif row[8]=='blle':
                                formatb='BO'
                            elif row[8]=='blle ':
                                formatb='BO'
                            elif row[8]=='blles':
                                formatb='BO'
                            elif row[8]=='blles':
                                formatb='BO'        
                            elif row[8]=='double mag':
                                formatb='DM'
                            elif row[8]=='dmg':
                                formatb='DM'
                            elif row[8]=='dmag':
                                formatb='DM'
                            elif row[8]=='dmags':
                                formatb='DM'
                            elif row[8]=='imp':
                                formatb='IM'
                            elif row[8]=='Imp':
                                formatb='IM'
                            elif row[8]=='imperiale':
                                formatb='IM'
                            elif row[8]=='impériale':
                                formatb='IM'
                            elif row[8]=='jéroboam':
                                formatb='JE'
                            elif row[8]=='jeroboam':
                                formatb='JE'
                            elif row[8]=='mg':
                                formatb='MG'
                            elif row[8]=='mag':
                                formatb='MG'
                            elif row[8]=='mgs':
                                formatb='MG'
                            elif row[8]=='mags':
                                formatb='MG'
                            elif row[8]=='magnum':
                                formatb='MG'
                            elif row[8]=='magnums':
                                formatb='MG'
                            else :
                                formatb=row[8]
                            #conditionnement CSDRC
                            conditionnement='COLLEC'
                            #prix CSDRC + commentaire
                            prix=row[7]
                            prix=row[7].replace('.',',')
                            prix=row[7].replace('€','')
                            prix=row[7].replace(' ','')
                            commentaires=row[2]+' - '+row[4]+'PV si rglt a fact : '+row[9]
                        else:
                            #gestion normale du cas de DRC
                            chateau=row[1]+' '+row[3]
                            chateau=chateau.replace('Château','')
                            chateau=chateau.replace('é','e')
                            chateau=chateau.replace('è','e')
                            chateau=chateau.replace('"','')
                            chateau=chateau.replace('ô','')
                            #chateau=re.sub(r'[0-9]','',chateau)
                            # année
                            annee=row[0]
                            # quantite et conditionnement
                            quantite=row[5]
                            if row[6]=='cb12':
                                quantite=str(int(quantite)*12)
                                conditionnement='CBO12'
                            elif row[6]=='cb6':
                                quantite=str(int(quantite)*6)
                                conditionnement='CBO6'
                            elif row[6]=='cb 1mag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1 mag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1d.mg':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1dmag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1Imp':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1imperiale':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1Impériale':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1jero':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1jeroboam':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1Jéroboam':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1jéroboam':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1mag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb1mg':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO1'
                            elif row[6]=='cb2':
                                quantite=str(int(quantite)*2)
                                conditionnement='CBO2'
                            elif row[6]=='cb24demi':
                                quantite=str(int(quantite)*2)
                                conditionnement='CBO24DE'
                            elif row[6]=='cb3':
                                quantite=str(int(quantite)*3)
                                conditionnement='CBO3'
                            elif row[6]=='cb3 mag':
                                quantite=str(int(quantite)*3)
                                conditionnement='CBO3'
                            elif row[6]=='cb3d.mg':
                                quantite=str(int(quantite)*3)
                                conditionnement='CBO3'
                            elif row[6]=='cb3dmags':
                                quantite=str(int(quantite)*3)
                                conditionnement='CBO3'
                            elif row[6]=='cb3mgs':
                                quantite=str(int(quantite)*3)
                                conditionnement='CBO3'
                            elif row[6]=='cb4':
                                quantite=str(int(quantite)*4)
                                conditionnement='CBO4'
                            elif row[6]=='cb5':
                                quantite=str(int(quantite)*5)
                                conditionnement='UNITE'
                            elif row[6]=='cb5mag':
                                quantite=str(int(quantite)*5)
                                conditionnement='UNITE'
                            elif row[6]=='cb6 mag':
                                quantite=str(int(quantite)*6)
                                conditionnement='CBO6'
                            elif row[6]=='cb6mag':
                                quantite=str(int(quantite)*6)
                                conditionnement='CBO6'
                            elif row[6]=='cb6mg':
                                quantite=str(int(quantite)*6)
                                conditionnement='CBO6'
                            elif row[6]=='cb6mgs':
                                quantite=str(int(quantite)*6)
                                conditionnement='CBO6'
                            elif row[6]=='CBO':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO'
                            elif row[6]=='CBO':
                                quantite=str(int(quantite)*1)
                                conditionnement='CBO'
                            elif row[6]=='cn1':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='cn1imperiale':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='cn1mag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='cn1magnum':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='cn4':
                                quantite=str(int(quantite)*4)
                                conditionnement='CC4'
                            elif row[6]=='cn6':
                                quantite=str(int(quantite)*6)
                                conditionnement='CC6'
                            elif row[6]=='co1':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='co12':
                                quantite=str(int(quantite)*12)
                                conditionnement='CC12'
                            elif row[6]=='co6':
                                quantite=str(int(quantite)*6)
                                conditionnement='CC6'
                            elif row[6]=='ct 1/2':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='ct.2 mg':
                                quantite=str(int(quantite)*2)
                                conditionnement='CC2'
                            elif row[6]=='ct1':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='ct10':
                                quantite=str(int(quantite)*10)
                                conditionnement='UNITE'
                            elif row[6]=='ct11':
                                quantite=str(int(quantite)*11)
                                conditionnement='UNITE'
                            elif row[6]=='ct12':
                                quantite=str(int(quantite)*12)
                                conditionnement='CC12'
                            elif row[6]=='ct1dmg':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='ct1mag':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='ct1mg':
                                quantite=str(int(quantite)*1)
                                conditionnement='CC1'
                            elif row[6]=='ct2':
                                quantite=str(int(quantite)*2)
                                conditionnement='CC2'
                            elif row[6]=='ct2 double mag':
                                quantite=str(int(quantite)*2)
                                conditionnement='CC2'
                            elif row[6]=='ct2mag':
                                quantite=str(int(quantite)*2)
                                conditionnement='CC2'
                            elif row[6]=='ct2mags':
                                quantite=str(int(quantite)*2)
                                conditionnement='CC2'
                            elif row[6]=='ct3':
                                quantite=str(int(quantite)*3)
                                conditionnement='CC3'
                            elif row[6]=='ct3blles':
                                quantite=str(int(quantite)*3)
                                conditionnement='CC3'
                            elif row[6]=='ct3mag':
                                quantite=str(int(quantite)*3)
                                conditionnement='CC3'
                            elif row[6]=='ct3mags':
                                quantite=str(int(quantite)*3)
                                conditionnement='CC3'
                            elif row[6]=='ct4':
                                quantite=str(int(quantite)*4)
                                conditionnement='CC4'
                            elif row[6]=='ct4mag':
                                quantite=str(int(quantite)*4)
                                conditionnement='CC4'
                            elif row[6]=='ct4mags':
                                quantite=str(int(quantite)*4)
                                conditionnement='CC4'
                            elif row[6]=='ct5':
                                quantite=str(int(quantite)*5)
                                conditionnement='UNITE'
                            elif row[6]=='ct6':
                                quantite=str(int(quantite)*6)
                                conditionnement='CC6'
                            elif row[6]=='ct7':
                                quantite=str(int(quantite)*7)
                                conditionnement='UNITE'
                            elif row[6]=='ct8':
                                quantite=str(int(quantite)*8)
                                conditionnement='UNITE'
                            elif row[6]=='cto12':
                                quantite=str(int(quantite)*12)
                                conditionnement='CC12'
                            elif row[6]=='cto12':
                                quantite=str(int(quantite)*12)
                                conditionnement='CC12'
                            elif row[6]=='COLLEC':
                                quantite=row[5]
                                conditionnement='COLLEC'
                            else:
                                quantite=row[5]
                                conditionnement='UNITE'
                                commentaires='Verif cdt - PV si rglt a fact : '+row[8]+' - '+row[4]
                            # Format de la bouteille DRC
                            if row[8]=='demi blle':
                                formatb='DE'
                            elif row[8]=='1/2blles':
                                formatb='DE'
                            elif row[8]=='blle':
                                formatb='BO'
                            elif row[8]=='blle ':
                                formatb='BO'
                            elif row[8]=='blles':
                                formatb='BO'
                            elif row[8]=='blles':
                                formatb='BO'        
                            elif row[8]=='double mag':
                                formatb='DM'
                            elif row[8]=='dmg':
                                formatb='DM'
                            elif row[8]=='dmag':
                                formatb='DM'
                            elif row[8]=='dmags':
                                formatb='DM'
                            elif row[8]=='imp':
                                formatb='IM'
                            elif row[8]=='Imp':
                                formatb='IM'
                            elif row[8]=='imperiale':
                                formatb='IM'
                            elif row[8]=='impériale':
                                formatb='IM'
                            elif row[8]=='jéroboam':
                                formatb='JE'
                            elif row[8]=='jeroboam':
                                formatb='JE'
                            elif row[8]=='mg':
                                formatb='MG'
                            elif row[8]=='mag':
                                formatb='MG'
                            elif row[8]=='mgs':
                                formatb='MG'
                            elif row[8]=='mags':
                                formatb='MG'
                            elif row[8]=='magnum':
                                formatb='MG'
                            elif row[8]=='magnums':
                                formatb='MG'
                            else :
                                formatb=row[8]
                            # Prix et commentaire DRC
                            prix=row[7]
                            prix=row[7].replace('.',',')
                            prix=row[7].replace('€','')
                            prix=row[7].replace(' ','')
                            commentaires='PV si rglt a fact : '+row[9]+' - '+row[4]
                                             
                    else :
                        #gestion des autres cas
                        chateau=row[1]+' '+row[3]+' '+row[2]
                        chateau=chateau.replace('Château','')
                        chateau=chateau.replace('é','e')
                        chateau=chateau.replace('è','e')
                        chateau=chateau.replace('"','')
                        chateau=chateau.replace('ô','')
                        #chateau=re.sub(r'[0-9]','',chateau)
                            # année
                        annee=row[0]
                        # quantite et conditionnement
                        quantite=row[5]
                        if row[6]=='cb12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CBO12'
                        elif row[6]=='cb6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb 1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1 mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1d.mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1dmag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Imp':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1imperiale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Impériale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jero':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jeroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1Jéroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1jéroboam':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb1mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO1'
                        elif row[6]=='cb2':
                            quantite=str(int(quantite)*2)
                            conditionnement='CBO2'
                        elif row[6]=='cb24demi':
                            quantite=str(int(quantite)*2)
                            conditionnement='CBO24DE'
                        elif row[6]=='cb3':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3 mag':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3d.mg':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3dmags':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb3mgs':
                            quantite=str(int(quantite)*3)
                            conditionnement='CBO3'
                        elif row[6]=='cb4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CBO4'
                        elif row[6]=='cb5':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='cb5mag':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='cb6 mag':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mag':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mg':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='cb6mgs':
                            quantite=str(int(quantite)*6)
                            conditionnement='CBO6'
                        elif row[6]=='CBO':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO'
                        elif row[6]=='CBO':
                            quantite=str(int(quantite)*1)
                            conditionnement='CBO'
                        elif row[6]=='cn1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1imperiale':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn1magnum':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='cn4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='cn6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='co1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='co12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='co6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='ct 1/2':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct.2 mg':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct1':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct10':
                            quantite=str(int(quantite)*10)
                            conditionnement='UNITE'
                        elif row[6]=='ct11':
                            quantite=str(int(quantite)*11)
                            conditionnement='UNITE'
                        elif row[6]=='ct12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='ct1dmg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct1mag':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct1mg':
                            quantite=str(int(quantite)*1)
                            conditionnement='CC1'
                        elif row[6]=='ct2':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2 double mag':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2mag':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct2mags':
                            quantite=str(int(quantite)*2)
                            conditionnement='CC2'
                        elif row[6]=='ct3':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3blles':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3mag':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct3mags':
                            quantite=str(int(quantite)*3)
                            conditionnement='CC3'
                        elif row[6]=='ct4':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct4mag':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct4mags':
                            quantite=str(int(quantite)*4)
                            conditionnement='CC4'
                        elif row[6]=='ct5':
                            quantite=str(int(quantite)*5)
                            conditionnement='UNITE'
                        elif row[6]=='ct6':
                            quantite=str(int(quantite)*6)
                            conditionnement='CC6'
                        elif row[6]=='ct7':
                            quantite=str(int(quantite)*7)
                            conditionnement='UNITE'
                        elif row[6]=='ct8':
                            quantite=str(int(quantite)*8)
                            conditionnement='UNITE'
                        elif row[6]=='cto12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='cto12':
                            quantite=str(int(quantite)*12)
                            conditionnement='CC12'
                        elif row[6]=='COLLEC':
                            quantite=row[5]
                            conditionnement='COLLEC'
                        else:
                            quantite=row[5]
                            conditionnement='UNITE'
                            commentaires='Verif cdt - PV si rglt a fact : '+row[9]+' - '+row[4]
                        # Format de la bouteille
                        if row[8]=='demi blle':
                            formatb='DE'
                        elif row[8]=='1/2blles':
                            formatb='DE'
                        elif row[8]=='blle':
                            formatb='BO'
                        elif row[8]=='blle ':
                            formatb='BO'
                        elif row[8]=='blles':
                            formatb='BO'
                        elif row[8]=='blles':
                            formatb='BO'        
                        elif row[8]=='double mag':
                            formatb='DM'
                        elif row[8]=='dmg':
                            formatb='DM'
                        elif row[8]=='dmag':
                            formatb='DM'
                        elif row[8]=='dmags':
                            formatb='DM'
                        elif row[8]=='imp':
                            formatb='IM'
                        elif row[8]=='Imp':
                            formatb='IM'
                        elif row[8]=='imperiale':
                            formatb='IM'
                        elif row[8]=='impériale':
                            formatb='IM'
                        elif row[8]=='jéroboam':
                            formatb='JE'
                        elif row[8]=='jeroboam':
                            formatb='JE'
                        elif row[8]=='mg':
                            formatb='MG'
                        elif row[8]=='mag':
                            formatb='MG'
                        elif row[8]=='mgs':
                            formatb='MG'
                        elif row[8]=='mags':
                            formatb='MG'
                        elif row[8]=='magnum':
                            formatb='MG'
                        elif row[8]=='magnums':
                            formatb='MG'
                        else :
                            formatb=row[8]
                        # Prix
                        prix=row[7]
                        prix=row[7].replace('.',',')
                        prix=row[7].replace('€','')
                        prix=row[7].replace(' ','')
                        commentaires='PV si rglt a fact : '+row[9]+' - '+row[4]     
  
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
