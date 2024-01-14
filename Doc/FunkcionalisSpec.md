# Funkcionális specifikáció

## 1. A rendszer céljai és nem céljai
Az alkalmazás célja, hogy megalósíthassunk egy olyan egyszerűen használható multifunkciós
kalkulátort, mely minden felhasználó számára megkönnyíti a mindennapi számítási, átszámítási 
problémákat. Fontos szempont számunkra, hogy applikációnk egy egyszerű hétköznapi módon használható 
kézreálló kalkulátor csomag legyen. Álomcélként tűztük ki, hogy minden számítógépen ez legyen az alap kalkulátor
csomag hasonlóképpen, mint egy Microsoft Office csomag.
## 2. Használati esetek
####2.1 Rendszert használó közönség
* Irodai használat.
* Otthoni hétköznapi használat.
* Telefonos mobil alkalmazás (Terepmunkások számára).
####2.2 A rendszernek a következő funkciókat kell ellátnia
* A felhasználók képesen legyenek a főmenüből elindítani a különböző alfunkciókat.
* A felhasználók az első verzió tartalmaként képesek legyen elindítani a számológép funkciót és alapvető műveleteket elvégezni.
* A felhasználók el tudják indítani és egyszerűen képesnek legyen használni a mértékegység átváltó funkciót.
![Use_case](https://github.com/dobiantal/MultiCalculator/blob/work/Doc/UML/Use_case.png )
![Állapotgép](https://github.com/dobiantal/MultiCalculator/blob/work/Doc/UML/Allapotgep.png )
## 3. Megfeleltetés, hogyan fedik le a használati esetek a követelményeket
ID|Verzió|Név|Kifejtés
--|------|---|--------
K01|V1.0|Összeadás|A számológép összeadás metódusa kap 2 operandust összeadja a két számot és képernyőjére kiírja az eredményt.|
K02|V1.0|Kivonás|A számológép kivonás metódusa kap 2 operandust kivonja a két számot és képernyőjére kiírja az eredményt|
K03|V1.0|Szorzás|A számológép szorzás metódusa kap 2 operandust összeszorozza a két számot és képernyőjére kiírja az eredményt|
K04|V1.0|Osztás|A számológép osztás metódusa kap 2 operandust elosztja a két számot és képernyőjére kiírja az eredményt|
K05|V1.0|Gyökvonás|A számológép négyzetgyök metódusa kap egy operandust veszi a négyzetgyökét és képernyőjére kiírja az eredményt|
K06|V1.0|Távolság|A mértékegység átváltó távolság értékek átváltásáért felelős metódus kap egy átváltandó számot és átváltja a kiválasztott SI mértékegységre.|
K07|V1.0|Tömeg|A mértékegység átváltó tömeg értékek átváltásáért felelős metódus kap egy átváltandó számot és átváltja a kiválasztott SI mértékegységre.|
K08|V1.0|Térfogat|A mértékegység átváltó térfogat értékek átváltásáért felelős metódus kap egy átváltandó számot és átváltja a kiválasztott SI mértékegységre.| 
## 4. Képernyőtervek
![Fokepernyo]( https://github.com/dobiantal/MultiCalculator/blob/work/Doc/Kepernyoterv/Fokepernyo.jpg)
![Szamologep]( https://github.com/dobiantal/MultiCalculator/blob/work/Doc/Kepernyoterv/Szamologep.jpg)
![Atvalto]( https://github.com/dobiantal/MultiCalculator/blob/work/Doc/Kepernyoterv/Atvalto.jpg)
## 5. Forgatókönyvek

## 6. Funkció–követelmény megfeleltetés



