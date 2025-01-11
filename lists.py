#Create a program that takes a list of numbers and prints the sum and average.

# define a function to collect the list from the user
def list_collect():
    # initialize an empty list
    list_of_numbers = []
    # ask the user for the length of the list
    list_length = int(input("Enter the length of the list: "))
    # loop through and populate the list with user input
    for i in range(list_length):
        list_of_numbers.append(int(input("Enter a number: ")))
    print("The list =>", list_of_numbers)
    # return the list
    return list_of_numbers

# define a function to calculate the sum of the list
def list_sum(list_of_numbers):
    # initialize sum to 0
    sum = 0
    # loop through the list and add each number to the sum
    for i in range(len(list_of_numbers)):
        sum += list_of_numbers[i]
    # return the sum
    return sum

# define a function to calculate the average of the list
def list_average(list_of_numbers):
    # return the sum of the list divided by the length of the list
    return list_sum(list_of_numbers) / len(list_of_numbers)

# call the list_collect function to get the list
main_list = list_collect()

# print the sum and average of the list
print(f"The sum of the list is: {list_sum(main_list)}")
print(f"The average of the list is: {list_average(main_list)}")
