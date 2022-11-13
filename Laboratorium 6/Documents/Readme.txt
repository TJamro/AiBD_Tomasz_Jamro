***********************************************************************
Kopia informacji od podfolderu Metadata
***********************************************************************
Originalny plik zawiera informację zwrotne od klientów dotyczące oceny odkurzaczy dla województwa Śląskiego w jednej z sieci sklepów. 


Originalny plik zawiera dane z 6 kolumnami:
1) Nienazwana kolumna, liczba porządkowa
2) Kolumna "Dni od zakupu", jak wskazuje nazwa, określa czas pomiędzy zakupem a wysłaniem oceny
3) Kolumna "Marka" zawiera informację, od której firmy 
4) Kolumna "Wiek kupującego" zawiera wiek osób które oceniajy kupiony produkt
Najpradopodobniej nie była to wymagana informacja, ponieważ w niektórych wpisach brakuje tej informacji
Szansa, że wywołane jest to utratą/uszkodzeniem danych jest minimalna, w takim przypadku wszystkie kolumny udległyby uszkodzeniu
5) Kolumna "Płeć kupującego" zawiera dwie możliwe wartości K,M
K - Kobieta
M - Męszczyzna
bd. - 1 wykryty wynik, z powodu braku informacji metadanych od źródła, pozostaje jedynie zgadnąć że była płeć prawdopodobnie nie została podana.
6) Kolumna "Ocena", Najważniejsza informacja, określa w skali 0-5 zadowolenie z produktu 

***********************************************************************
Działanie plików do wyciągnięcia danych statystycznych
***********************************************************************
Plik orginalny posiada uporządkowane dane. 
Ponieważ jest tylko jedna orginalna baza danych, a żadna nowa zmienna nie została wywnioskowana na podstawie tego pliku,
plik w folderze analysis data jest identyczny co do original data

działanie pliku plots.py
1)Wczytanie informacji z pliku źródłowego
2)Utworzenie tabeli frekwencji wartości dla każdej kolumny posiadającej zmienne jako zmienna Series od biblioteki Pandas
3)Przekonwertowanie kolumn z liczbowymi wartościami na numpy.array, obliczenie podstawowych danych statystycznych
4)Stworzenie wykresów za pomocą zmiennych Series z punktu 2), albo zmiennych numpy.array z punktu 3