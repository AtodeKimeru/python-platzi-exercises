def make_division_by(n):
    return lambda x: x//n

division_by_3 = make_division_by(3)
division_by_5 = make_division_by(5)
division_by_18 = make_division_by(18)

print(division_by_3(18))
print(division_by_5(100))
print(division_by_18(54))
