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
    if 'Original' in recCond or 'origine' in recCond:
        # Conditionnements Bordeaux OWC
        conditionnement=recCond
        conditionnement=conditionnement.replace('Original wood case - Sold by ','CBO')
        conditionnement=conditionnement.replace('Orignal wood case - Sold by ','CBO')
        conditionnement=conditionnement.replace('Original wood case - Soldy by ','CBO')
        conditionnement=conditionnement.replace('Original wood case -Sold by ','CBO')
        conditionnement=conditionnement.replace('Original wood case -Sold by ','CBO')
        conditionnement=conditionnement.replace('Original wood case - Sold by ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine - Vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine - vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine- vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine- Vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine-Vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois d\'origine-vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois D\'origine-Vendu par ','CBO')
        conditionnement=conditionnement.replace('Caisse bois D\'origine-vendu par ','CBO')
        commentaire=''
    else:
        # Conditionnement par défaut pour Bordeaux NotOWC + commentaires
        if formatb=='BO':
            if int(quantite)<12:
                conditionnement='UNITE'
            else:
                conditionnement='CBO12'
        elif formatb=='DE':
            if int(quantite)<24:
                conditionnement='UNITE'
            else:
                conditionnement='CBO24DE'
        elif formatb=='CL':
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
        else:
            conditionnement='UNITE'


        if Appelation in appAutres :
            if row[9] != '' or row[10] != '' or row[11] != '':
                commentaire = 'Verif cdt - Etq : '+unidecode(row[9])+' - Niveau : '+unidecode(row[10])+' - '+unidecode(row[11])
            else:
                commentaire = 'Verif cdt'
        else:
            if row[8] != '' or row[9] != '' or row[10] != '':
                commentaire = 'Verif cdt - Etq : '+unidecode(row[8])+' - Niveau : '+unidecode(row[9])+' - '+unidecode(row[10])
            else:
                commentaire = 'Verif cdt'

    return [conditionnement,commentaire]



