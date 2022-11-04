import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

''' #Kod do film_in_category, jeżeli str na wejsciu, int zrobiony w poprzednim laboratorium
#jedynie należy category_id nadpisać jako category (inna nazwa zmiennej)
#przypadek dla str
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
        category_id IN (
        SELECT
            category.category_id
        FROM
            category
        WHERE
            category.category_ID ~ '^ + category + $'
        )
        )
ORDER BY film.title, language.name ASC
'''
#category="AcTion"
#category="Action"
#test_midcode="SELECT film.title, language.name AS language, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (    SELECT film_category.film_id FROM film_category WHERE category_id IN ( SELECT category.category_id FROM category WHERE category.name ~ '^" + category + "$' ) ) ORDER BY film.title, language.name ASC"

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category) == str:
        coded_text="SELECT film.title AS title, language.name AS languge, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (    SELECT film_category.film_id FROM film_category WHERE category_id IN ( SELECT category.category_id FROM category WHERE category.name ~ '^" + category + "$' ) ) ORDER BY film.title, language.name ASC"
    elif type(category) == int:
        coded_text = "SELECT film.title AS title, language.name AS languge, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category) +") ORDER BY film.title, language.name ASC"
    else:
        return None
    ret = pd.read_sql(coded_text,con=connection) 
    return ret  

#w poprzednim przypadku dla "case sensetive
#...ame ~ '^" + category + "$' )...
#dodaj *
#...ame ~* '^" + category + "$' )...
#test_midcode2="SELECT film.title, language.name AS language, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (    SELECT film_category.film_id FROM film_category WHERE category_id IN ( SELECT category.category_id FROM category WHERE category.name ~* '^" + category + "$' ) ) ORDER BY film.title, language.name ASC"

def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category) == str:
        coded_text="SELECT film.title AS title, language.name AS languge, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (    SELECT film_category.film_id FROM film_category WHERE category_id IN ( SELECT category.category_id FROM category WHERE category.name ~* '^" + category + "$' ) ) ORDER BY film.title, language.name ASC"
    elif type(category) == int:
        coded_text = "SELECT film.title AS title, language.name AS languge, category.name AS category FROM film INNER JOIN language ON film.language_id = language.language_id INNER JOIN film_category ON film.film_id = film_category.film_id INNER JOIN category ON film_category.category_id = category.category_id WHERE film.film_id IN (SELECT film_category.film_id FROM film_category WHERE category_id = " + str(category) +") ORDER BY film.title, language.name ASC"
    else:
        return None
    ret = pd.read_sql(coded_text,con=connection) 
    return ret    

''' #Kod do film_cast
SELECT
    actor.first_name,
    actor.last_name
FROM
    film
INNER JOIN film_actor USING (film_id)
INNER JOIN actor USING (actor_id)
WHERE
    film.title ~ '^+title+$'
ORDER BY     actor.last_name, actor.first_name ASC
'''
title="Academy Dinosaur"
test_midcode3="SELECT actor.first_name, actor.last_name FROM film INNER JOIN film_actor USING (film_id) INNER JOIN actor USING (actor_id) WHERE film.title ~ '^" + title + "$' ORDER BY actor.first_name, actor.last_name ASC"

def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(title) is not str:
        return None 
    coded_text ="SELECT actor.first_name AS first_name, actor.last_name AS last_name FROM film INNER JOIN film_actor USING (film_id) INNER JOIN actor USING (actor_id) WHERE film.title ~ '^" + title + "$' ORDER BY actor.last_name, actor.first_name ASC"
    ret = pd.read_sql(coded_text,con=connection) 
    return ret    
''' #Kod do film_title_case_insensitive
SELECT
    film.title
FROM
    film
WHERE
    film.title ~* '(LIST)'
ORDER BY film.title ASC

gdzie LIST to wyliczanka elementów, połączana z elemnt1|element2|...|elementN 
'''
words=["Alone","TrIp"]
#words=['Giant', 'Harry', 'Birdcage', 'Iron']
str_final=""
for a in words:
    str_final=str_final+a+"|"
str_final=str_final[:-1]
test_midcode4="SELECT film.title FROM film WHERE film.title ~* '("+str_final+")' ORDER BY film.title ASC"


def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(words) is not list:
        return None
    str_final=""
    for a in words:
        if type(a) is not str:
            return None
        str_final=str_final+a+"|"
    str_final=str_final[:-1]
    
    coded_text="SELECT film.title AS title FROM film WHERE film.title ~* '(?:^| )("+str_final+")(?:$| )' ORDER BY film.title ASC"
    ret = pd.read_sql(coded_text,con=connection) 
    return ret 

