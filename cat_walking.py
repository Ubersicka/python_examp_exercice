# Втора задача, се използва if фунцкията.

walking_in_min = int(input())
walking_count = int(input())
calories_for_the_day = int(input()) * 0.50

total_min = walking_in_min * walking_count
burn_calories = total_min * 5

if burn_calories >= calories_for_the_day:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.')
