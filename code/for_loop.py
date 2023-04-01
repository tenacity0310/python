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
