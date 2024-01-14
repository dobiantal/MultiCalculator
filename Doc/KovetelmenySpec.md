# RFT Projekt 
# Követelményspecifikáció

## 1. Jelenlegi helyzet leírása
A Kartal település önkormányzata örömmel tudatja, hogy sikeresen pályázatot nyert az informatikai eszközök cseréjére és a 
használt szoftverek korszerűsítésére. Ezen nagyszerű lehetőség kapcsán a kartali önkormányzat beszerzésért felelős munkatársa
felkeresett azzal a jó hírrel, hogy cégünknek kellene fejleszteni egy olyan programot ami megoldást nyújt nekik a jelenlegi
munkafolyamataik során leggyakrabban előforduló hibák csökkentésére. Ezzeket a hibákat a manuális számolások és az átváltások okozzák
Ennek megoldása érdekében az önkormányzat elkötelezett a modern informatikai eszközök bevezetése mellett, 
melyek segítségével hatékonyabban és hibamentesebben végezhetik el mindennapi tevékenységeiket. 
## 2.Vágyálom rendszer leírása
A célunk egy rendkívül komplex szoftver megalkotása, amely két különleges opciót kínál a dolgozóknak,
ezáltal maximális funkcionalitást és kényelmet biztosítva. Az első opció egy magas szintű számológép,
amely minden olyan matematikai művelettel rendelkezik, amelyre a dolgozóknak szüksége van a mindennapi 
tevékenységeik során. A program egyszerű és felhasználóbarát felülettel rendelkezik, amely lehetővé teszi
az egyszerű összeadást, kivonást, osztást, szorzást és gyökvonást. Ennek a matematikai opciónak az a célja,
hogy a felhasználók könnyen és hatékonyan tudjanak számolni a mindennapi munkafolyamataik során.

A második opció egy speciális felületet kínál a mértékegység-átváltáshoz. Ezen a platformon a dolgozók
kiválaszthatják, hogy milyen területen szeretnének átváltást készíteni. 
Az átváltás három kulcsfontosságú területet foglal magában: Hosszúság, Tömeg és Térfogat.

#### Hosszúság:

* A program lehetővé teszi a milliméter, centiméter, deciméter, méter, kilóméter és mérföld egységek közötti pontos és megbízható átváltást.

#### Tömeg:

* Ezen felül a Tömeg opcióban a rendszer lehetővé teszi a qramm, dekagramm, kilógramm és tonna egységek közötti váltást is.

#### Térfogat:

* A térfogatnál a program támogatja a mililiter, centiliter, deciliter, liter, hektoliter és köbméter egységek közötti átváltást.

Ez a rendkívül sokoldalú szoftver nem csupán egy egyszerű eszköz, hanem egy olyan eszköz, amely integrálja a matematikai műveleteket és az egységátváltást egy könnyen kezelhető platformon, hogy segítse a dolgozókat hatékonyabb és pontosabb munkavégzésben.
## 3.A rendszerre vonatkozó pályázat
## 4.Jelenlegi üzleti folyamatok modellje
#### Bevezetés:

Az alábbi dokumentáció célja a jelenlegi üzleti folyamatok modelljének bemutatása, kifejtve az
informatikai eszközök cseréjére és a mértékegység-átváltásra fókuszálva. A jelenlegi állapot elemzése 
alapján célunk a hatékonyság és pontosság növelése a dolgozók mindennapi munkavégzése során.

#### Jelenlegi Matematikai Műveletek:

A jelenlegi üzleti folyamatokban a matematikai műveletek manuálisan történnek. Dolgozóinknak
szükségük van az összeadásra, kivonásra, osztásra, szorzásra és gyökvonásra a mindennapi 
feladataikhoz. Az alkalmazottak papír alapú vagy egyszerű számológépek segítségével végzik el 
ezeket a műveleteket.

#### Mértékegység-Átváltó Folyamatok:

A mértékegység-átváltás jelenleg kihívást jelent. A dolgozóknak nincs egy központi eszközük az egységátváltásra, és gyakran kell keresniük a megfelelő átváltási arányokat az interneten vagy könyvekben.

####  Jelenlegi Hosszúság Átváltások:

Az átváltások a hosszúság területén időigényesek és potenciálisan hibásak lehetnek. A dolgozóknak nincs egységes eszközük, ami pontos és gyors átváltást tesz lehetővé milliméter, centiméter, deciméter, méter, kilóméter és mérföld között.

#### Jelenlegi Térfogat Átváltások:

A térfogatnál a dolgozók hasonló kihívásokkal szembesülnek, ahol a mililiter, centiliter, deciliter, liter, hektoliter és köbméter közötti átváltások időigényesek és hajlamosak hibákra.

#### Jelenlegi Tömeg Átváltások:

A tömegnél a qramm, dekagramm, kilógramm és tonna közötti váltások szintén manuálisan történnek, és nincs egységes rendszer a folyamatok gyorsítására.

#### Jelenlegi Kihívások:

Manuális műveletek okoznak időveszteséget és hibalehetőséget.
Egységes és gyors átváltások hiánya.
Nincs központi rendszer a matematikai műveletek és mértékegység-átváltások egyszerűsítésére.
#### Javasolt Fejlesztési Irányok:

Készítsünk egy egyszerű és intuitív számológép funkciót a matematikai műveletekhez.
Hozzunk létre egy központi mértékegység-átváltó rendszert a Hosszúság, Terület és Térfogat területeken.
Implementáljunk olyan algoritmusokat, amelyek gyorsan és pontosan végeznek átváltásokat különböző mértékegységek között.
#### Elvárható Előnyök:

Gyorsabb és pontosabb matematikai műveletek.
Egységes és hatékony mértékegység-átváltások.
Csökkenő hibaszázalék a mindennapi feladatok során.
Ez a dokumentáció felvázolja a jelenlegi üzleti folyamatok modelljét, és azokat a területeket, amelyeken fejlesztéseket kívánunk végrehajtani a hatékonyság és pontosság növelése érdekében.






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

