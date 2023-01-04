farm_animal = ['goat', 'horse', 'chicken', 'cow', 'horse']
counter = 0

for animal in farm_animal:
    counter = counter + 1
    sentence = str(counter) + ". " + animal + " is safe in our farm!"

    print(sentence)