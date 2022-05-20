from unidecode import unidecode

import time

import re
import pandas as pd

import sys
sys.path.append("/var/www/html/ressources/nomenclature")
#import nomenclature as nom

#fichierFonction_blq_test permet d'utiliser les fonctionnalités de fichierFonction_blq_test sans modifier directement le fichier

# Mise en forme des différentes appelations des vins de Bordeaux
tab_appelation_bdx = ['AMIOT-SERVELLE', 'BARSAC', 'BORDEAUX', 'BORDEAUX SEC', 'FRANCS-COTES-DE-BORDEAUX', 'MARGAUX', 'MEDOC', 'MOULIS', 'PAUILLAC',
                'PESSAC-LEOGNAN', 'POMEROL', 'SAINT-EMILION', 'SAINT-EMILION GRAND CRU', 'SAINT-JULIEN', 'SAINT-ESTEPHE', 
                'SAUTERNES']

tab_conditionnement = ["UNITE", "CBO1", "CBO1DE", "CBO1G", "CBN1", "CCBO6", "CCBO12", "Cof", "CF3", "CF6", "CF1", "COLLEC", "GIBO1", "CC100", "CC", "CBO12", "CBO12DE", "CBO12PLA", "CBN", "CBN12", "C12D", "CC12DE", "CCN12",
"CBO16", "CBO2", "CBN2", "CBO24DE", "CC24", "CBO3", "CBN3", "CBO4", "CB4MAG", "CBN4", "CBO5", "CC5", "CBO6", "CBO6DE", "CBO6CLA", "CBO6PLA", "CBN6", "CC6COU", "CC6DEB", "CC6DES", "CC6PLA", "CCN6", "BOX", "CC7", "CBO8",
"CC1", "ETUI1", "CC2", "CC3", "CC4", "CC6", "CBO9", "CBO", "CC12", "CB1", "CB3", "CB6", "CB12"]

# A revoir
# tab_conditionnement = ["UNITE","CC1","CC2","CC3","CC4","CC6","CC12","CC24","CC24DE","CBO1","CBO2","CBO3","CBO4","CBO6","CBO12","CBO24","CBO24DE","COLLEC", "CB1", "CB3", "CB6", "CB12"]

tab_collection = ['COLLECTION']

# Faire attention certaine chaine de caractere ne marche pas
def supprimeChaineCaracteres(chaine_a_modifier : str, suppression_designation):
    
    for cellule_tableau in suppression_designation:
        chaine_a_modifier = chaine_a_modifier.replace(cellule_tableau, '')

    # Enlève les espaces en trop en début et fin de chaine de caractères
    return chaine_a_modifier.strip()

def testVinCollection(vin):

    index_chateau : int = -1
    
    for chaine_possible_collection in tab_collection:

        index_chateau : int = vin.find(chaine_possible_collection)

        if(index_chateau != -1):
    
            return index_chateau
            
    return index_chateau

tab_formater_vin = [",", "DOUBLE MAGNUM", "MAGNUM", "JEROBOAM", "NDEG", "NONE"]
tab_couleur_blanche = ["BLANC", "BL", "WHITE"]
tab_couleur_rose = ["ROSE"]

def formaterAppellation(appellation, exclude_appellation):
    for valeur in exclude_appellation:
        if( appellation.find(valeur) > 0 ):
            appellation = ""

    return unidecode(appellation)

def formaterVin(appelation : str, vin : str, couleur : str):

    if( appelation != ""):
        vin :str = appelation + " " + vin

    vin = vin.upper()

    vin = supprimeChaineCaracteres(vin, tab_formater_vin)

    vin = vin.replace('"', '')
    vin = vin.replace("'", '')

    if( couleur != ""):
        vin :str = (vin + ' BLANC') if (couleur in tab_couleur_blanche) else (vin)
        vin :str = (vin + ' ROSE') if (couleur in tab_couleur_rose) else (vin)

    return vin

def formaterVinAnnee(vin : str):

    annee : str = "INDICE_ANNEE"
    
    tab_annee_trouver = re.findall(r"\d{4}", vin)

    if( len(tab_annee_trouver) > 0 ):

        index_vin : int = vin.find(tab_annee_trouver[0])

        annee = vin[index_vin:index_vin+4]

        vin = vin[0:index_vin-1]
    
    return [vin, annee]

# A utiliser !!!
tab_formater_prix = [" ", "€", "NONE"]

