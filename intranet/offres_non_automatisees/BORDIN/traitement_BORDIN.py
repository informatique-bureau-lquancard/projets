import csv
import glob
import re
# coding: utf-8

for filename in glob.glob('*.csv'):
    with open(filename, newline='', encoding='utf-8') as monFichierEntre:
        dialect = csv.Sniffer().sniff(monFichierEntre.read(1024))
        monFichierEntre.seek(0)
        reader = csv.reader(monFichierEntre, dialect)
        #reader = csv.reader(monFichierEntre, delimiter=';', doublequote=False)
        nom_sortie='sortie_BORDIN.csv'
        with open(nom_sortie,'w',newline='', encoding='utf-8') as monFichierSortie:
            writer = csv.writer(monFichierSortie, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=';', quotechar='')
            enTete = ['Vin','Millesime','Format','Offer','Quantite','Conditionnement','Commentaire']
            writer.writerow(enTete)

            for row in reader:
                if 'Vintage' in row[0]:
                    bEcrire = 0
                else:
                    bEcrire = 1

                    VinMill = row[1]
                    Millesime = re.findall('[0-9][0-9][0-9][0-9]',VinMill)[0]
                    Vin = VinMill.replace(Millesime,'').strip()
                    Formatb = 'BO'
                    Offer = re.findall('[\d,.-]+',row[5])[0]
                    Offer = Offer.replace(',','')
                    Offer = Offer.replace('--','0')
                    quantite = '0'
                    conditionnement = 'CBO12'
                    Bid = re.findall('[\d,.-]+',row[4])[0]
                    Bid = Bid.replace(',','')
                    Trade = re.findall('[\d,.-]+',row[8])[0]
                    Trade = Trade.replace(',','')
                    commentaire = 'Bid : '+Bid+' - Last Trade : '+Trade



                # On fabrique la nouvelle ligne dans l'ordre voulu
                if bEcrire == 1 :
                    newRow=[Vin,Millesime,Formatb,Offer,quantite,conditionnement,commentaire]
                    writer.writerow(newRow)
        monFichierEntre.close()
