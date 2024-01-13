# RFT Projekt 
# Követelményspecifikáció

## 1. Jelenlegi helyzet leírása
## 2.Vágyálom rendszer leírása
## 3.A rendszerre vonatkozó pályázat
## 4.Jelenlegi üzleti folyamatok modellje
## 5.Igényelt üzleti folyamatok modellje
#### 5.1 Üzleti szereplők
A rendszerben nem különböztetünk meg külön felhasználó szinteket és jogosultsági szinteket sem. 
Bárki számára, aki futtaja a programot elérhetővé válik a számológép és a mértékegység átváltó egyaránt.
#### 5.2 Üzleti folyamatok
A felhasználók a képernyő terven is látható módon a megfelelő menüpont kiválasztásával tudják elérni külön-külön
a két funkciót mely új ablakon nyílik meg. A számológép alkalmazásban egy általános számológéphez hasonlóan
egyszerű matematikai műveleteket tudnak végrehajtani. A mértékegység átváltóban először kiválasztjuk melyik mérték-ben 
szeretnénk SI- egységeket átváltani egy másik SI mértékegységre. Minden esetben az alpalmazás az átváltóban és a számológép
esetében is figyeli a nem megfelelő beviteli értékeket valamit a helytelen műveletek végrehajtását. pl(0-val való osztás, 0 érétk átváltása.)
## 6.Követelménylista
#### 6.1 Funkcionális követelmények
##### Számológép:
* A számológép alkalmazásban a felhasználók számára legyen adott az **összeadás**, **kivonás**, **szorzás**, **osztás**, **gyökvonás**
funkciók használata. 
* Az alkalmazásban legyenek adottak a megfelelő beviteli gombok melyek segítségével használhatóak a különböző
funkciók és az arab számok 0-9-ig. Ezt követően jelenítse meg a kiszámított értéket.
* Képes legyen negatív számok előjeles megadására is.
* Hasonlóképpen egy hagyományos kézi számológéphez lehessen a képernyőt törölni a **CE** gomb segítségével.
##### Mértékegység átváltó:
* A mértékegység átváltó program képes legyen a **tömeg**, **térfogat** és **súly** mértékek átváltására.
* Tömeg esetében váltson **qramm**, **dekagramm**, **kilógramm**, **tonna** egységek között.
* Térfogat esetében váltson **mililiter**, **centiliter**, **deciliter**, **liter**, **hektoliter** és **köbméter** egységek között.
* Hosszúság esetében legyen képes kezelni a **milliméter**, **centiméter**, **deciméter**, **méter**, **kilóméter**, **mérföld** egységek közötti váltásokat.
#### 6.2 Nem funkcionális követelmények
A fejelsztésre kerülő szoftver a potenciális felhasználók számára könnyen tanulható és használható, minimális informatikai tudással alkalmazható. 
A program Windows platformra könnyen integrálható legyen.
## 7.(Irányított és szabad szöveges riportok szövege)
#### 7.1 Szabad riport:
* Felkérem Tatár Tamást és Dobi Antal szoftverfejlesztőket hogy a Mágikus Calculátorok kft nevében fejlesszenek egy olyan
multifunkcionális kalkulátort, melyben elérhetővé válik egy egyszerű szűmológép. A számológép képes legyen az egyszerű aritmetikai
műveletek mellett pl:(összeadás, kivonás, szorzás, osztás) a gyökvonásra is. Könnyen használható egyszerű designú szoftvert szeretnénk.
A számológéő mellett az első fázisban tartalmazzon a termék egy mértékegység átváltó almodult is. Ebben lehetősg legyen a tömeg, térfogat és 
távolság értékek átváltásában.

#### 7.2 Irányított riport:
* Asztali vagy webes felületen használható alkalmazásban gondolkodnak?  
_\Asztali alkalmazást szeretnénk/_
* A kinézet szempontjából milyen színvilágot valósítsunk meg?  
_\Egyszerű a szemnek kellemes pasztel színek alkamazását szeretnénk./_
* A mértékegység átváltó modulban milyen SI mértékegységek között legyen lehetőség az átváltásra?  
_\Tömeg esetén (g, dkg, kg, tonna), Térfogat esetén (ml, cl, dl, l, hl, m^3)/,
Távolság (mm, cm, dm, m, km, miles)/_
* A további bővíthetőség miatt megfelelő lenne-e esetleg egy alap belépőoldal és ebből leágazó almodulok megvalósítása?  
_\Igen fő szempont, hogy később bővíthető lehessen./_
* A mértékegység átváltóban a kiválasztható elemek legördülő menüből választhatóak legyenek vagy chckbox-os megoldást esetleg más alternatív lehetőséget alkalmazzunk?  
_\A legördülő menü szimpatikus és egyszűrenk tűnik. Megfelelő lesz./_

## 8.Fogalomszótár.

