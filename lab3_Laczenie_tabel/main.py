import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple



connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

''' #Kod do film_in_category
SELECT
    film.title AS title,
    language.name AS languge,
    category.name AS category
FROM
    film
INNER JOIN language ON film.language_id = language.language_id
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE
    film.film_id IN (    
    SELECT
        film_category.film_id
    FROM
        film_category
    WHERE
        category_id = ' + str(category_id) +
        )
ORDER BY film.title, language.name ASC
'''
#df = pd.read_sql("SELECT * from film WHERE language_id = 1",con=connection) #ten test pokazuje, że w bazie danych są tylko i wyjąćznie anglojęzyczne filmy...
#category_id=10
#test_midcode = "SELECT film.title, language.name AS language, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category_id) +") ORDER BY film.title, language.name ASC"

def film_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category_id) != int:
        return None
    coded_text = "SELECT film.title AS title, language.name AS languge, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category_id) +") ORDER BY film.title, language.name ASC"
    ret = pd.read_sql(coded_text,con=connection) 
    return ret

  
''' #Kod do number_films_in_category
SELECT
    category.name AS category,
    COUNT(film.title)
FROM
    film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category USING (category_id) 
WHERE
    film.film_id IN (    
    SELECT
        film_category.film_id
    FROM
        film_category
    WHERE
        category_id = ' + str(category_id) +
        )
    GROUP BY category.name 
'''    
#category_id=10
#test_midcode2 = "SELECT category.name AS category, COUNT(film.title) FROM film INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category USING (category_id) WHERE film.film_id IN ( SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category_id) + ") GROUP BY category.name "

def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category_id) != int:
        return None
    coded_text = "SELECT category.name AS category, COUNT(*) as count FROM film INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category USING (category_id) WHERE film.film_id IN ( SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category_id) + ") GROUP BY category.name "
    ret = pd.read_sql(coded_text,con=connection) 
    return ret

  
''' #Kod do number_film_by_length
SELECT
    length,
    COUNT(*)
FROM
    film
WHERE
    length BEETWEN ' + str(min_length) + ' AND ' + str(max_length) + '
GROUP BY length 
'''    
#min_length=145
#max_length=146
#test_midcode3 = "SELECT length, COUNT(*) FROM film WHERE length BETWEEN " + str(min_length) + " AND " + str(max_length) + " GROUP BY length "


def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if (type(min_length) is not int and type(min_length) is not float) or (type(max_length) is not int and type(max_length) is not float):
        return None    
    coded_text = "SELECT length, COUNT(*) FROM film WHERE length BETWEEN " + str(min_length) + " AND " + str(max_length) + " GROUP BY length "
    ret = pd.read_sql(coded_text,con=connection) 
    return None if ret.empty else ret

''' #Kod do client_from_city
SELECT
    city.city,
    customer.first_name,
    customer.last_name
FROM
    customer
INNER JOIN address USING (address_id) 
INNER JOIN city USING (city_id) 
WHERE
    customer.address_id IN (    
    SELECT
        address.address_id
    FROM
        address
    WHERE
        city_id IN (
        SELECT
            city.city_id
        FROM
            city
        WHERE
            city = ('+ city +')
                )
        )
ORDER BY customer.first_name, customer.last_name ASC 
'''    
#city="Aden" # Lethbridge - 0, , York - 1,
#test_midcode4 = "SELECT city.city, customer.first_name, customer.last_name FROM customer INNER JOIN address USING (address_id) INNER JOIN city USING (city_id) WHERE customer.address_id IN ( SELECT address.address_id FROM address WHERE city_id IN ( SELECT city.city_id FROM city WHERE city = ('"+ city + "') ) ) ORDER BY customer.first_name, customer.last_name ASC "

