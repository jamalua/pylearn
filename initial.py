print('Bismillah')

try:
    a = input("Write the score => ")
    if float(a) > 1.0:
        print('Bad score')
    elif float(a) >= 0.9:
        print('A')
    elif float(a) >= 0.8:
        print('B')
    elif float(a) >= 0.7:
        print('C')
    elif float(a) < 0.6:
        print('F')
except:
    print("Bad score")

