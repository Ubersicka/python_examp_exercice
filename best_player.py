best_player = ''
goals = 0
command = input()
while command != "END":
    goal = int(input())
    if goal > goals:
        best_player = command
        goals = goal
    if goals >= 10:
        break
    command = input()
print(f'{best_player} is the best player!')
if goals < 3:
    print(f'He has scored {goals} goals.')
else:
    print(f'He has scored {goals} goals and made a hat-trick !!!')








# name_of_the_player = input()
# count_goals = int(input())
#
# best_player = name_of_the_player
# score_of_the_best = count_goals
#
# while name_of_the_player != 'END':
#     name_of_the_player = input()
#     if name_of_the_player == "END":
#         print(f'{best_player} is the best player!')
#         if score_of_the_best >= 3:
#             print(f"He has scored {score_of_the_best} goals and made a hat-trick !!!")
#             break
#         elif score_of_the_best < 3:
#             print(f"He has scored {score_of_the_best} goals.")
#             break
#     goals = int(input())
#     if goals > score_of_the_best:
#         score_of_the_best = goals
#         best_player = name_of_the_player
#     if goals >= 10:
#         print(f'{best_player} is the best player!')
#         print(f"He has scored {score_of_the_best} goals and made a hat-trick !!!")
#         break
