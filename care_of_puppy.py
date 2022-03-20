# В пета зада че използва while цикъла с вграждане на if функцията в него.

food_in_kg = int(input())
food_in_grams = food_in_kg * 1000

eaten_food_in_grams = ''
total_eaten_food = 0

while eaten_food_in_grams != "Adopted":
    eaten_food = str(input())
    if eaten_food == 'Adopted':
        if total_eaten_food > food_in_grams:
            print(f'Food is not enough. You need {left_food} grams more.')
            break
        elif total_eaten_food <= food_in_grams:
            print(f'Food is enough! Leftovers: {left_food} grams.')
            break
    eaten_food_int = int(eaten_food)
    total_eaten_food += eaten_food_int
    left_food = abs(food_in_grams - total_eaten_food)