def formaterPrix(prix):

    if( prix is None ):
        return "0"

    prix = unidecode(repr(prix))

    # En le mettant cela n'écrit plus dans le fichier
    prix = prix.upper()

    prix = supprimeChaineCaracteres(prix , tab_formater_prix)
    
    # tester avec dewitt pour l'unicode()
    prix = prix.replace("'" , '')
    prix = prix.replace("\\U202F" , '')
    prix = prix.replace("EUR" , '')
    prix = prix.replace("." , ',')

    return prix

@DeprecationWarning
def formaterPrix3(prix : str):
    prix = unidecode(repr(str(prix)))
    prix = prix.upper()

    prix = supprimeChaineCaracteres(prix , tab_formater_prix)

    prix = prix.replace("'", '')
    prix = prix.replace(',','.')

    prix = prix.replace("\\U202F", '')

    return float(prix)

@DeprecationWarning
def formatterPrix2(prix :str):

    prix = prix.replace(" ", "")

    fPrix=repr(prix)
    fPrix=fPrix.replace('€','')
    fPrix=fPrix.replace("'","")
    fPrix=fPrix.replace("\\","")
    fPrix=fPrix.replace("u202f","")

    prix : str = unidecode(fPrix)
    prix=prix.replace('EUR','')
    prix=prix.replace('.',',')
    
    return prix

tab_formater_quantite = [" ", "<", ">", "+", "-", "\\U202F", "NOUSCONTACTER", "NOUSCONSULTER", "NA", "NONE"]

def formaterQuantite(quantite):

    if(quantite is None):
        return "0"

    quantite = unidecode(quantite).upper()
    quantite = supprimeChaineCaracteres(quantite, tab_formater_quantite)

    if(len(quantite) == 0):
        return "0"

    quantite = quantite.replace('ONREQUEST','0')

    return quantite

# Récupérer l'année en cours pour savoir si la date est en NV ?

NV = ['', '0', 'NV', 'NM', 'N', 'N,V,', 'N.V', 'N.V.', 'NONE', '-', '0000', '.0']
tab_formater_annee = ['(', ')', 'BATCH', 'DISG', ' ']

def formaterAnnee(annee : str):

    annee = annee.upper()

    if annee in NV:
        return 'NV'

    annee = supprimeChaineCaracteres(annee, tab_formater_annee)

    return annee

#Changement BT pour 70 !!  <- Mylène
BT = ['70CL', '0.7', '70']
#77 cl pour les champagnes
BO = ['73CL', '75CL', '77CL', '0.75', '75', '750', '750ML', 'BT.', 'BOUTEILLE', '76CL']
QUART = ['20']
DE = ['37.5CL', '37.5', '37,5', '0.375', '375', '375CL', '0.375CL', '1/2BT.', 'DEMI', '37.50CL']
#Changement CLJ pour 62 !! <- Mylène
CL = ['50CL', '0.5', '50']
CL_BIS = ['500']
CLJ = ['62CL']
L = ['100CL', '1000', '100']
# 1.75 pour les spiritueux
MG = ['150CL', '1.5', '1.5L', '150', 'MAG.', '1.75', 'MAGNUM', '1.50']
MG_BIS = ['1500', '1.5']
MJ = ['225CL', '225', '2250']
DM = ['300CL', '3', '3000', '300', '3L', 'D.MAG.', 'DMAG', 'DOUBLEMAGNUM']
JE = ['500CL', '5', '500', '5000', 'JERO.', 'JEROBOAM']
IM = ['600CL', '6', '600', '6000', 'IMPE.', '6L', 'IMPERIALE']
RE = ['450CL', '450', '4500']
SA = ['900CL', '9', 'SALM', '900', '9000', 'SALMANAZAR']
BA = ['1200CL', '12', '1200', '12000']
NA = ['1500CL','15', 'NABU', '1500', '15000', '15L']
ME = ['18', 'BALT', '1800', '18000']
BABY = ['27', '2700', '27000']

def formaterFormatBouteille(formatB : str):

    formatB = formatB.upper()
    formatB = formatB.replace(' ','')
    formatB = formatB.replace(',','.')

    # Voir s'il est possible d'avoir des 10,0 dans les formats ?
    if("," in formatB):
        formatB = formatB[0] + formatB[1 : (len(formatB))].replace("0", '')

    # Enlève les 0 à la fin
    if(formatB.isdigit()):
        formaB_nombre = float(formatB)

        if(formaB_nombre is not None):
            formaB_nombre = int(formaB_nombre)

        formatB = str(formaB_nombre)

    # print("-"+formatB+"-")

    # Amélioration : le metttre dans une fonction à part
    if formatB in BO:
        formatB='BO'
    elif formatB in QUART:
        formatB='1/4'
    elif formatB in DE:
        formatB='DE'
    elif formatB in CL:
        formatB='CL'
    elif formatB in CLJ:
        formatB='CLJ'
    elif formatB in BT:
        formatB='BT'
    elif formatB in L:
        formatB='L'
    elif formatB in MG:
        formatB='MG'
    elif formatB in MJ:
        formatB='MJ'
    elif formatB in DM:
        formatB='DM'
    elif formatB in JE:
        formatB='JE'
    elif formatB in IM:
        formatB='IM'
    elif formatB in RE:
        formatB='RE'
    elif formatB in SA:
        formatB='SA'
    elif formatB in BA:
        formatB='BA'
    elif formatB in NA:
        formatB='NA'
    elif formatB in ME:
        formatB='ME'
    elif formatB in BABY:
        formatB='BABY'
    else:
        return 'NON RECONNU'

    return formatB

