#####################################################
#                                                   #
#        Contact: @ba1int                           #
#        Date: 2024-04-18                           #
#                                                   #
#####################################################

from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam):
        self.szobaszam = szobaszam

    @abstractmethod
    def ar(self):
        pass

class EgyAgyasSzoba(Szoba):
    def ar(self):
        return 10000

class KetAgyasSzoba(Szoba):
    def ar(self):
        return 15000

class Szalloda:
    def __init__(self, szalloda_nev):
        self.szalloda_nev = szalloda_nev
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szalloda, szoba, datum):
        self.szalloda = szalloda
        self.szoba = szoba
        self.datum = datum

    def ar(self):
        return self.szoba.ar()

class FoglalasiRendszer:
    def __init__(self):
        self.szallodak = []
        self.foglalasok = []

    def _foglalas_kereses(self, szalloda_nev, szobaszam, datum):
        szalloda = self._szalloda_kereses(szalloda_nev)
        if szalloda is None:
            return None

        szoba = self._szoba_kereses(szalloda, szobaszam)
        if szoba is None:
            return None

        for foglalas in self.foglalasok:
            if foglalas.szalloda == szalloda and foglalas.szoba == szoba and foglalas.datum == datum:
                return foglalas

        return None
    def szalloda_hozzaadasa(self, szalloda):
        self.szallodak.append(szalloda)

    def szoba_foglalas(self, szalloda_nev, szobaszam, datum):
        szalloda = self._szalloda_kereses(szalloda_nev)
        if szalloda is None:
            print("Nem található szálloda ezzel a névvel.")
            return

        szoba = self._szoba_kereses(szalloda, szobaszam)
        if szoba is None:
            print("Nem található szoba ezzel a számmal.")
            return

        if not self._datum_ellenorzes(datum):
            print("Érvénytelen dátum. A dátumnak jövőbelinek kell lennie.")
            return

        if self._foglalt_e(szalloda, szoba, datum):
            print("A szoba már foglalt erre a dátumra.")
            return

        foglalas = Foglalas(szalloda, szoba, datum)
        self.foglalasok.append(foglalas)
        print(f"Foglalás létrehozva. Ár: {foglalas.ar()} Ft")

    def foglalas_lemondasa(self, szalloda_nev, szobaszam, datum):
        foglalas = self._foglalas_kereses(szalloda_nev, szobaszam, datum)
        if foglalas is None:
            print("Nem található foglalás ezekkel az adatokkal.")
            return

        self.foglalasok.remove(foglalas)
        print("Foglalás sikeresen lemondva.")

    def foglalasok_listazasa(self):
        if len(self.foglalasok) == 0:
            print("Nincsenek foglalások.")
            return

        for foglalas in self.foglalasok:
            print(f"Szálloda: {foglalas.szalloda.szalloda_nev}, Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

    def foglalhato_szobak_listazasa(self, datum):
        print(f"Foglalható szobák {datum} dátumra:")
        for szalloda in self.szallodak:
            print(f"Szálloda: {szalloda.szalloda_nev}")
            for szoba in szalloda.szobak:
                if not self._foglalt_e(szalloda, szoba, datum):
                    print(
                        f"  Szoba: {szoba.szobaszam}, Típus: {'Kétágyas' if isinstance(szoba, KetAgyasSzoba) else 'Egyágyas'}, Ár: {szoba.ar()} Ft")
            print()
    def _szalloda_kereses(self, szalloda_nev):
        for szalloda in self.szallodak:
            if szalloda.szalloda_nev == szalloda_nev:
                return szalloda
        return None

    def _szoba_kereses(self, szalloda, szobaszam):
        for szoba in szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba
        return None

    def _datum_ellenorzes(self, datum):
        mai_datum = datetime.now().date()
        return datum >= mai_datum

    def _foglalt_e(self, szalloda, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szalloda == szalloda and foglalas.szoba == szoba and foglalas.datum == datum:
                return True
        return False

# Példa használat
foglalasi_rendszer = FoglalasiRendszer()

# Alapértelmezett szálloda és szobák hozzáadása
alap_szalloda = Szalloda("0")
alap_szalloda.szoba_hozzaadasa(EgyAgyasSzoba(201))
alap_szalloda.szoba_hozzaadasa(KetAgyasSzoba(102))
alap_szalloda.szoba_hozzaadasa(EgyAgyasSzoba(303))
foglalasi_rendszer.szalloda_hozzaadasa(alap_szalloda)

# Alapértelmezett foglalások hozzáadása
foglalasi_rendszer.szoba_foglalas("0", 201, datetime(2024, 6, 15).date())
foglalasi_rendszer.szoba_foglalas("0", 102, datetime(2024, 6, 20).date())
foglalasi_rendszer.szoba_foglalas("0", 303, datetime(2024, 6, 25).date())
foglalasi_rendszer.szoba_foglalas("0", 201, datetime(2024, 7, 1).date())
foglalasi_rendszer.szoba_foglalas("0", 102, datetime(2024, 7, 5).date())

# Felhasználói adatbekérés
print("\nÜdv a feltöltési promptban! Adja meg a szállodákat és szobákat.")
while True:
    szalloda_nev = input("Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): ")
    if szalloda_nev == "":
        break

    szalloda = Szalloda(szalloda_nev)

    while True:
        szobaszam = input("Adja meg a szoba számát (vagy 'enter' a következő szállodához): ")
        if szobaszam == "":
            break

        szobaszam = int(szobaszam)
        if szobaszam % 2 == 0:
            szoba = KetAgyasSzoba(szobaszam)
        else:
            szoba = EgyAgyasSzoba(szobaszam)

        szalloda.szoba_hozzaadasa(szoba)

    foglalasi_rendszer.szalloda_hozzaadasa(szalloda)

print("Adatok feltöltve. Üdv a foglaló promptban!")

# Foglaló prompt
while True:
    print("\nVálasszon az alábbi lehetőségek közül:")
    print("1. Szoba foglalás")
    print("2. Szoba foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Adja meg a választását (1-4): ")

    if valasztas == "1":
        datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        foglalasi_rendszer.foglalhato_szobak_listazasa(datum)

        szalloda_nev = input("Adja meg a szálloda nevét: ")
        szobaszam = int(input("Adja meg a szoba számát: "))
        foglalasi_rendszer.szoba_foglalas(szalloda_nev, szobaszam, datum)
    elif valasztas == "2":
        szalloda_nev = input("Adja meg a szálloda nevét: ")
        szobaszam = int(input("Adja meg a szoba számát: "))
        datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        foglalasi_rendszer.foglalas_lemondasa(szalloda_nev, szobaszam, datum)
    elif valasztas == "3":
        foglalasi_rendszer.foglalasok_listazasa()
    elif valasztas == "4":
        print("Köszönjük, hogy használta a foglalási rendszert. Viszontlátásra!")
        break
    else:
        print("Érvénytelen választás. Kérjük, próbálja újra.")
