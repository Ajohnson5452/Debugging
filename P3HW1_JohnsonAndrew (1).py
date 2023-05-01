



#Andrew Johnson
#Programming
# Mar 8, 10:10 PM (13 hours ago)






# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
#Changed each input to float, updated the variable for modules 1-6 and deleted the space at the beginning of page
mod_1 = float(input('Enter grade for Module 1: '))

mod_2 = float(input('Enter grade for Module 2: '))

mod_3 = float(input('Enter grade for Module 3: '))

mod_4 = float(input('Enter grade for Module 4: '))

mod_5 = float(input('Enter grade for Module 5: '))

mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
#added a coma after mod_1 and mod2 by adding a space, also added mod_6
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


#fixed grades to lowercase, the same as the variable before and added a f string
#added number of tests
#changed the high to max
#Changed sum because you cannot use sum as a variiable
low = min(grades)

high = max(grades)

module_sum = sum(grades)

number_of_tests = len(grades)

module_avg = (module_sum / number_of_tests)

# determine letter grade for average
#print average to user
#Process variable to get sum & Avg
#Print results after processing
if module_avg >= 90: 
    print('Your grade is: A')
elif module_avg >= 80:   
     print('Your grade is: B')
elif module_avg >= 70:
    print('Your grade is a C')    
elif module_avg >= 60:
    print('Your grade is a D')
else:
    print('Your grade is: F')
    

