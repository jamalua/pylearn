def printInstructions(string_to_print):
    print(string_to_print)

def getUserScore(username):
    fhand = open('C:\\scripts\\pylearn\\UserScores.txt')
    d = dict()
    
    for line in fhand:
        try:
            line = line.split("," "r")
            d[line[0]] = line[1]
        except:
            pass
        

    return d.get(username,None)
    
    
    
