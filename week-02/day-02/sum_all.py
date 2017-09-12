# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`

ai = [3, 4, 5, 6, 7]

# --- solution 1 ---

def sum_list(ai):
    sum = 0
    for i in ai:
        sum += i
    return sum

print(sum_list(ai))

# --- solution 2 --- (simpler)

print(sum(ai))