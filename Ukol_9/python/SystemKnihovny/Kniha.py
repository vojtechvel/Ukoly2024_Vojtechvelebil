class Kniha:
    def __init__(self, nazev: str, autor: str, rok_vydani: int, isbn: str):
        self._nazev = nazev
        self._autor = autor
        self._rok_vydani = rok_vydani
        self.isbn = isbn

    @property
    def isbn(self):
        return self.isbn

# seter s kontrolou prazdné hodnoty a kontrolou správného zadaní hodnoty nové
    @isbn.setter
    def isbn(self, a):
        if not value:
            raise ValueError("Nesmí být prázdná hodnota")
        if (a > 999999999999):
            if (a < 10000000000000):
                self.isbn = a 
# vrací veškeré informace o knize
    def __str__(self) -> str:
        return f"Název: {self._nazev} Autor: {self._autor} Vydání: {self._rok_vydani} ISBN: {self._isbn}"
