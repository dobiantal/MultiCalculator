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
A program működésének a használati eseteinek más néven forgatókönyvjeit írjuk most le. A kiinduló 
állapotot a program elíndítása után kapjuk meg. Ennek az állapotnak a kinézetét a képernyőtervben 
szemléltettük. Ez a kiinduló állapot. Ebből az állapotból tudunk eljutni a program 2 al működéséhez.
Ezek az alműködések a számológép és az átváltó. 

### Számológép
 A főképernyőröl az első funkció gombra kattintva juthatunk el a számológéphez. A program ezen része
lesz az ahol matematikai műveleteket tudunk használni. A matematikai műveletek közt az alábbi esetek
  fordulhatnak elő: 
* #### Osztás
  * Az osztás műveletet úgy tudjuk használni hogy elsőnek az osztani kívánt értékre kattintunk
    majd ezután az osztó értéket adjuk meg. Ez után pedig az "=" gombra kattintva a program kiírja 
    az értéket.
* #### Szorzás
  * Az szorzás műveletet az osztás műveletéhez hasonlóan kell elvégeznünk. A különbség a műveleti jel 
    között van. Lépéseiben nincs különbség.
* #### Kivonás
  * Az érték és kivonandó megadása közt megadott kivonási művelet után az "=" jelre kattintva 
    visszakapjuk az értéket.
* #### Összeadás
  * Az alap érték után az összeadás gomb kattintása után megadjuk a hozzáadandó értéket. Az " = " jel 
    pedig kiírja az összeadott értéket.
* #### Gyökvonás
    * A program egyetlen olyan operátorja ahol a beírt érték után a négyzetgyökre kattintva megkapjuk
    az értéket. Itt nem kell második értéket megadni! Nincs szükség az " = " jelre kattintásra sem! 

### Átváltó
Ha a főképernyőn a második gombra kattintunk akkor az átváltó program nyílik meg. Ezen a
felületen tudunk átváltásokat elvégezni a követzetőkkel:

* #### Távolság
    * **Távolságot** kiválasztva a legördülő listában a távolsághoz tartozó mértékegységek
    fognak megjelenni. Ezek a következők lehetnek : **mile**, **km**, **m**, **dm**, **cm**, **mm**. Ezek 
      közül kell kiválasztanunk azt a mértékegységet amiről át szeretnénk váltani.
    * A kiválasztott mértékegység után érdemes beírni az értéket
    * Ezt követően kell kiválasztanunk hogy milyen mértékegységbe szeretnénk megvalósítani az átváltást
    * Az utolsó lépés pedig a középen elhelyezett nyíllal jelzett gombra való kattintás.
    
* #### Tömeg
   * **Tömeg** kiválasztva a legördülő listában a tömeghez tartozó mértékegységek
    fognak megjelenni. Ezek a következők lehetnek : **t**, **kg**, **dkg**, **g**. Ezek 
      közül kell kiválasztanunk azt a mértékegységet amiről át szeretnénk váltani.
    * A kiválasztott mértékegység után érdemes beírni az értéket
    * Ezt követően kell kiválasztanunk hogy milyen mértékegységbe szeretnénk megvalósítani az átváltást
    * Az utolsó lépés pedig a középen elhelyezett nyíllal jelzett gombra való kattintás.
* #### Térfogat 
    * **Térfogat** kiválasztva a legördülő listában a térfogathoz tartozó mértékegységek
    fognak megjelenni. Ezek a következők lehetnek : **m3**, **hl**, **l**, **dl**,**cl**,**ml**. Ezek 
      közül kell kiválasztanunk azt a mértékegységet amiről át szeretnénk váltani.
    * A kiválasztott mértékegység után érdemes beírni az értéket
    * Ezt követően kell kiválasztanunk hogy milyen mértékegységbe szeretnénk megvalósítani az átváltást
    * Az utolsó lépés pedig a középen elhelyezett nyíllal jelzett gombra való kattintás.


## 6. Funkció–követelmény megfeleltetés
| ID | Verzió | Követelmény | Funkció |
|--|------| --- | -------- |
| K01 | V1.0 | Főmenü | A főmenü funkció a funkciók közti váltást teszi lehetővé. A program 2 szolgálatot tud teljesíteni.|  
| K02 | V1.0 | Számológép | A számológép a főmenüből elérhető a számológép button-ra kattintva.|
| K03 | V1.0 | Osztás | Ez a matematikai művelet a számológépben van elhelyezve. A jele "/". |
| K04 | V1.0 | Szorzás | Ez a matematikai művelet a számológépben van elhelyezve. A jele "*". | 
| K05 | V1.0 | Kivonás | Ez a matematikai művelet a számológépben van elhelyezve. A jele "-". |
| K06 | V1.0 | Összeadás | Ez a matematikai művelet a számológépben van elhelyezve. A jele "+". |  
| K07 | V1.0 | Gyökvonás | Ez a matematikai művelet a számológépben van elhelyezve. A jele "√". |
| K08 | V1.0 | Átváltó | Ez a funkció a Főmenüből érhető el az átváltó feliratú gombra kattintva. | 
| K09 | V1.0 | Távolság | Ezt a funkcót az átváltóban valósítottuk meg. Az első lehajtható box-ból lehet kiválasztani majd az ehhez tartozó mértékegységekkel számolásokat végezni | 
| K10 | V1.0 | Tömeg | Ezt a funkcót az átváltóban valósítottuk meg. Az első lehajtható box-ból lehet kiválasztani majd az ehhez tartozó mértékegységekkel számolásokat végezni | 
| K11 | V1.0 | Térfogat | Ezt a funkcót az átváltóban valósítottuk meg. Az első lehajtható box-ból lehet kiválasztani majd az ehhez tartozó mértékegységekkel számolásokat végezni | 


