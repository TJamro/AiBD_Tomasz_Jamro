************************************************************************
Original data:
************************************************************************

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

************************************************************************
Command Files:
************************************************************************

WAŻNE
Działanie pliku processingdata.py uzależnione jest od skopiowania originalnego
pliky Weather.txt do folderu command files (projekt oceniany jest na innym komputerze, ścieżki dostępu
będą się różniły)

Przed uruchomieniem funckji można usunąć pliki loadme.txt, weather_sorted_date.txt
Funkcja nie nadpisuje ich, usunięcie pokaże że funkcjonalność działa

Plik loadme.txt
1)czytanie orginalnego pliku Weather.txt
2)tworzenie sepratora "|" pomiędzy sklepionymi wartościami ID,roku,miesiąca,nazwy mierzonej wielkości
3) zastąpienie starych separatorów "S","I"," " jako jeden i ten sam separator "|"
4) zapisanie zmienione pliku pod nazwą i rozszerzeniem "loadme.txt"

Plik weather_sorted_date.txt
1) wczytanie pliku loadme.txt jako tabela pandas (plik został specjalnie do tego przygotowany)
2) nazwanie kolumn
3) zamienienie 31 kolumn z osobnych dni, jako dwie kolumny "wartość" i "dzień"
4) każdy wpis TMIN,TMAX,PRCP zostaje wyciągnięty z rządów i zamienione w kolumny
5) zamienienie każdej zmiennej w typ danych str
6) usunięcie przypadkowych liter D w danych wartości (brak informacji, co oznaczają)
7) przesunięcie cyfr na początek string'u, ustalenie stałej długości 7 znaków
8) usunięcie rzędów dla których każda zmienna TMIN,TMAX,PRCP nie jest wartością liczbową - oznacza to brak wartości pomiaru
9) stworzenie kolumny daty która łączy dane z 3 kolumn roku, miesiąca, dnia
10) posegregowanie kolumn
11) zapisanie tabeli jako plik weather_sorted_date.txt

************************************************************************
Analysis Data
************************************************************************

Efekt końcowy uruchomienia skryptu Plik od weather_sorted_date.txt
Przykład lini z pliku

ID|Date|TMAX|TMIN|PRCP
MX000017004|1955-04-01|310    |150    |0 
Gdzie ID to nazwa stacji (w originalnym pliku, jest tylko 1 stacja),
Date to jest data w formacie yyyy-mm-dd, wcześniej znajdująca się w 33 osobnych kolumnach,
wartości TMAX,TMIN,PRCP w osobnych trzech kolumnach, które wcześniej były wartościami w wierszach

"Tidy data":
Każda zmienna tworzy kolumnę
-Obserwacja przynależy do stacji, posiada date pomiaru, oraz 3 wykryte zmienne
-Dane ID, date nie są obserwowanymi zmiennymi, ale są niezbędnymi informacjami do uporządkownia danych
Każda obserwacja tworzy rząd.
-Każdy rząd to pojedyńcza obserwacja 3 wartości z przypisaną datą
Każdy typ jednostki obserwacyjnej tworzy tabelę.
-istnieje tylko jedna stacja pogodowa w otrzymanych do laboratorium danych, nawet gdyby istniałe dany z innej stacji jest to nadal ten sam typ. Całkowicie innym typem jest na przykład stacja
 badania jakości wody lub inne typy informacji nie zawarte w originalnym pliku
************************************************************************
Documents
************************************************************************
Spostrzeżenia podczas pracy nad danymi:
-Isnieją dni z brakującymi pomiarami zmiennych. Dni w którym zdarzyłsię brak informacji od wszystkich trzech zmiennych są usunięte z pliku (naprzykład "31 dzień", gdy miesiąc miał 30 dni)
-Plik originalny posiadał niewyjaśnione litery D przy niektórych wartościach, informacja bez dokumentacji wyjaśniającej originalny plik została utracona
-Dlaczego plik posiadał trzy różne separatory, informacja bez dokumentacji wyjaśniającej originalny plik została utracona
-Istniały miesiące w originalnym pliku weather.txt, dla których pomiary pewnych danych zostały wstrzymane. Nie są zapisane jako rząd pełen -9999 wartości, te wiersze poprostu nie istniały