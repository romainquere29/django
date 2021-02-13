age = 14
name = "Romain"
print("hello")
print(age)

print(f"My name us {name} and my age is {age}")

if (age > 18):
    print('You\'re adult')
else:
    print('You\'re still a child')

todayIsCold = False

if todayIsCold:
    print ('today is cold')

dognames = ["dog1","Fido","Tohr"]
dognames.insert(1,"Jane")
print(dognames)
print(len(dognames))
print(dognames[2])
del(dognames[2])
print(len(dognames))


for dog in dognames:
    dog = 'name is : '+dog
    print(dog)

for element in range(1,10):
    print(element)

age = 0
while age < 18:
    print(age)
    age += 1

print('start loop challenge')
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
for element in numbers:
    if element > 90:
        print(element)


dogs = {"Fido":8, "Saly":13, "Sean":4}
print(dogs)
print(dogs["Saly"])
del(dogs["Fido"])
dogs["Sarah"] = 6
print(len(dogs))
print(dogs)


words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for indice in range(0,len(words)):
    print(indice)
    cooldictionary[words[indice]]=definitions[indice]
print(cooldictionary)
print(cooldictionary["Spange"])