#1
a = str(input('Enter the text: '))
b=0
if a[0]=='е':
    b+=1
for i in range(len(a)-1):
    if a[i] == ' ':
        if a[i+1]=='е':
            b+=1
    i+=1
print("amount of words starting with 'e': " + str(b))

#2
a = str(input('Enter the text: '))
b = 0
for i in a:
    if i == ':':
        a = a.replace(':', '%')
        b += 1
print(a)
print(b)

#3
a = str(input('Enter the text: '))
b = 0
for i in a:
    if i == '.':
        a = a.replace('.', ' ')
        b += 1
print(a)
print(b)

#4
a = str(input('Enter the text: '))
b = 0
for i in a:
    if i == 'a':
        a = a.replace('a', 'o')
        b += 1
print(b)

#5
a = str(input('Enter the text: '))
print(a.upper())

#6
x = str(input('Enter the text: '))
y = 0
for i in a:
    if i == 'a':
        a.replace('a', ' ')
        y += 1
print(y)

#7 -

#8
a = str(input('Enter the text: '))
b = 1
for i in a:
    if i == ' ':
        newa = a.split(' ')
        b += 1
print(b)

#9
word = str(input('Enter the word that will be counted: '))
a = str(input('Enter the text: '))
b = a.count(word)
print(b)

#10
a = str(input('Enter the text: '))
b = a.title()
print(b)

#11 -

#12
a = str(input("Enter the text: "))
b = a.split(" ")
c = 0
d = list(a)
for i in range(len(d)):
    if d[i] == " ":
        if d[i-1] == "I":
            print(b[c])
            c+= 1
if d[len(d)-1] == "I":
    print(b[len(b)-1])

#13 -

#14
a = str(input('Enter the text: '))
for i in a.split():
    if i.count('a') == True:
        if i.endswith('i') == True:
            print(i)

#15
a = str(input('Enter the text: '))
b = 0
for i in a:
    if i == 't':
        b += 1
print(b)

