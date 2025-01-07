from __future__ import annotations
from .Kniha import Kniha
from .Ctenar import Ctenar
import csv
import datetime


class Knihovna:
    def __init__(self, nazev: str):
        self.nazev = nazev
        self.knihy: list[Kniha] = []
        self.ctenari: list[Ctenar] = []
        self.vypujcene_knihy = {}

    def kniha_existuje(funkce):
        def wrapper(self, isbn: str, *args, **kwargs):
            if not any(kniha.isbn == isbn for kniha in self.knihy):
                raise ValueError(f"Kniha s ISBN {isbn} neexistuje.")
            return funkce(self, isbn, *args, **kwargs)
        return wrapper

    @classmethod
    def z_csv(cls, soubor: str) -> Knihovna:
        with open(soubor, newline='', encoding='utf-8') as csv_soubor:
            reader = csv.reader(csv_soubor)

            # Načtení názvu knihovny z prvního řádku
            prvni_radek = next(reader)
            nazev_knihovny = prvni_radek[0].split(":")[1].strip()

            knihovna = cls(nazev_knihovny)

            # Přečtení zbytku souboru
            reader = csv.DictReader(csv_soubor)  # DictReader začne číst od aktuální pozice
            for row in reader:
                if row['typ'] == 'kniha':
                    knihovna.pridej_knihu(
                        Kniha(row['nazev'], row['autor'], int(row['rok_vydani']), row['isbn'])
                    )
                elif row['typ'] == 'ctenar':
                    knihovna.registruj_ctenare(
                        Ctenar(row['jmeno'], row['prijmeni'])
                    )
        return knihovna

    def pridej_knihu(self, kniha: Kniha):
        if any(existing.isbn == kniha.isbn for existing in self.knihy):
            raise ValueError(f"Kniha s ISBN {kniha.isbn} již existuje.")
        self.knihy.append(kniha)

    @kniha_existuje
    def odeber_knihu(self, isbn: str):
        del self.knihy[isbn]
        
        

    def vyhledej_knihu(self, klicova_slovo: str = "", isbn: str = ""):
        if isbn:
            return [kniha for kniha in self.knihy if kniha.isbn == isbn]
        return [
            kniha for kniha in self.knihy
            if klicova_slovo in kniha.nazev or
               klicova_slovo in kniha.autor or
               klicova_slovo in kniha.rok_vydani
        ]
        

    def registruj_ctenare(self, ctenar: Ctenar):
        if ctenar in self.ctenari:
            raise ValueError("takový čtenář už existuje")
        self.ctenari.append(ctenar)

    def zrus_registraci_ctenare(self, ctenar: Ctenar):
        if ctenar not in self.ctenari:
            raise ValueError("Čtenář nemá registrac")
        del self.ctenari[ctenar]

    def vyhledej_ctenare(self, klicova_slovo: str = "", cislo_prukazky: int = None):
        if cislo_prukazky is not None:
            return [ctenar for ctenar in self.ctenari if ctenar.cislo_prukazky == cislo_prukazky]
        return [
            ctenar for ctenar in self.ctenari if klicova_slovo in ctenar.jmeno or
               klicova_slovo in ctenar.prijmeni
        ]

    @kniha_existuje
    def vypujc_knihu(self, isbn: str, ctenar: Ctenar):
        if isbn in self.vypujcene_knihy:
            raise ValueError(f"Kniha s ISBN {isbn} je již půjčena.")
        self.vypujcene_knihy[isbn] = (ctenar, datetime.date.today())

    @kniha_existuje
    def vrat_knihu(self, isbn: str, ctenar: Ctenar):
        if isbn not in self.vypujcene_knihy or self.vypujcene_knihy[isbn][0] != ctenar:
            raise ValueError(f"Kniha s ISBN {isbn} není půjčena tímto čtenářem.")
        del self.vypujcene_knihy[isbn]

    def __str__(self) -> str:
        knihy_str = "\n".join(str(kniha) for kniha in self.knihy)
        ctenari_str = "\n".join(str(ctenar) for ctenar in self.ctenari)
        return f"Knihovna: {self.nazev}\nKnihy:\n{knihy_str}\nČtenáři:\n{ctenari_str}"
