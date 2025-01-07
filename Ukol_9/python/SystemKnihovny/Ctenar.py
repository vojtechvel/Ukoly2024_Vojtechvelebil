import random


class Ctenar:
    def __init__(self, jmeno: str, prijmeni: str):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self.cislo_prukazky = self.vygeneruj_cislo_prukazky()

    #geter a seter pro cislo prukazky s kontrolou prazdne hodnoty
    @property
    def cislo_prukazky(self):
        return self.cislo_prukazky
    
    @cislo_prukazky.setter
    def cislo_prukazky(self, a):
        if a <= 0:
            raise ValueError("Špatná hodnota")
        self.cislo_prukazky = a

    @staticmethod
    def vygeneruj_cislo_prukazky() -> int:
        return random.randint(1, 100000)

#vypíše informace o čtenářovi
    def __str__(self) -> str:
        return f"Čtenář {self.jmeno} {self.prijmeni}, číslo průkazky: {self.cislo_prukazky}"
