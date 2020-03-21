from movie import Movies

mov1 = Movies('And so it begins',None,'English','Robert Kingman, Joe Patterson','2019')

print(mov1)
mov1.genre = 'Fantacy'
mov1.genre = 'Romance'
print(mov1)
mov1.RecomendedMovie('Romance')