#Question 1

def hello_name(user_name):
    #define what the function does
    print("hello_" + user_name + "!")
#Define the input for user_name in the function hello_name
hello_name('USERNAME')

#Question 2

def first_odds():
#Give the function range
    for num in range(1,100):
        #Define what numbers you want printed using % showing that it has to be odd
        if num % 2 == 1:
            print(num)
first_odds()

#stops at 99 since it was given range from 1 to 100, and to only take the odds from that range

#Question 3

def max_num_in_list(a_list):
    #define the function
    max = a_list[0]
    #Shows the list is not empty
    for i in a_list:
        #starts loop
        if i > max:
            max = i
        #If the biggest numer is greater than the max, it becomes said number
    return max
    #Brings back the max number
print(max_num_in_list([1,2,3,4,5,15]))
#gives the loop a list to sort through, finding the biggest number (15) and returning the max number to the terminal

#Question 4

def is_leap_year(a_year):
    #define the rules of a leap year
    leap = False
    #If these conditions are true for a_year, then it is a leap year
    if (a_year % 4 == 0 and a_year % 100 !=0) or (a_year % 400 == 0):
        leap = "This year is a leap year"
    #If these are not met, then a_year it is not a leap year
    else:
        leap = "This year is not a leap year"
    #Returns the results back to the terminal
    return leap
a_year = int(input('What year is it? '))
print(is_leap_year(a_year))
print(" ")

#Question 5 

def is_consecutive(a_list):   
    int(a_list)
    if not a_list or a_list == 1:
        return False
        print("This list is not in order.")
    #Allows there to not be just 1 number, nor strings or letters
    for i in range (1, len(a_list)):
        #Have to define a_list as an interger so the equations can work
        # defines the range can go from 0 to infinity
        if int(a_list[i]) - int(a_list[i - 1]) != 1:
            return "This list is not in order"
        #Defines that if i - (i-1) does not return 1, it is not in order 
        #[ex: 1,2,4,5, 2-1 = 1, 4-2 = 2, thus not in order]
        #Will return the results of the list
    return ('This list is ordered')
a_list = input("Enter a list: ")
print(is_consecutive(a_list))