def formaterFormatBouteilleBis(formatB : str):

    formatB = formatB.upper()
    formatB = formatB.replace(" ",'')

    # Voir s'il est possible d'avoir des 10,0 dans les formats ?
    if("," in formatB):
        formatB = formatB[0] + formatB[1 : (len(formatB))].replace("0", "")

    # Enlève les 0 à la fin
    if(formatB.isdigit()):
        formaB_nombre = float(formatB)

        if(formaB_nombre is not None):
            formaB_nombre = int(formaB_nombre)

        formatB = str(formaB_nombre)

    # Amélioration : le metttre dans une fonction à part
    if formatB in BO:
        formatB='BO'
    elif formatB in DE:
        formatB='DE'
    elif formatB in CL_BIS:
        formatB='CL'
    elif formatB in CLJ:
        formatB='CLJ'
    elif formatB in BT:
        formatB='BT'
    elif formatB in L:
        formatB='L'
    elif formatB in MG_BIS:
        formatB='MG'
    elif formatB in MJ:
        formatB='MJ'
    elif formatB in DM:
        formatB='DM'
    elif formatB in JE:
        formatB='JE'
    elif formatB in IM:
        formatB='IM'
        
    elif formatB in RE:
        formatB='RE'
    elif formatB in SA:
        formatB='SA'
    elif formatB in BA:
        formatB='BA'
    elif formatB in NA:
        formatB='NA'
    elif formatB in ME:
        formatB='ME'
    elif formatB in BABY:
        formatB='BABY'
    else:
        formatB='NON RECONNU'

    return formatB


verif_cdt_str : str = "Verif cdt : "

# Renvoi un conditionnement à partir de fonction avec un conditionnement vide et non-vide
def formaterConditionnement(formatB, quantite, conditionnement:  str, nom_vin):

    # print(" formatB : "+formatB)
    # print(" quantite : "+str(quantite))
    # print(" conditionnement : "+conditionnement)
    # print(" nom_vin: "+nom_vin)

    conditionnement = conditionnement.replace(" ", "")
    conditionnement = conditionnement.upper()

    if (conditionnement is None) or (len(conditionnement) == 0):

        # Attention tester si le conditionnement n'est pas dans le nom du vin avant de faire le conditionnement par défaut

        return conditionnementParDefaut(formatB, quantite)

    return conditionnementNonDefaut(formatB, quantite, conditionnement, nom_vin)

# Renvoi un conditionnement à partir d'un conditionnement non rempli
# A revoir !!
def conditionnementParDefaut(formatB, quantite):

    conditionnement = 'UNITE'

    if formatB == 'DE':
        if quantite > 24 :
            return 'CBO24DE'
            
        return conditionnement

    elif formatB == 'BO' or formatB == 'CL':
        if quantite > 12:
            return 'CBO12'

        return conditionnement

    elif formatB == 'MG' :
        if quantite > 6 :
            return 'CBO6'

        return conditionnement

    elif formatB == 'DM':
        if quantite > 3 :
            return 'CBO3'

        return conditionnement

    return 'CBO1'

UNITE : str = ['UNITE', 'LOOSE']
unite_str : str = 'UNITE'

# Méthode permettant de tester l'existance des valeurs d'un tableau dans une chaine de caractere
def existe(chaine_caractere : str, tableau):

    for cellule in tableau:
        return chaine_caractere.find(cellule)

