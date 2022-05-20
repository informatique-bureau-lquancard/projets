import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CDP3.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'
                if row[1]=='':
                    bEcrire=0
                else:
                    bEcrire=1

                    if 'Bordeaux Rouge' in row[0]:
                        chateau=unidecode(row[3])
                    elif 'Bordeaux Blanc' in row[0] and 'BLANC' not in row[3]:
                        chateau=unidecode(row[3])+' blanc'
                    elif 'Bordeaux Blanc' in row[0] and 'BLANC' in row[3]:
                        chateau=unidecode(row[3])
                    else:
                        chateau=unidecode(row[1])+' '+unidecode(row[3]) 
                    
                    # année
                    annee=row[2]
                    
                    # quantite
                    quantite=row[6]

                    # Format de la bouteille
                    if row[4]=='37.5 cl':
                        formatb='DE'
                    elif row[4]=='37,5 cl':
                        formatb='DE'
                    elif row[4]=='20 cl':
                        formatb='1/4'
                    elif row[4]=='25 cl':
                        formatb='1/4'
                    elif row[4]=='35 cl':
                        formatb='1/4'
                    elif row[4]=='35 cl':
                        formatb='1/4'
                    elif row[4]=='50 cl':
                        formatb='CL'
                    elif row[4]=='63 cl':
                        formatb='BT'
                    elif row[4]=='70 cl':
                        formatb='BT'
                    elif row[4]=='75 cl':
                        formatb='BO'
                    elif row[4]=='1000 cl':
                        formatb='L'
                    elif row[4]=='150 cl':
                        formatb='MG'
                    elif row[4]=='300 cl':
                        formatb='DM'
                    elif row[4]=='500 cl':
                        formatb='JE'
                    elif row[4]=='600 cl':
                        formatb='IM'
                    else :
                        formatb=row[4]
                    # Prix
                    fPrix=repr(row[7])
                    fPrix=fPrix.replace("'","")
                    fPrix=fPrix.replace("\\","")
                    fPrix=fPrix.replace("u202f","")
                    prix=unidecode(fPrix)
                    prix=prix.replace(" EUR","")
                    prix=prix.replace(".",",")

                    #conditionnement et commentaires
                    if row[5]=='':
                        if formatb=='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO24DE'
                        elif formatb=='1/4':
                            conditionnement='UNITE'
                        elif formatb=='CL':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO12'
                        elif formatb=='BT':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO12'
                        elif formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO12'
                        elif formatb=='L':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO12'
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO6'
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                            else:
                                conditionnement='CBO3'
                        elif formatb=='JE':
                            conditionnement='CBO1'
                        elif formatb=='IM':
                            conditionnement='CBO1'
                    elif row[5]=='C/8':
                        conditionnement='UNITE'
                    elif row[5]=='C/7':
                        conditionnement='UNITE'
                    elif row[5]=='C/5':
                        conditionnement='UNITE'
                    elif row[5]=='C/10':
                        conditionnement='UNITE'
                    elif row[5]=='C/11':
                        conditionnement='UNITE'
                    elif row[5]=='C/18':
                        conditionnement='UNITE'
                    elif row[5]=='C/9':
                        conditionnement='UNITE'
                    elif row[5]=='CBO/10':
                        conditionnement='CBO'
                    else:
                        conditionnement=row[5]
                        conditionnement=conditionnement.replace('CBM/','CBN')
                        conditionnement=conditionnement.replace('CO/','CC')
                        conditionnement=conditionnement.replace('CBDMO/','CBN')
                        conditionnement=conditionnement.replace('CGBO/','CBO')
                        conditionnement=conditionnement.replace('CBDM/','CBN')
                        conditionnement=conditionnement.replace('CBMO/','CBO')
                        conditionnement=conditionnement.replace('CMO/','CBO')
                        conditionnement=conditionnement.replace('CMAT/','CC')
                        conditionnement=conditionnement.replace('CM/','CBN')
                        conditionnement=conditionnement.replace('CBO/','CBO')
                        conditionnement=conditionnement.replace('C/','CC')
                        conditionnement=conditionnement.replace('CB/','CBO')
                        
                
                    commentaires='VERIF CDT : '+row[5]




                    
                if bEcrire==1:
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,officieux,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
