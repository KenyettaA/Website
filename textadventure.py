# 6.14.2017 Christine and Kenyetta's Text Adventure Project: AoT Survival Game

print("Welcome, to the Attack on Titan Season II Survival Game!")
print("User, what is thy name?")
name = input()

print(name + ", let's begin!")

start = '''
For the past 2 days you have been running away from the titans. Earlier today
 your friends and you have found an abandoned tower that seemed safe from the
 titans for a while. It is now nighttime, so you and your friends are taking
 turns for the night shift.
 Click for more.
'''

print(start)

first = '''
You see one of your friends, Reiner, getting up. He's about to take over Connie's
shift. He asks, "Would anyone like to join?"
'''

print("Type '1' to join him or '2' to stay.")
answer1 = input()
if answer1 == "1":
    print("You reply, 'I would LOVE to go with you!' You and Reiner head downstairs.")

    print("You and Reiner walk downstairs in silence. As he opens the door, you notice")
    print(" a fat titan looking hungry. What would you do?")
    print("1. Close the door 2. Scream 3. Run upstairs to get help 4. Faint")
    answer2 = input()
    if answer2 == "1":
        print("As you attempt to force the door closed, the titan rigorously destroys")
        print(" the door onto you. You get squished then you die from the pain.")
    elif answer2 == "2":
        print(name+", you idiot. Stop screaming and do something next time. You died.")
    elif answer2 == "3":
        print("You yell at Reiner to hold onto the door as you run upstairs, calling")
        print(" 'Berthrolt! Connie! GET THE $%^& OUT! THERE IS A MO#$%^**&%$@ TITAN")
        print(" THAT'S ABOUT TO BITE OUR A$% OFF")

        print("The boys come running downstairs; Berthrolt with a pitchfork and Connie with an axe")
        print(" They help you get Reiner free and then you all kill the titan")
        print(" After that exhausting night you all have a good night's sleep and the next day you return")
        print(" to headquarters. Good job! You survived the game!")

    elif answer2 == "4":
        print("While you were unconcious, Reiner died, the others upstairs died, then")
        print(" you died. You all met in Heaven. Have a wonderful afterlife.")
    else:
        print(name+", you idiot, you were supposed to choose from 1, 2, 3, or 4.")
        print("Stupid people will not survive this world. You're dead.")


elif answer1 == "2":
    print("Nobody answers. Reiner huffs and head downstairs by himself.")

    print("You hear the creak of the door downstairs, but you were too busy ")
    print(" searching for food to take notice of Connie shaking your shoulders.")
    print(" You look up as you hear Reiner's cry for help and the loud noises ")
    print(" from outside. What would you do?")
    print("1. Continue to look for food 2. Look out the window 3. Run downstairs 4. Faint")
    answer3 = input()
    if answer3 == "1":
        print("You selfish piece of trash. Reiner got killed instantly and the titan")
        print(" came upstairs and ate everyone else including you and your tuna can.")
    elif answer3 == "2":
        print(name+", you dummie. As you stick your head out of the window, you see")
        print(" a giant throat ready to swallow you. You died from losing your head.")
    elif answer3 == "3":
        print("You and the others create a mini stampede on the stairway, with you")
        print(" leading the way. You see an axe next to Reiner but his arm is getting")
        print(" bitten by the titan. What would you do?")

        print("1. Run for the axe 2. Run to Reiner 3. Run back upstairs 4. Try to close the door.")
        answer5 = input()
        if answer5 == "1":
            print("You retreive the axe and yell a war cry. You swing the axe as far as possible")
            print(" and aim for the titan's eye. It strikes accurately and the titan lets out a ")
            print(" low groan. Reiner pulled his arm out and slammed the door close with Berthroldt")
            print(" and Connie. Sasha, Krista and Ymir from upstairs gives a shout before sliding")
            print(" down a cannon. You all survive! yaay!")
        elif answer5 == "2":
            print(name+", you baka. Reiner attempts to push you away but your stubborness")
            print(" led you to die before Reiner does. Eventually everyone dies after you.")
        elif answer5 == "3":
            print(" You coward. Everyone downstairs die not long after you close the door")
            print(" upstairs. However, the titan broke down the door to finish its job. ")
            print(" You died.")
        elif answer5 == "4":
            print(" Although a good try, the lack of manpower without Reiner led to the door")
            print(" not being pushed enough. The titan forced its way into the room and kills everyone.")
        else:
            print(name+", you idiot, you were supposed to choose from 1, 2, 3, or 4.")
            print("Stupid people will not survive this world. You're dead.")

else:
    print("You idiot, you were supposed to choose from 1 or 2.")
    print("Stupid people will not survive this world. You're dead.")

'''
Extra Ideas
1. Return to start button (Click to restart)
2. The End statement

'''


# Close window on click.
#exitonclick()
