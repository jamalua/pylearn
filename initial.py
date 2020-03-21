print('Bismillah')



def computer_grade(grade):
    try:
        if float(grade) > 1.0:
            print('Bad score')
        elif float(grade) >= 0.9:
            print('A')
        elif float(grade) >= 0.8:
            print('B')
        elif float(grade) >= 0.7:
            print('C')
        elif float(grade) < 0.6:
            print('F')
    except:
        print('Bad score')


#a = input('Enter teh grade => ')
#computer_grade(a)
"""
sum = 0
loopNumber = 0
while True:
    i = input('Enter a number: ')
    if i == 'done':
        break
    try:
        num = int(i)
        sum = sum + num
        loopNumber = loopNumber + 1
    except:
        print('bad data')
print( sum / loopNumber10 )

  

str  = 'X-DSPAM-Confidence:0.8475'

col_pos = str.find(':')
num = str[col_pos+1:]
fl_number = float(num)
print(fl_number)





fhand = open('c:\\Users\\Jamal\\Desktop\\romeo.txt')
count = 0
t = []
for line in fhand:
    temp = line.split()
    for word in temp:
        if word not in t:
            t.append(word)
t.sort()
print(t)


fhand = open('c:\\Users\\Jamal\\Desktop\\mbox-short.txt')
name = ""
for line in fhand:
    if 'From' in line:
        temp = line.split()
        name = name + temp[1] + '\n'
print(name)


word = 'asdsaasdfsdaetwerkhdslfkoermnaskdekklereksipqwoezcxcxmdiwasdasdasdqwwrasdiyfsdaisdajkhfdskjfhsdfdsfwpoiuetryurbne'
d = dict()

for letter in word:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] = d[letter] + 1
print(d)


fhand = open('c:\\Users\\Jamal\\Desktop\\mbox-short.txt')
d = dict()
for line in fhand:
    if 'From' in line:
        line = line.strip()
        li = line.split()
        try:
            if li[2] not in d:
                d[li[2]] = 1
            else:
                d[li[2]] = d[li[2]] + 1
        except:
            print(li)
print(d)


txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append([len(word), word])

t.sort(reverse=True)
print(t)

res = list()
for length, word in t:
    res.append(word)

print(res)


data = ''' 
dfdsf
dsfdsf
dfdsf
sdfdsf
sdfdsf
'''

fhand = open('c:\\Users\\Jamal\\Desktop\\mbox-short.txt')
d = dict()
for line in fhand:
    if 'From' in line:
        words = line.split()
        if 'From' in words:
            d[words[1]] = d.get(words[1], 0) + 1

print(d)

l = list()
for k,v in d.items():
    l.append((v,k))
    l.sort(reverse=True)

print(l[0])

#Google maps stuff
https://developers.google.com/places/web-service/place-id
https://developers.google.com/places/web-service/search
https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Batapur&inputtype=textquery&key=AIzaSyC2AEgrNdbDcIO6Lj1iiRrd1EkGgAcQZ-E
https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJ36B9SuYRGTkRt7mgaBbqoHk&key=AIzaSyC2AEgrNdbDcIO6Lj1iiRrd1EkGgAcQZ-E


import xml.etree.cElementTree as ET
"""

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far ",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)

print("Type ", type(an))
print("Dir ", dir(an))
print("Type ", type(an.x))
print("Type", type(an.party))


