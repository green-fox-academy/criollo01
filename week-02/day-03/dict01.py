students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

# def candies_number():

def student_candy_ate():
        for i in range(len(students)):
                print(students[i]['name'] + " : " + str(students[i]['candies']) )
student_candy_ate()

def sum_of_candies(students):
        candy_counter = 0
        for student in students:
                candy_counter += student["candies"]
        return candy_counter

print(sum_of_candies(students))

def sum_of_people_who_have_less():
        sum=0
        for i in range(len(students)):
                if students[i]['candies']<5:
                        sum += students[i]['age']
        print("The sum is: ", sum)

sum_of_people_who_have_less()