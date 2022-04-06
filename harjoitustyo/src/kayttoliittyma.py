from file_reader import Repository
from database_connection import get_database_connection

komennot = {
    'x': 'x lopeta',
    '1': '1 lisaa tulo',
    '2': '2 lisaa meno',
    '3': '3 tulosta arvio',
    '4': '4 tulosta kaikki menot ja tulot',
    '5': '5 poista tulo',
    '6': '6 poista meno',
    '7': '7 poista kaikki tiedot'
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
                self._tulosta_tiedot()
            elif komento == '5':
                self._poista_tulo()
            elif komento == '6':
                self._poista_meno()
            elif komento == '7':
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

    def _tulosta_tiedot(self):
        menot = self._palvelu.get_data_expenses()
        tulot = self._palvelu.get_data_income()

        print('Tulot:')
        for tulo in tulot:
            print(tulo[0], tulo[1])

        print('Menot:')
        for meno in menot:
            print(meno[0], meno[1])

    def _poista_tulo(self):
        nimi = input('Anna poistettavan tulon nimi: ')

        self._palvelu.delete_income(nimi)

    def _poista_meno(self):
        nimi = input('Anna poistettavan menon nimi: ')

        self._palvelu.delete_expense(nimi)

sovellus = Kayttoliittyma()
sovellus.kaynnista()