# Renvoi un conditionnement à partir d'un conditionnement rempli
# A modifier !!
def conditionnementNonDefaut(formatB : str, quantite : int, conditionnement : str, nom_vin : str):

    # Conditionnement unité
    if((existe(conditionnement, UNITE)) != -1):
        return unite_str

    if(conditionnement in tab_conditionnement):
        return conditionnement

    # Conditionnement en partie définie
    if('CBO'in conditionnement):
        conditionnement = conditionnement.replace('CBO/','CBO')
        conditionnement = conditionnement.replace("X", '')

        tab_entier_conditionnement = re.findall(r"\d", conditionnement)

        return "CBO" + "".join(tab_entier_conditionnement);

    # Conditionnement éloigné
    conditionnement_simple : str = ""

    etui_str :str = "ETUI"
    gift_box_str :str = "GIFTBOX"
    caisse_str :str = "CAISSE"
    carton_str :str = "CARTON"
    coffret_str :str = "COFFRET"

    if nom_vin in tab_collection:
        return "COLLEC"

    if etui_str in conditionnement:
        return "ETUI1"

    if gift_box_str in conditionnement:
        return "GIBO1"

    conditionnement = conditionnement.replace("X", '')

    type_conditionnement : str

    # print('Passe 3 ')

    # fr ou an
    if (caisse_str in conditionnement) or ("CB" in conditionnement):

        type_conditionnement = caisse_str
        conditionnement_simple = "CB"
    
    elif (("OWC" in conditionnement) or ("OC" in conditionnement)) :
        if(conditionnement == "OC"):
            #return conditionnementParDefaut(formatB, quantite)
            return "CC" + str(chiffresConditionnement(conditionnement, "C"))

        return "CBO" + str(chiffresConditionnement(conditionnement, "C"))

    elif (carton_str in conditionnement) or ("CT" in conditionnement):

        type_conditionnement = carton_str
        conditionnement_simple = "CC"
 
    elif coffret_str in conditionnement:

        type_conditionnement = coffret_str
        # A modifier Cof en COF
        # return "Cof" + chiffresConditionnement(conditionnement, coffret_str)

        return "CF"+chiffresConditionnement(conditionnement, coffret_str)

    # Mis ici sinon il y a conflit avec les conditionnement commençant par 'CO'
    elif('CO'in conditionnement):
        conditionnement=conditionnement.replace('CO/','CC')
        return conditionnement;
    else: 

        # print('Passe 2')
        return unite_str

    conditionnement_simple = conditionnement_simple + prefixConditionnement(conditionnement) + str(chiffresConditionnement(conditionnement, type_conditionnement)) + suffixeConditionnement(conditionnement, quantite, formatB)

    # print('Passe 1 ')

    return conditionnement_simple

# Définit un prefix dans le conditionnement avant les chiffres
def prefixConditionnement(conditionnement):

    bois_str : str = "BOIS"
    orgine_str : str = "ORIGINE"
    neutre_str : str = "NEUTRE"

    # fr ou an
    # if (bois_str in conditionnement and orgine_str in conditionnement) or ("O" in conditionnement):
    #     return "O"

    if neutre_str in conditionnement:
        return "N"

    return "O"

# Récupération du premier chiffre après le type de conditionnement
def chiffresConditionnement(conditionnement, type_conditionnement):

    numbers = re.findall("\d+", conditionnement)


    if(len(numbers) == 0):
        return "1"

    # A revérifier !!! La ligne d'en haut a été modifié

    if( ("CAISSE" in conditionnement) or ("CARTON" in conditionnement)):

        if( conditionnement[0] == "1"):
            return numbers[1]
        return numbers[0]

    if( ("COFFRET" in conditionnement) ):

        if( conditionnement[0] == "1"):
            return "1"
        return numbers[0]
        
    # a revoir
    # numbers = [int(temp)for temp in conditionnement.split() if temp.isdigit()]

    return numbers[0]

# Rajouter si plusieurs millesimes à la suite
tab_collection = ["COLLECT", "PANACHEE", "VERTICALE", "CAISSEDUCLOT"]

# Définit un suffixe dans le conditionnement après les chiffres
def suffixeConditionnement(conditionnement, quantite, formatB):

    plat_str : str = "LAT"
    glissiere_str = "GLISSIERE"

    if ((plat_str in conditionnement) and (quantite >= 6)):
        return "PLA"

    if (formatB == 'DE') and (int(quantite) > 24):
        return 'DE'
        
    if glissiere_str in conditionnement :
        return "G"

    return ""

@DeprecationWarning
def formaterCommentaire(commentaire):
    return commentaire

@DeprecationWarning
def bLigneIncorrecte3(prix, quantite):
    if (len(prix) == 0 or len(quantite) == 0 or 
    prix=='PrixdeVente' or prix=='Price/Unit') :
        return True

    return False

@DeprecationWarning
def bLigneIncorrecte2(prix, designation_prix, chateau):
    if (len(prix) == 0 or len(chateau) == 0 or prix == designation_prix) :
        return True

    return False

