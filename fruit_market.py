strawbery_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberries_quantity = float(input())
strawbery_quantity = float(input())

raspberries_price = strawbery_price / 2
orange_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_price = (bananas_price * banana_quantity) + \
              (orange_price * orange_quantity) + \
              (raspberries_price * raspberries_quantity) + \
              (strawbery_price * strawbery_quantity)

print (f'{total_price:.2f}')
