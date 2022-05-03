# Budjettisovellus

Sovelluksen tarkoitus on auttaa rahankulutuksen ja säästämisen arvioinnissa. Sovellukseen voi kirjata tuloja ja menoja.

## Python

Sovellus on testattu python-versiolla 3.8

## release

[https://github.com/samusyrjanen/ot-harjoitustyo/releases](https://github.com/samusyrjanen/ot-harjoitustyo/releases)

## Dokumentaatio

[vaatimusmäärittely](./harjoitustyo/dokumentaatio/vaatimusmaarittely.md)  
[työaikakirjanpito](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)  
[changelog](./harjoitustyo/dokumentaatio/changelog.md)  
[arkkitehtuuri](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)  
[käyttöohje](./harjoitustyo/dokumentaatio/kayttoohje.md)  

## Asennus

Asenna riippuvuudet:  
Siirry ensin hakemistoon harjoitustyo/  
`poetry install`  

Tietokannan alustus:  
`poetry run invoke initialize-database`

Sovelluksen käynnistys:  
`poetry run invoke start`

## komentorivitoiminnot

Ohjelman suorittaminen:  
`poetry run invoke start`

Testaus:  
(testien suorittaminen poistaa olemassa olevat tiedot sovelluksesta)  
`poetry run invoke test`

Testikattavuus:  
(testien suorittaminen poistaa olemassa olevat tiedot sovelluksesta)  
`poetry run invoke coverage-report`  

Pylint:  
`poetry run invoke lint`