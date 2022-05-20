from unidecode import unidecode

import time

import re

#fichierFonction_blqa version 1.01

# Mise en forme des différentes appelations des vins de Bordeaux
tab_appelation_bdx = ['AMIOT-SERVELLE', 'BARSAC', 'BORDEAUX', 'BORDEAUX SEC', 'FRANCS-COTES-DE-BORDEAUX', 'MARGAUX', 'MEDOC', 'MOULIS', 'PAUILLAC',
                'PESSAC-LEOGNAN', 'POMEROL', 'SAINT-EMILION', 'SAINT-EMILION GRAND CRU', 'SAINT-JULIEN', 'SAINT-ESTEPHE', 
                'SAUTERNES']

tab_conditionnement = ["UNITE","CC1","CC2","CC3","CC4","CC6","CC12","CC24","CC24DE","CBO1","CBO2","CBO3","CBO4","CBO6","CBO12","CBO24","CBO24DE","COLLEC", "CB1", "CB3", "CB6", "CB12"]

def formatterPrix(prix):

    prix = prix.replace(" ", "")

    fPrix=repr(prix)
    fPrix=fPrix.replace('€','')
    fPrix=fPrix.replace("'","")
    fPrix=fPrix.replace("\\","")
    fPrix=fPrix.replace("u202f","")

    prix=unidecode(fPrix)
    prix=prix.replace('EUR','')
    prix=prix.replace('.',',')
    
    return prix

def formatterQuantite(quantiteBis):

    if(len(quantiteBis) == 0):
        return "0"

    quantite = quantiteBis.upper()
    quantite = quantite.replace('ONREQUEST','0')
    quantite = quantite.replace('<','')
    quantite = quantite.replace('>','')

    return quantite

# Récupérer l'année en cours pour savoir si la date est en NV ?

def formatterAnnee(annee):
    if  annee == '' or annee == '0' or annee == 'NV' or annee == 'NM':
        return 'NV'

    return annee

#Changement BT pour 70 !!  <- Mylène
BT = ['70CL']
#77 cl pour les champagnes
BO = ['75CL', '77CL', '0,75', '75']
DE = ['37,5CL', '0,375']
#Changement CLJ pour 62 !! <- Mylène
CL = ['50CL', '0,5']
CLJ = ['62CL']
L = ['100CL']
MG = ['150CL', '1,5']
MJ = ['225CL']
DM = ['300CL', '3']
JE = ['500CL', '5']
IM = ['600CL', '6']
RE = ['450CL']
SA = ['900CL', '9', 'SALM']
BA = ['1200CL']
NA = ['1500CL','15', 'NABU']
ME = ['18', 'BALT']
BABY = ['27']

def formatterFormatBouteille2(formatB):

    formatB = formatB.upper()
    formatB = formatB.replace(" ","")

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
        formatB='NON RECONNU'

    return formatB

def formatterFormatBouteille(formatB):
    # Amélioration : le metttre dans une fonction à part
    if formatB=='62 cl' or formatB=='70 cl' or formatB=='75 cl' or formatB=='0,75':
        formatB='BO'
    elif formatB=='37,5 cl' or formatB=='0,375':
        formatB='DE'
    elif formatB=='150 cl' or formatB=='1,5' or formatB=='1,50':
        formatB='MG'
    elif formatB=='300 cl' or formatB=='3' or formatB=='3,00':
        formatB='DM'
    elif formatB=='500 cl'or formatB=='5' or formatB=='5,00':
        formatB='JE'
    elif formatB=='600 cl' or formatB=='6' or formatB=='6,00':
        formatB='IM'
        
    elif formatB=='450 cl':
        formatB='RE'
    elif formatB=='9' or formatB=='9,00':
        formatB='SA'
    elif formatB=='15' or formatB=='15,00':
        formatB='NA'
    elif formatB=='18' or formatB=='18,00':
        formatB='BA'
    elif formatB=='27' or formatB=='27,00':
        formatB='BABY'
    else:
        formatB='NON RECONNU'

    return formatB

# Renvoi un conditionnement à partir de fonction avec un conditionnement vide et non-vide
def formatterConditionnement(formatB, quantite, conditionnement, nom_vin):

    conditionnement = conditionnement.replace(" ", "")
    conditionnement = conditionnement.upper()

    print(" ")
    print("formatB : "+formatB)
    print("quantite"+str(quantite))
    print("conditionnement : "+conditionnement)
    print("nom_vin  : "+nom_vin)

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

