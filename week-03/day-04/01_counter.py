# Write a recursive function that takes one parameter: n and counts down from n.
def recursive(n):
    if n == 0:
        return
    print(n)
    recursive(n-1)
    return n

recursive(10)
