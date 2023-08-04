cars = ["audi", "ferrari", "ford focus", "toyota"]
groceries = ['grapes', 'oranges', 'bananas']

def car_adder(thing_to_add, target_list):
    if thing_to_add[0].lower() in 'abcdefg':
        print("This car starts with A-G")
        target_list.append(thing_to_add)
    else:
        print("This item starts with H-Z and we are not allowing it in our club.")


car_adder("BMW", cars)
car_adder("Honda", cars)
car_adder("cinnamon", groceries)
car_adder("zapples", groceries)


print(cars)
print(groceries)