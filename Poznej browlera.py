
import random
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

import Blahoprani
import SeznamBrowleru
import Smajlik

def vypisRekordy() -> None:
    jmeno = input("\nZadej svoje jméno: ")
    soubor = "Rekordy.txt"
    souborZapis = open(soubor, mode="r+")
    obsah = souborZapis.read()
    souborZapis.writelines(f"\n{jmeno}, datum: {date.today()}, čas hry: {round((end - start),2)} ")
    souborZapis.close()
    souborZapis = open(soubor, mode="r")
    obsah = souborZapis.read()
    print(obsah)
    souborZapis.close()

def zjistiRekord(cislo: float) -> None:
    soubor = "Rekordy.txt"
    souborZapis = open(soubor, mode="r")
    obsah = souborZapis.readlines()
    obsah.remove("\n")
    for radek in obsah:
        rekord = True
        radek2 = radek.split(" ")
        if (float(radek2[len(radek2)-2])) < cislo:
            rekord = False
            break
    if rekord == True:
        print("\nVýborně, udělal jsi rekord!")
        Blahoprani.blahoprani()
    souborZapis.close()


brawler = random.choice(list(SeznamBrowleru.brawleri.keys()))
hledaneSlovo = brawler.lower()
hledaneSlovoSeznam = list(hledaneSlovo)
tajenka = (len(hledaneSlovoSeznam)*"_ ")
start = time.time()
print("""\nAhoj, vítej ve hře: Poznej brawlera
      \nPokus se uhádnout jméno brawlera, které je schované v následující tajence
      \nMáš 5 pokusů\n
      """)
print(f"{tajenka}")
hraPokracuje = True
pokusy = 5
while hraPokracuje and pokusy > 0 and "_" in tajenka:
    tip = input("\nZadej hledané písmeno. Pokud chceš využít nápovědu 1, zadej 1. Pokud chceš využít nápovědu 2, zadej 2: ").lower()
    if tip == "1":
       print(f"\nHledaný brawler je {SeznamBrowleru.brawleri[brawler]["napoveda1"]}")
    elif tip == "2":
       print(f"\nHledaný brawler patří do kategorie {SeznamBrowleru.brawleri[brawler]["napoveda2"]}")
    elif tip != "1" and tip != "2" and tip != "8" and tip.isalpha() == False:
       print("\nNeplatné zadání, zkus to příště")
       quit()
    elif tip.isalpha() or tip == "8":
        seznamIndexu = list()
        for pozice, pismeno in enumerate(hledaneSlovoSeznam):
            if pismeno == tip.lower():
                print("\nSprávně :)")
                seznamIndexu.append(pozice)
                for index in seznamIndexu:
                    tajenkaSeznam = list(tajenka)
                    for znak in tajenkaSeznam:
                        if znak == " ":
                            tajenkaSeznam.remove(znak)
                    if index == 0:       
                        tajenkaSeznam[index] = tip.upper()
                    elif index > 0:
                        tajenkaSeznam[index] = tip.lower()
                tajenka = " ".join(tajenkaSeznam)
        print(f"\n{tajenka}")
        if tip.lower() not in hledaneSlovoSeznam:
            pokusy -= 1
            if pokusy == 4 or pokusy == 3 or pokusy == 2:
                print(f"Vedle...zbývají ti ještě {pokusy} pokusy")
            elif pokusy == 1:
                print("Zbývá ti poslední pokus")
end = time.time()
print(f"""
      \nDíky za hru :)
      \nHra ti trvala {round((end - start),2)} sekund
      \n\nPokud se chceš dozvědět něco o brawlerovi, kterého jméno jsi hádal, klikni na: {SeznamBrowleru.brawleri[brawler]["odkaz"]}\n""")
driver = webdriver.Chrome() 
driver.get(f"{SeznamBrowleru.brawleri[brawler]["odkaz"]}")

if pokusy > 0:
    volba = input("Chceš zapsat svůj výkon do tabulky rekordů (ano/ ne): ")
    if volba == "ano":
        zjistiRekord(round((end - start),2))
        vypisRekordy()

  
Smajlik.nakresliSmajlika()

