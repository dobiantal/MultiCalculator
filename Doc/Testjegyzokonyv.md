#Tesztjegyzőkönyv
Tesztelést végezte: Tatár Tamás, Dobi Antal
Operációs rendszer: WIN10, MAC OS
Dátum: 2024.01.17.
Talált hibák száma: 0

### Mértékegységátváltó Unit teszt
* A mértékegység átváltó backend szolgáltatás tesztelése alkalmával megvizsgáltunk minden variációt
Amit a felhasználó a beviteli mezők segítségével el tud érni. A tesztesetek lefuttatása alkalmával nem
kaptunk hibaüzenetet. Az értékek megfeleőek.

### Számológép Unit teszt
* A számológép backend szolgáltatások tesztelése során megvizsgáltuk, hogy a különböző műveletek a végrehajtása során
a megfeleő értékkel tér-e vissza metódusunk.  A tesztesetek lefuttatása alkalmával nem
kaptunk hibaüzenetet. Az értékek megfeleőek.

### Számológép frontend manuális teszt
* A megjelenő képernyőn látható gombok a megfelelő működési funkciót látják el.
A visszatérési értékek az elvártaknak megfelelnek.

### Mértékegység átváltó frontend manuális teszt
* A megjelenő képernyőn látható gombok a megfelelő működési funkciót látják el. A visszatérési értékek
az elvártaknak megfelelnek.

### A Mértékegységátváltó és a Számológép integrációs tesztje.(Kezdőképernyő teszt)
* Összeillesztettük a számológép és a mértékegységátváltó modult a kedzőképernyővel. Az összeillesztés
sikereses volt. A kezdőképernyőn a gombok lenyomás után a megfelelő ablak nyílik meg.