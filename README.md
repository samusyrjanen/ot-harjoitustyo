# Budjettisovellus

Sovelluksen tarkoitus on auttaa rahankulutuksen ja säästämisen arvioinnissa. Sovellukseen voi kirjata tuloja ja menoja.

## Python

Sovellus on testattu python-versiolla 3.8

## Dokumentaatio

[vaatimusmäärittely](./harjoitustyo/dokumentaatio/vaatimusmaarittely.md)  
[työaikakirjanpito](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)  
[changelog](./harjoitustyo/dokumentaatio/changelog.md)  
[arkkitehtuuri](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)  

## Asennus

Asenna riippuvuudet:  
`poetry install`  

Tietokannan alustus:  
`poetry run invoke initialize-database`

Sovelluksen käynnistys:  
`poetry run invoke start`

## komentorivitoiminnot

Ohjelman suorittaminen:  
`poetry run invoke start`

Testaus:  
`poetry run invoke test`

Testikattavuus:  
`poetry run invoke coverage-report`  

Pylint:  
`poetry run invoke lint`