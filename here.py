
#define the function
def practice_function(number):
    for x in range(number):
        print("Happy Birthday Kenyetta!")

#call the function
practice_function(7)

#how to do a while loop
done = False
count = 5

while not done:
    print("This is a while loop")
    count -=1
    if count <0:
        done = True
