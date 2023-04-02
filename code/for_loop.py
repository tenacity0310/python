# excerpted from "Head First Python" in page 38
word="bottles"
# "range (99, 0, -1) indicates that the the number starts from "99", and to the end "1" NOT "0" by decreasing every 1 step. 
# The scope of the whole "for loop" will the extend to the idented code blocks/ suites under the "for_loop"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print ("Take one down.")
    print("Pass it around.")
    if beer_num==1:
        print ("No more bottles of beer on the wall.")
    else: 
        new_num = beer_num -1
        if new_num == 1:
# Although it seems that the new assignment of variable "word" is under the embedded "if condition", its scope will spread the entire coding from top to toe once the if condition is met.
            word = "bottle"
        print (new_num, word, "of beer on the wall.")
    print()

# The following illustrates the usage of "range" function
# Print out more specific expressions of the function range (5)
print (range (5))
for i in range (0,5):
    print (i)
# By invoking the "list()" function, a list of numbers in the "range() function"would be rendered.
# range (5) indicates counting from 0 
print (list (range (5)))
# "range (5,10)" starts from 5 to 9, exclusvie of 10, and the number increase by 1.
print (list (range (5,10)))
# "range (0,10,2)" starts from 0 to 10, exclusvie of 10, and the number increase by 2.
print (list (range (0,10,2)))
# "range (10,0,-2)" starts from 10 to 0, exclusvie of 0, and the number steps down by 2.       
print (list (range (10,0,-2)))
# "range (10,0,2)" will yield nothing but "[]", since this the range is downward from 10 to 0 but the function has to go up 2 steps every time. 
print (list (range (10,0,2)))
# "range (99,0,-1)" starts from 99 to 0, exclusvie of 0, and the number steps down by 1.
print (list (range (99,0,-1)))