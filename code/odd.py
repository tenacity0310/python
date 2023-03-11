# Use fn+ F5 press to run the code
from datetime import datetime
# from datetime = Python’s standard library which is a large stock of software modules providing lots of prebuilt (and high-quality) reusable code.
# import datetime = one submodule from the standard library’s datetime module. 

# The variable odds is defined in terms of "list", which will be enclaosed by square brackets "[]".
# List in pyhton could hold data of any type.
# "=" asssignment operator; variable "odds" are assigned the vaule of a list; variable "right_this_minute" are assigned by the method call datetime.today().second
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33,35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute
print (right_this_minute)

# The 'in' operator checks if one thing is inside another. The 'in' operator returns either 'True' or 'False'
# The colon (:) is important, in that it introduces a new suite of code that must be indented to the right. 
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")

# We can also decompose the varibale right_this_minute in what follows, BUT NOT recommended.
time_now = datetime.today()
right_this_minute_version2 = time_now.minute

print ("Time of today:", time_now)
print ("The minute of the current hour:", right_this_minute_version2)

# Loop over the code, but pause for a few random second as designated by the function time.sleep() and random.radiant()