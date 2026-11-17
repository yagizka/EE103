notes = ['do', 're', 'mi']
print(notes)

notes.extend(['fa', 'sol', 'la', 'si'])
print(notes)    # ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']


notes.insert(6, 'ti')
print(notes)    # ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti', 'si']

notes[0] = 'DO'
print(notes)

notes[1:3] = ['RE', 'MI']
print(notes)

notes.remove('ti')
print(notes)

last_note = notes.pop()
print(notes, last_note)

notes.pop(2)
print(notes)  

del notes[0]
print(notes) 

notes.reverse()
print(notes) 

notes.sort()
print(notes)

notes.clear()
print(notes) 

total = 0
dummy_range = range(10)
dummy_list_1 = list(dummy_range)
dummy_list_2 = []
for i in range(10):
    dummy_list_2.append(i)
print(dummy_list_1 == dummy_list_2)  # True
for value in dummy_list_1:
    total += value
print("Total: ", total)  # Total: 45

dummy_list = [x**2 for x in range(10)]   # [0,1,4,9,16,25,36,49,64,81]

for index, value in enumerate(dummy_list):
    print(index)
    print(value)


def lenght_square(L):
    square_list = []
    for x in L:
        square_list.append(x**2)
        return (len(L), len(square_list))
print(lenght_square([1, 2, 3, 4, 5]))  # (5, 5)



