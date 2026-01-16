from algemene_functies import mijn_functie2

def aanbieding_1(smaak,prijs,korting):
    nw_prijs = prijs*(1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nw_prijs} euro"
    return uitvoer

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    uitvoer2 = f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer2

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer3 = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer3

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer4 = mijn_functie2(korte_lijst[0],korte_lijst[1])
    return uitvoer4