# Трета задача е с условие в условието.
fruit = input()
size_of_the_set = input()
number_of_orders = int(input())
price = 0
if fruit == "Watermelon":
    if size_of_the_set == "small":
        price = 2 * 56
    elif size_of_the_set == "big":
        price = 5 * 28.70
if fruit == "Mango":
    if size_of_the_set == "small":
        price = 2 * 36.66
    elif size_of_the_set == "big":
        price = 5 * 19.60
if fruit == "Pineapple":
    if size_of_the_set == "small":
        price = 2 * 42.10
    elif size_of_the_set == "big":
        price = 5 * 24.80
if fruit == "Raspberry":
    if size_of_the_set == "small":
        price = 2 * 20
    elif size_of_the_set == "big":
        price = 5 * 15.20

total_price = number_of_orders * price
if total_price < 400:
    pass
elif total_price <= 1000:
    total_price -= total_price * 0.15
else:
    total_price *= 0.50

print(f'{total_price:.2f} lv.')
