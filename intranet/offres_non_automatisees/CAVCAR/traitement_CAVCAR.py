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

import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

nomProfil : str = "CAVCAR"
extensionDebut : str = ".csv"
extensionFin : str = ".csv"

###############################################################
### Fonction pour application du conditionnement par defaut ###
###############################################################

for filename in glob.glob('*' + extensionDebut):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_' + nomProfil + extensionFin
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            # writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='', quotechar='') 
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')

            for row in reader:
                officieux='1'

                ##############################################################
                ### VARIABLE DE COLONNES                                   ###
                ### SI CHANGEMENTS DANS L'ORDRE DES COLONNES, PROCEDEZ ICI ###
                ##############################################################
                Mill_Reg = row[0]
                quantite = row[6]
                formatB = row[1]
                conditionnement = row[5]
                Appellation_Domaine = unidecode(row[2])
                vin = unidecode(row[3])
                prix = row[4]
                couleur = row[7]

                ####################################
                ### FORMATAGE DE LA CHAINE fPrix ###
                ####################################
                prix : str = unidecode(str(ft.formaterPrix(prix)))

                # print("prix : " + prix)

                #######################################
                ### Identification ds lignes Region ###
                #######################################

                # if Mill_Reg == 'Bordeaux' :
                #     iBdx = 1

                #######################
                ### LIGNES A ECRIRE ###
                #######################

                # Exclusion de l'en-tête de colonne
                # if (row[0]!='' and row[6]=='') or (row[0]=='Mill.'):
                #     continue

                # designation_prix = ["/BTS"]

                designation_prix = ["/BTS"]

                # ft.bLigneIncorrecte(prix, designation_prix, vin) ???

                if( ft.bLigneIncorrecte(prix, designation_prix, vin)):
                    continue;

                # print("prix : " + prix)

                vin = Appellation_Domaine+' '+vin

                ####################################
                ### FORMATAGE DE LA CHAINE Vol   ###
                ####################################

                formatB : str = str(ft.formaterFormatBouteille(formatB)) 

                annee = Mill_Reg
                annee = annee.replace(".","")

                # conditionnement = row[3] ???

                commentaire : str = ""

                if (conditionnement is None) or (len(conditionnement) == 0):
                    commentaire += ft.verif_cdt_str

                # Conditionnement OWC
                if conditionnement != "":

                    # Conditionnements Bordeaux OWC
                    conditionnement=conditionnement.replace('/','')
                    conditionnement=conditionnement.replace('mag','')
                    conditionnement=conditionnement.replace('imp','')
                    conditionnement=conditionnement.replace('D-MAG','')
                    conditionnement=conditionnement.replace(' 1/2','DE')
                    conditionnement=conditionnement.replace('CT','CC')
                    conditionnement=conditionnement.replace('OC','CC')
                    conditionnement=conditionnement.replace('jero','')
                    conditionnement=conditionnement.replace('mathu','')
                    conditionnement=conditionnement.replace("NEUTRE6MAG",'CBN6')
                    conditionnement=conditionnement.replace("CC6 MIXED",'COLLEC')
                    conditionnement=conditionnement.replace("CBO6MIX",'COLLEC')

                    commentaire = ''
                else:

                    # Conditionnement par défaut pour Bordeaux NotOWC + commentaires
                    conditionnement = ft.formaterConditionnement(formatB, int(quantite), conditionnement, vin)

                # On fabrique la nouvelle ligne dans l'ordre voulu
                newRow=[vin,annee,formatB,prix,quantite,conditionnement,commentaire,officieux]
                writer.writerow(newRow)

            monFichierEntre.close()
