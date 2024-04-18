# Szálloda Foglalási Rendszer

Ez a Szálloda Foglalási Rendszer egy Python-ban írt alkalmazás, amely lehetővé teszi a felhasználók számára, hogy szállodákat és szobákat hozzanak létre, valamint foglalásokat hozzanak létre és mondjanak le.

## Használat

A program két fő részből áll:

1. **Adatfeltöltési prompt**:
   - A program elején a felhasználónak lehetősége van új szállodák és szobák hozzáadására.
   - A felhasználónak meg kell adnia a szálloda nevét, majd a hozzá tartozó szobák számát.
   - A szobák típusa (egy- vagy kétágyas) automatikusan meghatározásra kerül a szobaszám alapján.
   - A feltöltés a felhasználó által megadott adatok beolvasásával folytatódik, amíg a felhasználó "enter" gombbal nem fejezi be.

2. **Foglaló prompt**:
   - Miután a szállodák és szobák feltöltése megtörtént, a program a foglaló promptba lép.
   - A felhasználó itt választhat a következő lehetőségek közül:
     1. Szoba foglalása
     2. Szoba foglalás lemondása
     3. Foglalások listázása
     4. Kilépés
   - A foglalás során a felhasználónak meg kell adnia a szálloda nevét, a szoba számát és a foglalás dátumát.
   - A lemondás során a felhasználónak meg kell adnia a szálloda nevét, a szoba számát és a foglalás dátumát.
   - A foglalások listázása során a program kilistázza az aktuális foglalásokat.

## Adatstruktúra

A program a következő fő osztályokat használja:

- `Szoba`: Az egy- és kétágyas szobák absztrakt osztálya, amely a szoba árát határozza meg.
- `EgyAgyasSzoba` és `KetAgyasSzoba`: A `Szoba` osztály konkrét implementációi.
- `Szalloda`: A szállodák osztálya, amely a szálloda nevét és a hozzá tartozó szobákat tárolja.
- `Foglalas`: A foglalások osztálya, amely a szállodát, a szobát és a foglalás dátumát tárolja.
- `FoglalasiRendszer`: A fő osztály, amely a szállodákat, a szobákat és a foglalásokat kezeli.

## Működés

A program a következő lépéseket követi:

1. Alapértelmezett szálloda és szobák hozzáadása a `FoglalasiRendszer`-hez.
2. Alapértelmezett foglalások hozzáadása a `FoglalasiRendszer`-hez.
3. Felhasználói adatbekérés a szállodák és szobák hozzáadására.
4. Foglaló prompt megjelenítése, ahol a felhasználó választhat a különböző lehetőségek közül.

## Használati példa

```
Üdv a feltöltési promptban! Adja meg a szállodákat és szobákat.
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): Hotel A
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 101
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 102
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): Hotel B
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 201
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 202
Adja meg a szoba számát (nebo 'enter' a következő szállodához): 
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): 

Adatok feltöltve. Üdv a foglaló promptban!

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 1
Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): 2024-06-15
Foglalható szobák 2024-06-15 dátumra:
Szálloda: Hotel A
  Szoba: 101, Típus: Egyágyas, Ár: 10000 Ft
  Szoba: 102, Típus: Kétágyas, Ár: 15000 Ft
Szálloda: Hotel B
  Szoba: 201, Típus: Egyágyas, Ár: 10000 Ft
  Szoba: 202, Típus: Kétágyas, Ár: 15000 Ft

Adja meg a szálloda nevét: Hotel A
Adja meg a szoba számát: 102
Foglalás létrehozva. Ár: 15000 Ft

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 3
Szálloda: Hotel A, Szoba: 102, Dátum: 2024-06-15

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 4
Köszönjük, hogy használta a foglalási rendszert. Viszontlátásra!
```
