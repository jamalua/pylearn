class Movies(object):
    def __init__(self,ptitle,pgenre,plang,pdirectors,pyear):
        self.title = ptitle
        self._genre = pgenre
        self.lang = plang
        self.directors = pdirectors
        self.year = pyear

    def __str__(self):
        return f"Title = {self.title}, Genre = {self._genre}, Language = {self.lang}, Directors = {self.directors}, Release Year = {self.year}"
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        if value in ('Romance','Action','Drama','Thriller','Horror'):
            self._genre = value
        else:
            print(f'{value} is not a correct Genre')

    def RecomendedMovie(self,value):
        if value == 'Romance':
            print('Recomended Movie "First Date"')
        elif value == 'Action':
            print('Recomended Movie "Mutant"')
        elif value == 'Drama':
            print('Recomended Movie "The Awakening"')
        elif value == 'Thriller':
            print('Recomended Movie "Mr K"')
        elif value == 'Drama':
            print('Recomended Movie "A walk down Dowson Street"')
        else:
            print('Wrong choice')




