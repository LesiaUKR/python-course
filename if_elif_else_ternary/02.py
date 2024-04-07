'''
A leap year can be checked by dividing the year by 4.
 If the year is completely divisible, then it is a leap year. 
 A century year on the other hand should be exactly divisible by 400 to be a leap year. 

To check if any century year is a leap year, then instead of checking its divisibility 
by 4, first the number is divided by 100. Then, the quotient obtained is again divided 
by 4. If the remainder thus obtained is 0, then the century year will be considered a 
leap year. 

'''
import calendar

year = int(input("Enter a year: "))

if calendar.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# ternary operator
# <condition true> if <condition> else <condition false>

print("is leap year") if calendar.isleap(year) else print("is not leap year")


a = 2
b = 3

if a >= b:
    minimum = b
else:
    minimum = a

print(minimum)

# ternary operator

minimum = b if a >= b else a
print(minimum)
