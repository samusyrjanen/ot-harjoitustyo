from file_reader import Repository
from database_connection import get_database_connection

komennot = {
    'x': 'x lopeta',
    '1': '1 lisaa tulo',
    '2': '2 lisaa meno',
    '3': '3 tulosta arvio',
    '4': '4 poista kaikki tiedot'
}

class Kayttoliittyma:
    def __init__(self):
        self._palvelu = Repository(get_database_connection())

    def ohje(self):
        for komento in komennot.values():
            print(komento)

    def kaynnista(self):
        self.ohje()

        while True:
            komento = input('anna komento: ')

            if komento not in komennot:
                print('virheellinen komento')
                self.ohje()
                continue

            if komento == 'x':
                break
            elif komento == '1':
                self._lisaa_tulo()
            elif komento == '2':
                self._lisaa_meno()
            elif komento == '3':
                self._tulosta_arvio()
            elif komento == '4':
                self._poista_kaikki_tiedot()

    def _lisaa_tulo(self):
        nimi = input('Anna nimi tulolle: ')
        maara = int(input('Tulon määrä euroina: '))

        self._palvelu.add_income(maara, nimi)

    def _lisaa_meno(self):
        nimi = input('Anna nimi maksulle: ')
        maara = int(input('Maksujen määrä euroina: '))

        self._palvelu.add_expense(-maara, nimi)

    def _tulosta_arvio(self):
        tulot = self._palvelu.read_income()
        menot = self._palvelu.read_expenses()

        print(f'Tuloarviosi kuukaudessa: {sum(tulot+menot)}')
        print(f'Tuloarviosi vuodessa: {12*sum(tulot+menot)}')

    def _poista_kaikki_tiedot(self):
        self._palvelu.clear()

sovellus = Kayttoliittyma()
sovellus.kaynnista()