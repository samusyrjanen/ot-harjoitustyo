from file_reader import Repository
from database_connection import get_database_connection

komennot = {
    'x': 'x lopeta',
    '0': '0 ohje',
    '1': '1 lisaa tulo',
    '2': '2 lisaa meno',
    '3': '3 tulosta arvio',
    '4': '4 tulosta kaikki menot ja tulot',
    '5': '5 poista tulo',
    '6': '6 poista meno',
    '7': '7 lisaa tämänhetkinen varallisuus',
    '8': '8 poista kaikki tiedot'
}

class Kayttoliittyma:#miten tätä kannattais jakaa osiin?
    def __init__(self, palvelu):
        self._palvelu = palvelu

    def ohje(self):
        for komento in komennot.values():
            print(komento)
        print()

    def kaynnista(self):
        self.ohje()

        while True:
            komento = input('anna komento: ')
            print()

            if komento not in komennot:
                print('virheellinen komento')
                self.ohje()
                continue

            if komento == 'x':
                break
            if komento == '0':
                self.ohje()
            if komento == '1':
                self._lisaa_tulo()
            if komento == '2':
                self._lisaa_meno()
            if komento == '3':
                self._tulosta_arvio()
            if komento == '4':
                self._tulosta_tiedot()
            if komento == '5':
                self._poista_tulo()
            if komento == '6':
                self._poista_meno()
            if komento == '7':
                self._lisaa_varallisuus()
            if komento == '8':
                self._poista_kaikki_tiedot()

    def _lisaa_tulo(self):
        nimi = input('Anna nimi tulolle: ')
        maara = int(input('Tulon määrä euroina: '))
        print()

        self._palvelu.add_income(maara, nimi)

    def _lisaa_meno(self):
        nimi = input('Anna nimi maksulle: ')
        maara = int(input('Maksujen määrä euroina: '))
        print()

        self._palvelu.add_expense(-maara, nimi)

    def _tulosta_arvio(self):
        tulot = self._palvelu.read_income()
        menot = self._palvelu.read_expenses()
        varallisuus = self._palvelu.read_wealth()

        print(f'''Tuloarviosi kuukaudessa: {sum(tulot+menot)}
Tuloarviosi vuodessa: {12*sum(tulot+menot)}

Varallisuutesi kuukauden päästä: {sum(tulot+menot) + varallisuus}
Varallisuutesi vuoden päästä: {12*sum(tulot+menot) + varallisuus}
        ''')

    def _poista_kaikki_tiedot(self):
        self._palvelu.clear()
        print('Tiedot poistettu')
        print()

    def _tulosta_tiedot(self):
        menot = self._palvelu.get_data_expenses()
        tulot = self._palvelu.get_data_income()

        print('Tulot:')
        for tulo in tulot:
            print(tulo[0], tulo[1])
        print()

        print('Menot:')
        for meno in menot:
            print(meno[0], meno[1])
        print()

    def _poista_tulo(self):
        nimi = input('Anna poistettavan tulon nimi: ')
        print()

        self._palvelu.delete_income(nimi)

    def _poista_meno(self):
        nimi = input('Anna poistettavan menon nimi: ')
        print()

        self._palvelu.delete_expense(nimi)

    def _lisaa_varallisuus(self):
        varallisuus = int(input('Anna tämänhetkinen varallisuus: '))
        print()

        self._palvelu.add_wealth(varallisuus)

repository = Repository(get_database_connection())
sovellus = Kayttoliittyma(repository)
sovellus.kaynnista()
