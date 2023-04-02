# 3 ways to show the name of the weekday
# first way 
import time
# Display the weekday = time.strftime("%A")
today = time.strftime("%A") 
print (today)
condition = 'Headache'
if today == 'Saturday':
    print ("Let's party! Today is Saturday!")
# The 'elif' conditions intend to add dispaprate conditions for 'if/else' expressions.
elif today == 'Sunday':
    if condition == 'Headache':
        print ('Recover, then rest.')
    else:
        print ('Rest.') 
else:
    print ('Work, work, work.') 


# 2nd way
from datetime import datetime
#print (datetime.today().strftime("%A"))
today = 'Sunday'
condition = 'Headache'
print (today, condition)
if today == 'Saturday':
    print ("Let's party! Today is Saturday!")
# The 'elif' conditions intend to add dispaprate conditions for 'if/else' expressions.
elif today == 'Sunday':
    if condition == 'Headache':
        print ('Recover, then rest.')
    else:
        print ('Rest.') 
else:
    print ('Work, work, work.') 
# 3rd way
import datetime
#print (datetime.date.today().strftime("%A"))
today = 'Wednesday'
condition = 'Headache'
print (today)
if today == 'Saturday':
    print ("Let's party! Today is Saturday!")
# The 'elif' conditions intend to add dispaprate conditions for 'if/else' expressions.
elif today == 'Sunday':
    if condition == 'Headache':
        print ('Recover, then rest.')
    else:
        print ('Rest.') 
else:
    print ('Work, work, work.') 