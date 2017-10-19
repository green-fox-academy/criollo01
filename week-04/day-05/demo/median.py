
def median(numbers):
    numbers.sort()
    if len(numbers) < 1:
        return None
    if len(numbers) % 2 == 0:
        return (numbers[(int(len(numbers) / 2))] + numbers[int((len(numbers) / 2)) -1]) / 2
    else:
        return numbers[int(len(numbers) / 2)]