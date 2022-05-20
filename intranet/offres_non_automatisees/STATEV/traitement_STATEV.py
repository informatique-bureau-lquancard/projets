## coding: utf-8
import csv
import glob
import re
import io
import time
from unidecode import unidecode


for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_STATEV.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='|', quotechar='')

            index=0
            iAcheteur=""
            iVendeur=""
            iDate=""
            
            trou='' # besoin de le faire une seule fois
            
            for row in reader:
                bEcrire=0
                if row[5]=="2":
                    index=1
                    iAcheteur=row[2]
                    iVendeur=row[3]
                    iDate=row[1]
                    iApporteur=row[7]
                    iRealisateur=row[8]
                    iOperateur=row[9]
                    iFlux=row[10]
                    bEcrire=0
                elif row[5]=="Courtage (%)":
                    index=2
                    acheteur="Acheteur"
                    vendeur="Vendeur"
                    date="Date"
                    courtage="Courtage (%)"
                    vin="Vin"
                    quantite="Quantite"
                    formatb="Format"
                    facturation="Facturation"
                    app="Appellation"
                    apporteur="Apporteur"
                    realisateur="Realisateur"
                    operateur="Operateur"
                    flux="Flux"
                    transaction="Transaction"
                    bEcrire=1
                else:
                    bEcrire=1 
                    if index==1:
                        acheteur=iAcheteur
                        vendeur=iVendeur
                        date=iDate
                        courtage=row[5]
                        vin=row[3]
                        quantite=row[1]
                        formatb=row[2]
                        facturation=row[4]
                        app=row[7]
                        apporteur=iApporteur
                        realisateur=iRealisateur
                        operateur=iOperateur
                        flux=iFlux
                        transaction=unidecode(row[8])

                # écriture de la ligne
                if bEcrire==1 :
                    newRow=[acheteur,vendeur,date,vin,quantite,formatb,courtage,facturation,app,apporteur,realisateur,operateur,flux,transaction,trou,trou,trou]
                    writer.writerow(newRow)            
            monFichierEntre.close()