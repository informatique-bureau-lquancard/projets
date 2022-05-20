import csv
import glob
import re
import io
import time
from unidecode import unidecode
from lxml import etree
import sys
import xml.etree.ElementTree as ET
# coding: utf-8

tree = etree.parse("http://admin.millesima.fr/media/productsfeedpick/fr.xml")

Vin = etree.Element("Produit")

nom_sortie='sortie_MILIMA.csv'

dCond = ["CBO12","CBO6","CBO4","CBO3","CBO2","CBO1","CBO24","CBO24DE","CC12","CC6","CC4","CC3","CC2","CC1","CC24","UNITE"]

with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
    writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')

    for Vin in tree.xpath("/XMLFILE/Produit") :
        chateau = unidecode(Vin[0].text)
        couleur = Vin[4].text

        if couleur == "Blanc" :
            chateau = chateau[:-5]+ ' blanc'
        else:
            chateau = unidecode(chateau[:-5])

        chateau = chateau.replace('"','')
        chateau = chateau.replace(',','')


        iMill = Vin[1].text
        if iMill == '0000' :
            millesime = 'NV'
        else:
            millesime = iMill





        Contenant = Vin[9].text
        if Contenant == "750" :
            formatb = "BO"
        elif Contenant == "1500" :
            formatb = "MG"
        elif Contenant == "3000" :
            formatb = "DM"
        elif Contenant == "375" :
            formatb = "DE"
        elif Contenant == "5000" :
            formatb = "JE"
        elif Contenant == "4500" :
            formatb = "RE"
        elif Contenant == "6000" :
            formatb = "IM"
        elif Contenant == "9000" :
            formatb = "SA"
        elif Contenant == "12000" :
            formatb = "BA"
        elif Contenant == "15000" :
            formatb = "NA"
        elif Contenant == "18000" :
            formatb = "ME"
        elif Contenant == "27000" :
            formatb = "BABY"

        qCaisse = Vin[18].text
        iNb = qCaisse.find("*")
        qCaisse = qCaisse[:int(iNb)].replace(" ","")

        fprix = Vin[7].text
        fprix = float(fprix) / int(qCaisse)
        prix = str(fprix)
        prix = prix.replace(".",",")



        quantite = Vin[17].text

        Cond = Vin[10].text
        if "caisse de" in Cond :
            iCond=Cond.find("caisse de")
            Cond=Cond[int(iCond):]
            conditionnement="CBO"+Cond[9:12]
        elif "carton de" in Cond :
            conditionnement="CC"+Cond[13:15]
        else:
            conditionnement="UNITE"

        conditionnement=conditionnement.replace(" ","")

        if conditionnement=="CBO24" and formatb=="DE" :
            newCond="CBO24DE"
            commentaire = ""
        elif conditionnement not in dCond :
            newCond="UNITE"
            commentaire="VERIF CDT - "+conditionnement
        else:
            newCond=conditionnement
            commentaire=""

        newRow=[chateau,millesime,formatb,prix,quantite,newCond,commentaire]
        writer.writerow(newRow)
