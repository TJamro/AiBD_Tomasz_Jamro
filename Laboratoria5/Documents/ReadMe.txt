Original data:

Przydatna zawartość zkopiowana z podfolderu Metadata:
MX000017004195504TMAX  310  I  310  I  310  I  320  I  330  I  320  I  320  I  330  I  330  I  330  I  330  I  320  I  310  I  310  I  320  I  320  I  320  I  310  I  310  I  320  I  320  I  330  I  330  I  330  I  330  I  330  I  330  I  340  I  330  I  320  I-9999

z MX000017004195504TMAX  
MX000017004 to nazwa stacji ID (początek każdego wiersza)

z MX000017004195504TMAX  
1955 to rok (4 cyfry po ID, tak samo do każdego wpisu)

z MX000017004195504TMAX  
04 to miesiąc (5 i 6 cyfra po ID, tak samo dla każdego wpisu)

z MX000017004195504TMAX  
TMAX (końcówka pierwszych liter na początku wiersza, możliwe wartości to TMAX,TMIN, albo PRCP) 

Następnie dane dla każdego dnia są prezentowana kolumna po kolumnie, dzień posiada długość 7 znaków na wpis, po czym występuje segregator
separatory dla dni miesiąca to chaos, opcje to:
1) Brak separatora (1 dzień, odrazu po nazwie zmiennej)
2) spacja
3) litera "I" 
4) litera "S"

brak wpisu lub utracenie danych to -9999
czasmi przypadkowa litera D jest wpisana do pomiarów

Command Files:

WAŻNE
Działanie funkcji processing data uzależnione jest od skopiowania originalnego
pliky Weather.txt do folderu command files (projekt oceniany jest na innym komputerze, ścieżki dostępu
będą się różniły)

Przed uruchomieniem funckji można usunąć pliki loadme.txt, weather_sorted_date.txt
Funkcja nie nadpisuje ich, usunięcie pokaże że funkcjonalność działa


