import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(10000)
        self.varaton_maksukortti=Maksukortti(10)

    def test_rahamaara_ja_myydyt_lounaat_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa,
            self.kassapaate.edulliset,self.kassapaate.maukkaat),
            (100000,0,0))

    def test_kateisosto_edullisesti(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(1000),
            self.kassapaate.kassassa_rahaa,
            self.kassapaate.edulliset),
            (760,100240,1))

    def test_kateisosto_maukkaasti(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(1000),
            self.kassapaate.kassassa_rahaa,
            self.kassapaate.maukkaat),
            (600,100400,1))

    def test_kateisosto_maksu_ei_riittava(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(100),
            self.kassapaate.syo_maukkaasti_kateisella(100),
            self.kassapaate.kassassa_rahaa,
            self.kassapaate.edulliset,
            self.kassapaate.maukkaat),
            (100,100,100000,0,0))

    def test_korttiosto_edullisesti(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),
            self.kassapaate.edulliset,
            self.kassapaate.kassassa_rahaa),
            (True,1,100000))

    def test_korttiosto_maukkaasti(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),
            self.kassapaate.maukkaat,
            self.kassapaate.kassassa_rahaa),
            (True,1,100000))

    def test_varaton_korttiosto_edullisesti(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.varaton_maksukortti),
            self.kassapaate.edulliset,
            self.kassapaate.kassassa_rahaa),
            (False,0,100000))

    def test_varaton_korttiosto_maukkaasti(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.varaton_maksukortti),
            self.kassapaate.maukkaat,
            self.kassapaate.kassassa_rahaa),
            (False,0,100000))

    def test_rahan_lataus_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.varaton_maksukortti,1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa,
            self.varaton_maksukortti.saldo),
            (100000+1000,10+1000))

    def test_negatiivisen_rahamaaran_lataus_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.varaton_maksukortti,-1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa,
            self.varaton_maksukortti.saldo),
            (100000,10))