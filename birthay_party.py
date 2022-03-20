# Първа задача е с обикновенно смятане

rent = float(input())

cake = rent * 0.20
drink = cake - cake * 0.45
animator = rent / 3

total = rent + cake + drink + animator

print(f"{total:.1f}")