# Renvoi un conditionnement à partir d'un conditionnement rempli
# A modifier !!
def conditionnementNonDefaut(formatB, quantite, conditionnement, nom_vin):

    # Conditionnement en partie définie
    if('CBO'in conditionnement):
        conditionnement=conditionnement.replace('CBO/','CBO')
        return conditionnement;

    # Conditionnement éloigné
    conditionnement_simple : str = ""

    etui_str :str = "ETUI"
    gift_box_str :str = "GIFTBOX"
    caisse_str :str = "CAISSE"
    carton_str :str = "CARTON"
    coffret_str :str = "COFFRET"

    if nom_vin in tab_collection:
        print("COLLEC")
        return "COLLEC"

    if etui_str in conditionnement:
        print("ETUI1")
        return "ETUI1"

    if gift_box_str in conditionnement:
        print("GIBO1")
        return "GIBO1"

    type_conditionnement : str

    if caisse_str in conditionnement:
        print(caisse_str)
        type_conditionnement = caisse_str
        conditionnement_simple = "CB"

    elif carton_str in conditionnement:
        print(carton_str)
        type_conditionnement = carton_str
        conditionnement_simple = "CC"
 
    elif coffret_str in conditionnement:
        print(coffret_str)
        type_conditionnement = coffret_str
        # A modifier Cof en COF
        # return "Cof" + chiffresConditionnement(conditionnement, coffret_str)

        return "CF"+chiffresConditionnement(conditionnement, coffret_str)

    # Mis ici sinon il y a conflit avec les conditionnement commençant par 'CO'
    elif('CO'in conditionnement):
        conditionnement=conditionnement.replace('CO/','CC')
        return conditionnement;
    else: 
        return "UNITE"

    conditionnement_simple = conditionnement_simple + prefixConditionnement(conditionnement) + str(chiffresConditionnement(conditionnement, type_conditionnement)) + suffixeConditionnement(conditionnement, quantite, formatB)

    return conditionnement_simple

    return "UNITE"

# Définit un prefix dans le conditionnement avant les chiffres
def prefixConditionnement(conditionnement):

    bois_str : str = "BOIS"
    orgine_str : str = "ORIGINE"
    neutre_str : str = "NEUTRE"

    if bois_str in conditionnement and orgine_str in conditionnement:
        return "O"

    if neutre_str in conditionnement:
        return "N"

    return ""

# Récupération du premier chiffre après le type de conditionnement
def chiffresConditionnement(conditionnement, type_conditionnement):
    
        print(conditionnement)

        i_cond = conditionnement.index(type_conditionnement)
        print("i_cond : "+ str(i_cond))
        print(len(conditionnement) - 1)

        conditionnement_sans_chiffre = conditionnement[i_cond:len(conditionnement) - 1]

        print("conditionnement_sans_chiffre : "+conditionnement_sans_chiffre)

        numbers = re.findall("\d+", conditionnement)

        # numbers = [int(temp)for temp in conditionnement.split() if temp.isdigit()]

        print(numbers)
        print("numbers[0] : "+str(numbers[0]))

        return numbers[0]

# Rajouter si plusieurs millesimes à la suite
tab_collection = ["COLLECT", "PANACHEE", "VERTICALE", "CAISSEDUCLOT"]

# Définit un suffixe dans le conditionnement après les chiffres
def suffixeConditionnement(conditionnement, quantite, formatB):

    plat_str : str = "PLAT"
    glissiere_str = "GLISSIERE"

    if (plat_str in conditionnement) and (quantite == 6):
        return "PLA"

    if (formatB == 'DE') and (int(quantite) > 24):
        return 'DE'
        
    if glissiere_str in conditionnement :
        return "G"

    return ""

@DeprecationWarning
def formatterCommentaire(commentaire):
    return commentaire

def bLigneIncorrecte(prix, quantite):
    if (len(prix) == 0 or len(quantite) == 0 or 
    prix=='PrixdeVente' or prix=='Price/Unit') :
        return True

    return False

#A revoir
def tableau_ligne(tab_colonne, ws, i):
    
    tab_cell = []

    for index_colonne in range(len(tab_colonne)):
        tab_cell.extend(ws.cell(row = i, column = index_colonne).value)
        
    return tab_cell



