from file_reader import File_reader

komennot = {
    'x': 'x lopeta',
    '1': '1 lisaa tulo',
    '2': '2 tulosta arvio',
    '3': '3 poista kaikki tiedot'
}

class Kayttoliittyma:
    def __init__(self):
        self._palvelu = File_reader()

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
                self._tulosta_arvio()
            elif komento == '3':
                self._poista_kaikki_tiedot()

    def _lisaa_tulo(self):
        nimi = input('Anna nimi tulolle: ')
        maara = input('Tulon määrä euroina: ')

        self._palvelu.add(maara, nimi)

    def _tulosta_arvio(self):
        tulot = self._palvelu.read()

        print(sum(tulot))

    def _poista_kaikki_tiedot(self):
        self._palvelu.clear()

sovellus = Kayttoliittyma()
sovellus.kaynnista()