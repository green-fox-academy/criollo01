list_input = [34, 12, 24, 9, 5]

def bubblesort(list_input):
    for i in range(len(list_input)):
        for k in range(len(list_input) -1, i, -1):
            if (list_input[k] < list_input[k - 1]):
                swap(list_input, k, k - 1)
 
def swap(list_input, x, y):
    tmp = list_input[x]
    list_input[x] = list_input[y]
    list_input[y] = tmp

bubblesort(list_input)
print(list_input)