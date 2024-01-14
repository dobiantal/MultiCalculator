# Tesztelési terv

### 1. Számológép frontend 
* Manuális teszttel ellenőrizzük a működést:  
_A manuális teszt során kézzel megkattintjuk a funkciógombokat, hogy a megfelelő funkcióhoz a
megfelelő kimenetet jelenik meg._
### 2. Számológép backend
A számológép backend tesztelésénél Unit teszt alkalmazása. Ezeknek a unit teszteknek 
az opárátorok metódusainak pontosságát kell ellenőriznie. Minden operátorra készíteni kell
unit tesztet. Ez a jegyzőkönyvben a **T2** jelzéssel fog szerepelni!
### 3. Átváltó frontend 
Az átváltó frontendet manuális módon kell tesztelni. A tesztben ellenőrizni kell, hogy
minden funkció gomb azt az eseményt hívja meg amit meg kell hívnia. Továbbá ellenőrizni kell
a legördülő listák helyességét. Esetleges probléma esetlegesen ott merülhet fel 
ahol már a mértékegységet kell kiválasztani. Ha nem a megfelelő típusú mértékegység jelenik meg
arra hibajegyet kell készíteni. A jegyzőkönyvben a **T3** mas jelzéssel fog szerepelni!
### 4. Átváltó backend
* Unit teszt:  
_Minden metódust mely az átváltásokért felelős értéktesztnek vetjük alá. Ellenőrizzük, hogy
minden átváltás a mefelelő értékkel tér vissza._
### 5. Főképernyő
* Manuális teszt:  
_Az első verzióban a kezdőképernyőn két funkciógomb fog helyet foglalni. Ezek tesztelése, melyben
vizsgáljuk, hogy a megfelelő gomb a hozzárendelt új képernyőt nyitja._

