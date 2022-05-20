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
        conditionnement=conditionnement.replace('C/','CC')
        conditionnement=conditionnement.replace('CBO/','CBO')
        conditionnement=conditionnement.replace('Btle','UNITE')
        conditionnement=conditionnement.replace('Magnum','UNITE')
        conditionnement=conditionnement.split(' ')[0]

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
        nom_sortie='sortie_CAVEX.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:
                officieux='1'

                ##############################################################
                ### VARIABLE DE COLONNES                                   ###
                ### SI CHANGEMENTS DANS L'ORDRE DES COLONNES, PROCEDEZ ICI ###
                ##############################################################
                annee = row[7]
                region = row[2]
                quantite = row[6]
                Vol = row[8]
                recCond = row[5]
                Appellation_Domaine = unidecode(row[1])
                Vin = unidecode(row[0])
                fPrix = row[9]
                couleur = row[4]

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

                #######################
                ### LIGNES A ECRIRE ###
                #######################

                if row[1]== 'Domaine':
                    # Exclusion de l'en-tête de colonne
                    bEcrire=0
                elif row[0]=='' and row[6]=='':
                    bEcrire=0
                else:
                    bEcrire=1

                    if region == 'Bordeaux':
                        chateau = Vin
                    else:
                        chateau = Appellation_Domaine+' '+Vin

                    ####################################
                    ### FORMATAGE DE LA CHAINE Vol   ###
                    ####################################

                    if Vol == '75' or Vol =='70' or Vol == '62':
                        formatb = 'BO'
                    elif Vol == '50':
                        formatb = 'CL'
                    elif Vol == '150':
                        formatb = 'MG'
                    elif Vol == '300':
                        formatb = 'DM'
                    elif Vol == '500':
                        formatb = 'JE'
                    elif Vol == '600':
                        formatb = 'IM'
                    elif Vol == '37.5' or Vol == '37,5':
                        formatb = 'DE'
                    elif Vol == '100':
                        formatb = 'L'
                    elif Vol == '450' and 'Caisse' not in Vin:
                        formatb = 'RE'
                    elif Vol == '450' and 'Caisse' in Vin:
                        formatb = 'BO'
                    elif Vol == '675' and 'Caisse' in Vin:
                        formatb = 'BO'
                    else:
                        formatb = Vol


                    conditionnement = Cond(recCond,formatb,quantite)[0]
                    commentaire = Cond(recCond,formatb,quantite)[1]

                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1:
                    newRow=[chateau,annee,formatb,prix,quantite,conditionnement,commentaire,officieux]
                    writer.writerow(newRow)
            monFichierEntre.close()