# Le plus performant
def bLigneIncorrecte(prix, designation_prix, vin):
    if ((vin is None) or (prix is None) or (len(prix) == 0) or (prix == "NONE") or (len(vin) == 0) or (prix in designation_prix)) :
        return True

    return False

#A revoir
def tableau_ligne(tab_colonne, ws, i):
    
    tab_cell = []

    for index_colonne in range(len(tab_colonne)):
        tab_cell.extend(ws.cell(row = i, column = index_colonne).value)
        
    return tab_cell

def affectationLignes(j, ws, vin, millesime, formatB, prix, quantite, conditionnement, commentaire):
    c1 = ws.cell(row = j, column = 1)
    c1.value = vin

    c2 = ws.cell(row = j, column = 2)
    c2.value = millesime

    c3 = ws.cell(row = j, column = 3)
    c3.value = formatB

    c4 = ws.cell(row = j, column = 4)
    c4.value = prix

    c5 = ws.cell(row = j, column = 5)
    c5.value = quantite

    c6 = ws.cell(row = j, column = 6)
    c6.value = conditionnement

    c7 = ws.cell(row = j, column = 7)
    c7.value = commentaire

def affectationLignes2(j, ws, vin, millesime, formatB, prix, quantite, conditionnement, commentaire, typeTarif):
    c1 = ws.cell(row = j, column = 1)
    c1.value = vin

    c2 = ws.cell(row = j, column = 2)
    c2.value = millesime

    c3 = ws.cell(row = j, column = 3)
    c3.value = formatB

    c4 = ws.cell(row = j, column = 4)
    c4.value = prix

    c5 = ws.cell(row = j, column = 5)
    c5.value = quantite

    c6 = ws.cell(row = j, column = 6)
    c6.value = conditionnement

    c7 = ws.cell(row = j, column = 7)
    c7.value = commentaire

    c8 = ws.cell(row = j, column = 8)
    c8.value = typeTarif

# A revoir pour trouver une valeur d'une liste de liste
def testValeur(liste: list, valeurTestee, valeur_minimale : int):
    
    for i in range(valeur_minimale, len(liste)):

        indice = liste[i].index(valeurTestee)

        if(indice != -1):
            return indice

        # for valeur_liste in liste:

        #     if(valeurTestee == valeur_liste):
            
        #         print("cle : " + str (cle_tableau))
        #         # NA est la première valeur
        #         return cle_tableau + 1
    # Resultat : NA
    return 1

#Fonction de suppression des lignes vides d'un workbook
def suppressionLignesVidesWorkbook(ws):
    index_row = []

    for n in range(1, ws.max_row):
        if ws.cell(n, 1).value is None:
            index_row.append(n)

    for row_del in range(len(index_row)):
        ws.delete_rows(idx=index_row[row_del], amount=1)
        index_row = list(map(lambda k: k -1, index_row))

def testCommentaireParenthese(vin : str):

    commentaires : str = ""

    if( "(" in vin):
        indice_1 : int = vin.index('(')
        indice_2 : int = vin.index(')')

        # print(vin)
        # print(indice_1)
        # print(indice_2)

        commentaires = vin[indice_1 + 1 : indice_2]

        # print(commentaire)

        vin = vin[0 : indice_1 - 1 ]
        # print("-" + vin + "-")

    return [vin, commentaires]

# Essai non concluant de faire automatiquement le remplissage des tableau
# une fonction() : pour vin = sheet['A'] // dans REDCIR

# vin_str : str = "VIN"
# millesime_str : str = "MILLESIME"
# formatB_str : str = "FORMAT_BOUTEILLE"
# prix_str : str = "PRIX"
# quantite_str : str = "QUANTITE"
# conditionnement_str : str = "CONDITIONNEMENT"
# commentaire_str : str = "COMMENTAIRE"
# appellation_str : str = "APPELLATION"
# couleur_str : str = "COULEUR"
# regie_str : str = "REGIE"

# tab_designations_colonnes_par_defaut = [vin_str, millesime_str, formatB_str, prix_str, quantite_str, conditionnement_str]

# vin millesime formatB prix quantite conditionnement commentaire appellation couleur regie autre
# def formatterColonnesOnglets(dictionnaire_entree, sheet):

#     dataframe = pd.DataFrame()

#     for clef, valeur in dictionnaire_entree.items():

#         # Pour éviter les erreurs des valeurs vides, création de colonne vide
#         if(valeur == ""):
#             dataframe[clef]  = ""
#             continue

#         dataframe[clef] = sheet[valeur]

#     return dataframe