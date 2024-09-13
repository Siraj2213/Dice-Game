import random

def dicegame():
    print("Welcome to the Roll 3 Dice Game!!!")
    start = str(input("Roll the Dice? (Y/N) "))
    start = start.lower()
    run = 0
    youscore = 0
    AIscore = 0
    while start == "y":
        run = run + 1
        dice1 = int(random.randrange(1,7))
        dice2 = int(random.randrange(1,7))
        dice3 = int(random.randrange(1,7))

        dice4 = int(random.randrange(1,7))
        dice5 = int(random.randrange(1,7))
        dice6 = int(random.randrange(1,7))

        def dicefirst(dicenumber):
            for first in dicenumber:
                if first ==1:
                    print("|         | ",end ="")
                elif first ==2 or first ==3:
                    print("|    o    | ",end ="")
                elif first ==4 or first ==5 or first ==6:
                    print("|  o   o  | ",end="")
            print()
        
        def dicesecond(dicenumber):
            for second in dicenumber:
                if second ==1 or second ==5 or second ==3:
                    print("|    o    | ",end ="")
                elif second ==2 or second ==4:
                    print("|         | ",end ="")
                elif second ==6:
                    print("|  o   o  | ",end="")
            print()

        def dicethird(dicenumber):
            for third in dicenumber:
                if third ==1:
                    print("|         | ",end ="")
                elif third ==2 or third ==3:
                    print("|    o    | ",end ="")
                elif third ==4 or third ==5 or third ==6:
                    print("|  o   o  | ",end="")
            print()
            
        print("Let's roll your dice!!!")
        print("----------- ----------- -----------")
        dicefirst([dice1, dice2, dice3])
        dicesecond([dice1, dice2, dice3])
        dicethird([dice1, dice2, dice3])
        print("----------- ----------- -----------\n")

        print("It's AI's turn to roll the dice!!!")
        print("----------- ----------- -----------")
        dicefirst([dice4, dice5, dice6])
        dicesecond([dice4, dice5, dice6])
        dicethird([dice4, dice5, dice6])
        print("----------- ----------- -----------")

        you = dice1+dice2+dice3
        AI = dice4+dice5+dice6
        print("YOU",f"({you})", f"{dice1},{dice2},{dice3}""  -  "f"{dice4},{dice5},{dice6}" ,f"({AI})" , "AI\n")
        if you > AI:
            print("You win!!!")
            youscore = youscore + 1
        elif you < AI:
            print("AI wins...")
            AIscore = AIscore + 1
        elif you == AI:
            print("Draw?!!")
        winratio = youscore/run
        print(f"GRAND TOTAL AFTER THE RUN " f"#{run}:"," YOU", youscore,"-",AIscore,"AI " , "(Win Ratio:",f"{format(winratio, '.3f')})")
        start = str(input("Roll the Dice? (Y/N) "))
        start = start.lower()
        

    if start == "n":
        gameover = "See ya!!!"
        print(gameover)
    elif start != "n" or "y":
        dicegame()

dicegame()

