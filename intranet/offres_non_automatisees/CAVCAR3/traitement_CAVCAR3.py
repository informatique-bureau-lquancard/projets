# -*- coding: utf-8 -*-
import csv
import glob
import re
from unidecode import unidecode
# coding: utf-8

global quantite
global Appelation
global formatb
global conditionnement
global recCond


###############################################################
### Fonction pour application du conditionnement par defaut ###
###############################################################

def Cond(recCond,formatb,quantite):


    # Conditionnement OWC
    if recCond!="":

        # Conditionnements Bordeaux OWC
        conditionnement=recCond
        conditionnement=conditionnement.replace('/','')
        conditionnement=conditionnement.replace('mag','')
        conditionnement=conditionnement.replace('imp','')
        conditionnement=conditionnement.replace('D-MAG','')
        conditionnement=conditionnement.replace(' 1/2','DE')
        conditionnement=conditionnement.replace('CT','CC')
        conditionnement=conditionnement.replace('OC','CC')
        conditionnement=conditionnement.replace('jero','')
        conditionnement=conditionnement.replace('mathu','')
        commentaire = ''
    else:

        # Conditionnement par défaut pour Bordeaux NotOWC + commentaires
        if formatb=='BO':
            if int(quantite)<12:
                conditionnement='UNITE'
                commentaire='Verif cdt'
            else:
                conditionnement='CBO12'
                commentaire='Verif cdt'
        elif formatb=='DE':
            if int(quantite)<24:
                conditionnement='UNITE'
                commentaire='Verif cdt'
            else:
                conditionnement='CBO24DE'
                commentaire='Verif cdt'
        elif formatb=='CL':
            if int(quantite)<12:
                conditionnement='UNITE'
                commentaire='Verif cdt'
            else:
                conditionnement='CBO12'
                commentaire='Verif cdt'
        elif formatb=='MG':
            if int(quantite)<6:
                conditionnement='UNITE'
                commentaire='Verif cdt'
            else:
                conditionnement='CBO6'
                commentaire='Verif cdt'
        elif formatb=='DM':
            if int(quantite)<3:
                conditionnement='UNITE'
                commentaire='Verif cdt'
            else:
                conditionnement='CBO3'
                commentaire='Verif cdt'
        elif formatb=='JE':
            conditionnement='CBO1'
            commentaire='Verif cdt'
        elif formatb=='IM':
            conditionnement='CBO1'
            commentaire='Verif cdt'
        else:
            conditionnement='UNITE'
            commentaire='Verif cdt'



    return [conditionnement,commentaire]



for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_CAVCAR2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'

                ##############################################################
                ### VARIABLE DE COLONNES                                   ###
                ### SI CHANGEMENTS DANS L'ORDRE DES COLONNES, PROCEDEZ ICI ###
                ##############################################################
                Mill_Reg = row[0]
                Qte = row[6]
                Vol = row[1]
                recCond = row[5]
                Appellation_Domaine = unidecode(row[2])
                Vin = unidecode(row[3])
                fPrix = row[4]
                couleur = row[7]

                ####################################
                ### FORMATAGE DE LA CHAINE fPrix ###
                ####################################
                fPrix=unidecode(fPrix)
                fPrix=fPrix.replace("'","")
                fPrix=fPrix.replace("\\","")
                fPrix=fPrix.replace("u202f","")
                fPrix=fPrix.replace(" EUR","")
                fPrix=fPrix.replace(" ","")
                prix=fPrix

                #######################################
                ### Identification ds lignes Region ###
                #######################################
                if Mill_Reg == 'Alsace':
                    iBdx = 0
                elif Mill_Reg == 'Beaujolais':
                    iBdx = 0
                elif Mill_Reg == 'Bordeaux' :
                    iBdx = 1
                elif Mill_Reg == 'Bourgogne' :
                    iBdx = 0
                elif Mill_Reg == 'Champagne' :
                    iBdx = 0
                elif Mill_Reg == 'Vallée du Rhône':
                    iBdx = 0


                #######################
                ### LIGNES A ECRIRE ###
                #######################

                if row[0]!='' and row[6]=='':
                    # Exclusion de l'en-tête de colonne
                    bEcrire=0
                elif row[0]=='' and row[6]=='':
                    bEcrire=0
                elif row[0]=='Mill.':
                    bEcrire=0
                else:
                    bEcrire=1

                    if iBdx == 1:
                        chateau = Vin
                    else:
                        chateau = Appellation_Domaine+' '+Vin

                    ####################################
                    ### FORMATAGE DE LA CHAINE Vol   ###
                    ####################################

                    if Vol == '75 cl' or Vol =='70 cl' or Vol == '62 cl':
                        formatb = 'BO'
                    elif Vol == '50 cl':
                        formatb = 'CL'
                    elif Vol == '150 cl':
                        formatb = 'MG'
                    elif Vol == '300 cl':
                        formatb = 'DM'
                    elif Vol == '500 cl':
                        formatb = 'JE'
                    elif Vol == '600 cl':
                        formatb = 'IM'
                    elif Vol == '37.5 cl' or Vol == '37,5 cl':
                        formatb = 'DE'
                    elif Vol == '100 cl':
                        formatb = 'L'
                    elif Vol == '450 cl' and 'Caisse' not in Vin:
                        formatb = 'RE'
                    elif Vol == '450 cl' and 'Caisse' in Vin:
                        formatb = 'BO'
                    elif Vol == '675 cl' and 'Caisse' in Vin:
                        formatb = 'BO'
                    else:
                        formatb = Vol

                    quantite = Qte

                    annee = Mill_Reg
                    annee = annee.replace(".","")

                    conditionnement = Cond(recCond,formatb,quantite)[0]
                    commentaire = Cond(recCond,formatb,quantite)[1]

                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1:
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux]
                    writer.writerow(newRow)
            monFichierEntre.close()