def client_from_city(city:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(city) is not str:
        return None
    coded_text = "SELECT city.city, customer.first_name, customer.last_name FROM customer INNER JOIN address USING (address_id) INNER JOIN city USING (city_id) WHERE customer.address_id IN ( SELECT address.address_id FROM address WHERE city_id IN ( SELECT city.city_id FROM city WHERE city = ('"+ city + "') ) ) ORDER BY customer.first_name, customer.last_name ASC "
    ret = pd.read_sql(coded_text,con=connection) 
    return ret


''' #Kod do avg_amount_by_length
SELECT
    film.length,
    AVG(payment.amount)
FROM
    film
INNER JOIN inventory USING (film_id) 
INNER JOIN rental USING (inventory_id) 
INNER JOIN payment USING (rental_id) 
WHERE
    film.length = + str(length) + 
GROUP BY film.length
'''    
#length = 90
#test_midcode5 = "SELECT film.length, AVG(payment.amount) FROM film INNER JOIN inventory USING (film_id) INNER JOIN rental USING (inventory_id) INNER JOIN payment USING (rental_id) WHERE film.length = " + str(length) + " GROUP BY film.length"

def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(length) is not int and type(length) is not float:
        return None
    coded_text = "SELECT film.length, AVG(payment.amount) FROM film INNER JOIN inventory USING (film_id) INNER JOIN rental USING (inventory_id) INNER JOIN payment USING (rental_id) WHERE film.length = " + str(length) + " GROUP BY film.length"
    ret = pd.read_sql(coded_text,con=connection) 
    return ret

''' #Kod do client_by_sum_length
SELECT
    customer.first_name,
    customer.last_name,
    SUM(film.length)
FROM
    customer
INNER JOIN rental USING (customer_id) 
INNER JOIN inventory USING (inventory_id) 
INNER JOIN film USING (film_id)  
GROUP BY customer.first_name, customer.last_name
HAVING SUM(film.length) >= + str(min_sum) +
ORDER BY SUM(film.length), customer.first_name, customer.last_name ASC
'''    
#sum_min = 1999
#test_midcode6 = "SELECT customer.first_name, customer.last_name, SUM(film.length) FROM customer INNER JOIN rental USING (customer_id) INNER JOIN inventory USING (inventory_id) INNER JOIN film USING (film_id) GROUP BY customer.first_name, customer.last_name HAVING SUM(film.length) >= " + str(sum_min) + "ORDER BY SUM(film.length), customer.first_name, customer.last_name ASC "
def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(sum_min) is not int and type(sum_min) is not float:
        return None
    coded_text = "SELECT customer.first_name As first_name, customer.last_name AS last_name, SUM(film.length) as sum FROM customer INNER JOIN rental USING (customer_id) INNER JOIN inventory USING (inventory_id) INNER JOIN film USING (film_id) GROUP BY customer.first_name, customer.last_name HAVING SUM(film.length) >= " + str(sum_min) + "ORDER BY SUM(film.length), customer.last_name, customer.first_name ASC "
    ret = pd.read_sql(coded_text,con=connection) 
    return ret 
''' #Kod do film_in_category
SELECT
    category.name AS category,
    AVG(film.length),
    SUM(film.length),
    MIN(film.length),
    MAX(film.length)
FROM
    category
INNER JOIN film_category USING (category_id)
INNER JOIN film USING (film_id)
WHERE
    category.name = ('+ name +')
GROUP BY category.name
'''
#name = "Action"
#test_midcode7 = "SELECT category.name AS category, AVG(film.length), SUM(film.length), MIN(film.length), MAX(film.length) FROM category INNER JOIN film_category USING (category_id) INNER JOIN film USING (film_id) WHERE category.name = ('"+ name +"') GROUP BY category.name"
def category_statistic_length(name:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(name) is not str:
        return None
    coded_text = "SELECT category.name AS category, AVG(film.length), SUM(film.length), MIN(film.length), MAX(film.length) FROM category INNER JOIN film_category USING (category_id) INNER JOIN film USING (film_id) WHERE category.name = ('"+ name +"') GROUP BY category.name"
    ret = pd.read_sql(coded_text,con=connection) 
    return ret




#testowanie składni języka
'''
SELECT
    film_id
    title
FROM
    film
WHERE
    film_id IN (
        SELECT
            inventory.film_id
        FROM
            rental
        INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
        WHERE
            return_date BETWEEN '2005-05-29' AND '2005-05-30'
    );
'''
#test = "SELECT title, film_id FROM film WHERE film_id IN ( SELECT inventory.film_id FROM rental INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id WHERE return_date BETWEEN '2005-05-29 00:00:00' AND '2005-05-30 23:59:59')"
#df = pd.read_sql(test_midcode,con=connection)
#df
#category_id = 1
#coded_text = "SELECT film.title, language.name AS language, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category_id) +") ORDER BY film.title, language.name ASC"
#ret = pd.read_sql(coded_text,con=connection) 
#print(ret)