for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_ANGWIN2.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for row in reader:

                ####################################
                ### DICTIONNAIRE DES APPELATIONS ###
                ####################################
                appBdx = ["Saint Emilion","Pauillac","Saint Julien","Haut Médoc","Margaux","Pessac Léognan","Listrac Médoc","Saint Estèphe","Pomerol","Côtes de Bourg","Médoc","Moulis en Médoc","Moulis en Medoc","Côtes de Castillon","Castillon","Sauternes","Graves","Lalande de Pomerol","Fronsac","Bordeaux Côtes de Francs","Bordeaux","Sainte Foy Bordeaux"]
                appAutres = ["étrangers","Etrangeres","Alsace","Beaujolais","Corse","Etranger","Jura","Languedoc Roussillon","Loire","Outside France","Provence","Savoie","Sud Ouest","Côteaux du Languedoc"]
                appRhone = ["Crozes Hermitage","Cornas","Côtes du Rhône","Saint Joseph","VDP de Méditerranée","Châteauneuf du Pape","Côte Rôtie","Hermitage","Côtes du Rhône","Vacqueyras","VDP de Vaucluse","IGP Vaucluse","Château Grillet","Cairanne","IGP Collines Rhodaniennes","Condrieu","Costières de Nimes","Côtes du Vivarais"]
                appChampagne = ["Champagne"]

                ##############################################################
                ### VARIABLE DE COLONNES                                   ###
                ### SI CHANGEMENTS DANS L'ORDRE DES COLONNES, PROCEDEZ ICI ###
                ##############################################################

                recCond = row[8]
                Appelation = row[0]
                Estate = row[1]

                if Appelation in appAutres:
                    Wine = row[3]
                    Color = row[4]
                    fPrix=repr(row[8])
                    quantite=row[7]
                    annee=row[5]
                elif Appelation in appRhone:
                    Wine = row[2]
                    Color = row[3]
                    fPrix=repr(row[7])
                    quantite=row[6]
                    annee=row[4]
                elif Appelation in appChampagne:
                    Wine = row[2]
                    Color = row[3]
                    fPrix=repr(row[7])
                    quantite=row[6]
                    if row[4]!='':
                        annee=row[4]
                    else:
                        annee='0'
                else:
                    Wine = row[2]
                    Color = row[3]
                    fPrix=repr(row[7])
                    quantite=row[6]
                    annee=row[4]

                if quantite == '':
                    quantite = 0

                if annee == 'NV':
                    annee = 'NV'
                elif annee =='':
                    annee = 'NV'
                elif annee == '0':
                    annee = 'NV'

                ####################################
                ### FORMATAGE DE LA CHAINE fPrix ###
                ####################################

                fPrix=unidecode(fPrix)
                fPrix=fPrix.replace("'","")
                fPrix=fPrix.replace("\\","")
                fPrix=fPrix.replace("u202f","")
                fPrix=fPrix.replace(" EUR","")
                prix=fPrix

                if Appelation in appAutres :
                #Format bouteille
                    if row[6]=='75':
                        formatb='BO'
                    elif row[6]=='150':
                        formatb='MG'
                    elif row[6]=='300':
                        formatb='DM'
                    elif row[6]=='37.5':
                        formatb='DE'
                    elif row[6]=='50':
                        formatb='CL'
                    elif row[6]=='500':
                        formatb='JE'
                    elif row[6]=='600':
                        formatb='IM'
                    else:
                        formatb=row[6]
                elif Appelation in appChampagne :
                #Format bouteille
                    if row[5]=='75':
                        formatb='BO'
                    elif row[5]=='150':
                        formatb='MG'
                    elif row[5]=='300':
                        formatb='DM'
                    elif row[5]=='37.5':
                        formatb='DE'
                    elif row[5]=='50':
                        formatb='CL'
                    elif row[5]=='500':
                        formatb='JE'
                    elif row[5]=='600':
                        formatb='IM'
                    else:
                        formatb=row[5]
                else:
                #Format bouteille
                    if row[5]=='75':
                        formatb='BO'
                    elif row[5]=='150':
                        formatb='MG'
                    elif row[5]=='300':
                        formatb='DM'
                    elif row[5]=='37.5':
                        formatb='DE'
                    elif row[5]=='50':
                        formatb='CL'
                    elif formatb == '450':
                        formatb = 'RE'
                    elif row[5]=='500':
                        formatb='JE'
                    elif row[5]=='600':
                        formatb='IM'
                    else:
                        formatb=row[5]

                #######################
                ### LIGNES A ECRIRE ###
                #######################

                if row[1]=='Estate':
                    # Exclusion de l'en-tête de colonne
                    bEcrire=0

                else:
                    bEcrire=1

                    ###############################################################
                    ### Récupération du nom du vin dans une chaine de caractère ###
                    ###############################################################
                    chaine=unidecode(Wine)
                    # Split de la chaine
                    chaine=re.split('[0-9][0-9][0-9][0-9]',chaine)

                    #############################
                    ### BORDEAUX OWC & NOTOWC ###
                    #############################
                    if Appelation in appBdx :
                        if Color == 'White':
                            chateau = chaine[0]+' blanc'
                            CondCom = Cond(recCond,formatB,quantite)
                            conditionnement = CondCom[0]
                            commentaire = CondCom[1]
                        else:
                            chateau = chaine[0]
                            CondCom = Cond(recCond,formatb,quantite)
                            conditionnement = CondCom[0]
                            commentaire = CondCom[1]

                    ######################################################
                    ### TRAITEMENT LIGNES AUTRES QUE BDX, BGO et RHONE ###
                    ######################################################
                    elif Appelation in appAutres:
                        chateau = chaine[0]
                        CondCom = Cond(recCond,formatB,quantite)
                        conditionnement=CondCom[0]
                        commentaire = CondCom[1]

                    ######################################################
                    ### TRAITEMENT LIGNES AUTRES QUE BDX, BGO et RHONE ###
                    ######################################################
                    elif Appelation in appChampagne:
                        chateau = chaine[0]
                        CondCom = Cond(recCond,formatb,quantite)
                        conditionnement=CondCom[0]
                        commentaire = CondCom[1]
                        #commentaire = 'Verif cdt - '+unidecode(row[12])+' '+unidecode(row[13])+' '+unidecode(row[14])

                    ##############################################
                    ####### TRAITEMENT DES LIGNES BGO ET RHONE ###
                    ##############################################
                    else:
                        chateau = chaine[0]
                        # Conditionnement par defaut
                        CondCom = Cond(recCond,formatB,quantite)
                        conditionnement = CondCom[0]
                        commentaire = CondCom[1]
                        # if Appelation in appRhone :
                        #     commentaire = 'Verif cdt - '+unidecode(row[12])+' '+unidecode(row[13])+' '+unidecode(row[14])
                        # else:
                        #     commentaire = 'Verif cdt - '+unidecode(row[12])+' '+unidecode(row[13])

                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1:
                    chateau = chateau.replace('"','')
                    chateau = chateau.replace(',','')
                    chateau = chateau.strip()
                    commentaire = commentaire.replace(',','')
                    newRow=[chateau,annee,formatB,prix,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
            monFichierEntre.close()
