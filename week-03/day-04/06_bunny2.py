def bunny_ear_sum(bunny_number):
    if bunny_number <= 0:
        return 0
    elif bunny_number == 1:
        return 2
    elif bunny_number % 2 == 0:
        return 3 + bunny_ear_sum(bunny_number - 1)
    elif bunny_number % 2 != 0:
        return 2 + bunny_ear_sum(bunny_number - 1)

print(bunny_ear_sum(1))
