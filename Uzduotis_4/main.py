# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.


class Movie:
    """Movie klasė turinti pavadinimo, režisieriaus ir biudžeto savybes"""

    def __init__(self, title, director, budget):
        """Sukuriamos pavadinimo, režisieriaus ir biudžeto savybės"""
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        """Grąžina True, jeigu biudžetas > 100 000 000 USD, kitu atveju False"""
        return self.budget > 100000000
          


movie1 = Movie("Harry Potter and the Prisoner of Azkaban", "Alfonso Cuaron", 130000000)
movie2 = Movie("The Godfather", "Francis Ford Coppola", 6000000)
movie3 = Movie("Pulp Fiction", "Quentin Tarantino", 8000000)


# print(movie1.was_expensive())
# print(movie2.was_expensive())
# print(movie3.was_expensive())