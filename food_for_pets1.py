number_of_days = int(input())
quantity_of_foods = float(input())

dog_eaten_food = 0
cat_eaten_food = 0
eaten_biscuits = 0

for days in range(1, number_of_days + 1):
    dog_day_one = int(input())
    cat_day_one = int(input())
    dog_eaten_food += dog_day_one
    cat_eaten_food += cat_day_one
    if days % 3 == 0:   # Модулно деление на 3 като това, ще влиза в проверката, само на всеки 3ти ден.
        eaten_biscuits += (dog_day_one + cat_day_one) * 0.10

total_dog_and_cat_eaten = dog_eaten_food + cat_eaten_food
total_food_eaten_in_percent = total_dog_and_cat_eaten / quantity_of_foods * 100
dog_eaten_food_in_percent = dog_eaten_food / total_dog_and_cat_eaten * 100
cat_eaten_food_in_percent = cat_eaten_food / total_dog_and_cat_eaten * 100

print(f'Total eaten biscuits: {round(eaten_biscuits)}gr.')
print(f'{total_food_eaten_in_percent:.2f}% of the food has been eaten.')
print(f'{dog_eaten_food_in_percent:.2f}% eaten from the dog.')
print(f'{cat_eaten_food_in_percent:.2f}% eaten from the cat.')
