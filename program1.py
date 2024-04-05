#######################################################################
# author:Maygoal Behbahani
# date: 12/4/2023
# desc: program 1

########################################################################

# A function to prompt the user for a number and return that value to
# the calling statement.
def info():
    number = int(input("What limit are you interested in? "))
    return number

# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
prime = False
def prime(num):
 prime =False
 factors = []
 if num == 0 or num == 1:
  prime = False
 else:
  for n in range(num) :
   if num % (n+1) == 0:
    factors.append(n+1)
            
 if len(factors) == 2:
  prime = True

  return prime


################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.

number = info()
List = []
for num in range(number):
  
 if prime(num) == True:
  List.append(num)

print(f"There are {len(List)} prime numbers less than {number}")
print(List)