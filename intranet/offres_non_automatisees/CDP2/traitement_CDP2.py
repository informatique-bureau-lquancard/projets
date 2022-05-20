import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CDP2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'
                if row[1]=='':
                    pass
                else:
                    # Nom du chateau
                    chateau=row[1]
                    # année
                    annee=row[0]
                    
                    # quantite
                    quantite=row[4]
                    # Format de la bouteille
                    if row[2]=='37.5 cl':
                        formatb='DE'
                    elif row[2]=='37,5 cl':
                        formatb='DE'
                    elif row[2]=='20 cl':
                        formatb='1/4'
                    elif row[2]=='25 cl':
                        formatb='1/4'
                    elif row[2]=='35 cl':
                        formatb='1/4'
                    elif row[2]=='35 cl':
                        formatb='1/4'
                    elif row[2]=='50 cl':
                        formatb='CL'
                    elif row[2]=='63 cl':
                        formatb='BT'
                    elif row[2]=='70 cl':
                        formatb='BT'
                    elif row[2]=='75 cl':
                        formatb='BO'
                    elif row[2]=='1000 cl':
                        formatb='L'
                    elif row[2]=='150 cl':
                        formatb='MG'
                    elif row[2]=='300 cl':
                        formatb='DM'
                    elif row[2]=='500 cl':
                        formatb='JE'
                    elif row[2]=='600 cl':
                        formatb='IM'
                    else :
                        formatb=row[2]
                    # Prix
                    prix=row[5]
                    #prix=row[6].replace('.',',')
                    prix=row[5].replace('€','')
                    #prix=row[6].replace(' ','')

                    #conditionnement et commentaires
                    if row[3]=='':
                        if formatb=='DE':
                            if int(quantite)<24:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO24DE'
                                commentaires='VERIF CDT'
                        elif formatb=='1/4':
                            conditionnement='UNITE'
                            commentaires='VERIF CDT'
                        elif formatb=='CL':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'
                        elif formatb=='BT':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'
                        elif formatb=='BO':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'
                        elif formatb=='L':
                            if int(quantite)<12:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO12'
                                commentaires='VERIF CDT'
                        elif formatb=='MG':
                            if int(quantite)<6:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO6'
                                commentaires='VERIF CDT'
                        elif formatb=='DM':
                            if int(quantite)<3:
                                conditionnement='UNITE'
                                commentaires='VERIF CDT'
                            else:
                                conditionnement='CBO3'
                                commentaires='VERIF CDT'
                        elif formatb=='JE':
                            conditionnement='CBO1'
                            commentaires='VERIF CDT'
                        elif formatb=='IM':
                            conditionnement='CBO1'
                            commentaires='VERIF CDT'
                    elif row[2]=='C/8':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/7':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/5':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/10':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/11':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/18':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='C/9':
                        conditionnement='UNITE'
                        commentaires='Verif cdt : '+row[3]
                    elif row[2]=='CBO/10':
                        conditionnement='CBO'
                        commentaires='Verif cdt : '+row[3]
                    else:
                        conditionnement=row[3]
                        conditionnement=conditionnement.replace('CBM/','CBN')
                        conditionnement=conditionnement.replace('CBDM/','CBN')
                        conditionnement=conditionnement.replace('CM/','CBN')
                        conditionnement=conditionnement.replace('CBO/','CBO')
                        conditionnement=conditionnement.replace('C/','CC')
                        commentaires='Verif cdt : '+row[3]
 
                    # On fabrique la nouvelle ligne dans l'ordre voulu
                    trou=''
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaires,officieux,trou,trou]
                    writer.writerow(newRow)
            monFichierEntre.close()
