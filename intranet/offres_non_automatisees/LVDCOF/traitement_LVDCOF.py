## coding: utf-8
import csv
import glob
import re
import io
import time
from unidecode import unidecode
import sys
sys.path.append("/var/www/html/php/fonctions_tarifs")
import Fonction_tarifs as ft

# Quand on passe de fichier xslx à csv : des lettres (z) se mettent sur les noms des derniers vins

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_LVDCOF.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index_chateau = 0
            vCond = 0
            trou='' # besoin de le faire une seule fois

            for row in reader:

                appellation = unidecode(row[2]).upper()

                chateau = unidecode(row[0]).upper()

                quantite = str(unidecode(row[5]))
                quantite = quantite.replace(' ', '')
                quantite = ft.formaterQuantite(quantite)
            
                prix = unidecode(row[4])

                # formatte le prix pour qu'il ne reste que des chiffres
                prix = ft.formaterPrix(prix)
                
                # Test si la ligne n'est pas à copier dans le fichier final : OUI continue la boucle NON continue les instructions pour cette ligne
                if (ft.bLigneIncorrecte(prix, quantite)) :
                    # i=i+1 :debug
                    continue

                #######
                bEcrire=0
                #il ne faut rien faire sur les lignes d'en-tête
                # if row[0]=="" or row[0]=="WINE" or row[4]=="":
                #     continue

                # A partir de là, on traite les lignes et ne surtout pas oublier les vins blancs !
                # chateau=unidecode(row[0])


                # annee
                annee = row[1]
                annee = ft.formaterAnnee(annee)

                # if row[4]=='NV':
                #     annee=time.strftime('%Y')
                # else:
                #     annee=row[4]

                # Format de bouteille
                formatB=unidecode(row[6])+''
                formatB = ft.formaterFormatBouteille(formatB)

                # Prix , on nettoie la chaine prix
                # prix=repr(row[4])
                # prix=fichierFonction.formatterPrix(prix)

                #quantite
                # quantite=repr(row[5])
                # quantite=fichierFonction.formatterQuantite(quantite)

                #if ''
                
                # Avant
                #if 'CB 12' in row[7]:
                #    conditionnement='CBO12'
                #elif 'CB 6' in row[7]:
                #    conditionnement='CBO6'
                #elif 'CB 3' in row[7]:
                #    conditionnement='CBO3'
                #elif 'CB 1' in row[7]:
                #    conditionnement='CBO1'
                #elif 'CT 12' in row[7] or 'CTN 12' in row[7]:
                #    conditionnement='CC12'
                #elif 'CT 6' in row[7] or 'CTN 6' in row[7]:
                #    conditionnement='CC6'
                #else:
                #    conditionnement='UNITE'

                conditionnement = unidecode(row[7])

                if 'Wooden Case 1' in conditionnement:
                    conditionnement='CBO1'
                elif 'Wooden Case 2' in conditionnement or 'Wooden case 2' in conditionnement:
                    conditionnement='CBO2'
                elif 'Wooden Case 3' in conditionnement or 'Wooden case 3' in conditionnement or 'Wooden Case 1 & 3' in conditionnement:
                    conditionnement='CBO3'
                elif 'Wooden Case 6' in conditionnement or 'Wooden case 6' in conditionnement or 'Wooden Case 1 & 6' in conditionnement or 'Wooden Case 1, 3 & 6' in conditionnement or 'Wooden Case 3 & 6' in conditionnement:
                    conditionnement='CBO6'
                elif 'Wooden Case 12' in conditionnement or 'Wooden Case 6 & 12' in conditionnement or 'Wooden case 6 & 12' in conditionnement:
                    conditionnement='CBO12'
                elif 'Carton Box 3' in conditionnement:
                    conditionnement='CC3'
                elif 'Carton Box 4' in conditionnement:
                    conditionnement='CC4'
                elif 'Carton Box 6' in conditionnement:
                    conditionnement='CC6'
                elif 'Carton Box 6 & 12' in conditionnement:
                    conditionnement='CC12'
                else:
                    conditionnement='UNITE'

                #Commentaire
                #commentaire='VERIF CDT - Qte = '+row[7]
                # commentaire='VERIF CDT'

                commentaire = ""

                if annee.find('-') != -1:
                    # commentaire = commentaire+' '+annee
                    commentaire = annee
                    annee = 'NV'

                Officieux = 1

                # écriture de la ligne
                # On fabrique la nouvelle ligne dans l'ordre voulu
                newRow=[chateau,annee,formatB,prix,quantite,conditionnement,commentaire,Officieux]
                writer.writerow(newRow)


            monFichierEntre.close()
