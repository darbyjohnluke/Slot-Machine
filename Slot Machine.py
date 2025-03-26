import random
print("Welcome to Darby's Slot Machine")
score = 0
moneyspent = 0
while True:
    imput = input("Do you wish to roll the dice? ('Yes/No'): ").lower()
    if imput == "yes":
        slots = ["Apple", "Cherry", "Mango", "Pineapple", "Strawberry", "Tomato", "Pear", "Peach", "Banana", "Apple"]
        def slot1():
            rand1 = random.randint(1, 9)
            return rand1
        def slot2():
            rand2 = random.randint(1, 9)
            return rand2
        def slot3():
            rand3 = random.randint(1, 9)
            return rand3
        slotone = slot1()
        slottwo = slot2()
        slotthree = slot3()

        print(slots[slotone], slots[slottwo], slots[slotthree])
        if slotone == slottwo:
            score += 2
            moneyspent += 1
            print("You've hit a Screener, $1 will bw awarded to your prize money with the other winnings!")
        elif slotone == slotthree:
            score += 2
            moneyspent += 1
            print("You've hit a Ender, $1 will bw awarded to your prize money with the other winnings!")
        elif slottwo == slotthree:
            score += 2
            moneyspent += 1
            print("You've hit a Outro, $1s will bw awarded to your prize money with the other winnings!")
        elif slotone == slottwo == slotthree:
            score += 100
            moneyspent += 10
            print("Congratulations!!! You've hit a Jackpot, $100 will bw awarded to your prize money with the other winnings!")
        else:
            moneyspent += 1
            continue
    elif imput == "no":
        break
    else:
        print("Invalid response, please type Yes/No")
        continue
scoreaftertax = score * 0.7
remaining = scoreaftertax - moneyspent
if score == 0:
    print("Today you've won nothing in rewards!")
    print("You've spent $" + str(moneyspent) + ", and You're taking home: $" + str(score))
elif score > moneyspent:
    print("Today you've earned $" + str(remaining) + " Congratulations!")
    print("You've spent $" + str(moneyspent) + ", and You're taking home: $" + str(scoreaftertax))
elif score < moneyspent:
    print("Today you've lost $" + str(-remaining) + " Better luck next time!")
    print("You've spent $" + str(moneyspent) + ", and You're taking home: $" + str(scoreaftertax))
else:
    print("Today you've broken even in winnings, but lost $" + str(remaining) + " after tax")
    print("You've spent $" + str(moneyspent) + ", and You're taking home: $" + str(scoreaftertax))
print("***The prize money available is shown after tax deductions***")
print("Goodbye!")
print("score =", score)
print("Money Spent: ", moneyspent)
