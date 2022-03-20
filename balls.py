import math

number_of_balls = int(input())

points = 0
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_another = 0

for balls in range(number_of_balls):
    color = (input())
    if color == "red":
        points += 5
        count_red += 1
    elif color == "orange":
        points += 10
        count_orange += 1
    elif color == "yellow":
        points += 15
        count_yellow += 1
    elif color == "white":
        points += 20
        count_white += 1
    elif color == "black":
        points /= 2
        count_black += 1
    else:
        count_another += 1
        pass

print(f"Total points: {math.floor(points)}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_another}")
print(f"Divides from black balls: {count_black}")



