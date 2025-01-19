memory = ['apple', 'milk', 'oats']

def add_1(ingredient_1): 
    memory.append(ingredient_1)
    print(memory)

def add_2(ingredient_2): 
    memory.append(ingredient_2)
    print(memory)
    return memory

def add_3(ingredient_3): 
    global memory
    memory.append(ingredient_3)
    print(memory)

def add_4(ingredient_4): 
    memory.append(ingredient_4)
    print(memory)

Ingredient_1 = input('Ingredient_1')
Ingredient_2 = input('Ingredient_2')
Ingredient_3 = input('Ingredient_3')
Ingredient_4 = input('Ingredient_4')
add_1(Ingredient_1)
add_2(Ingredient_2)
add_3(Ingredient_3)
add_4(Ingredient_4)
print(memory)

