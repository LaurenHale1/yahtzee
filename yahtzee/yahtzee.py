import random

def introduction():
    print("""Welcome to this Yahtzee program. The rules are simple. Roll the 5
dice each round. You have up to three rolls per round. After you are
done rolling, pick a category to score in. Try to get a high score!\n""")
    
def options(scores,yahtzee):
      upper=0
      lower=0
      bonus1=0
      bonus2=0
      print(scores)
      for i in range(6):
        if scores[i]!="":
          upper+=int(scores[i])
      if upper>=63:
        bonus1=35
        upper=upper+bonus1
      lower=0
      for i in range(6,13):
        if scores[i]!="":
          lower+=int(scores[i])
      if yahtzee>=2:
        bonus2=100
      total1=lower+upper+bonus1+bonus2
      print("""
      The score as of now is:
      1. Aces            |""",scores[0],"""
      2. Twos            |""",scores[1],"""
      3. Threes          |""",scores[2],"""
      4. Fours           |""",scores[3],"""
      5. Fives           |""",scores[4],"""
      6. Sixes           |""",scores[5],"""
      Upper Total        |""",upper,"""
      Bonus              |""",bonus1,"""
      7. 3-of-a-kind     |""",scores[6],"""
      8. 4-of-a-kind     |""",scores[7],"""
      9. Full House      |""",scores[8],"""
      10. Small Straight |""",scores[9],"""
      11. Large Straight |""",scores[10],"""
      12. Yahtzee        |""",scores[11],"""
      13. Chance         |""",scores[12],"""
      Bonus              |""",bonus2,"""
      Lower Total        |""",lower,"""
      Total              |""",total1,"""
      """)
      return total1
      print("""
      The score as of now is:
      1. Aces            |""",scores[0],"""
      2. Twos            |""",scores[1],"""
      3. Threes          |""",scores[2],"""
      4. Fours           |""",scores[3],"""
      5. Fives           |""",scores[4],"""
      6. Sixes           |""",scores[5],"""
      Upper Total        |""",upper,"""
      Bonus              |""",bonus1,"""
      7. 3-of-a-kind     |""",scores[6],"""
      8. 4-of-a-kind     |""",scores[7],"""
      9. Full House      |""",scores[8],"""
      10. Small Straight |""",scores[9],"""
      11. Large Straight |""",scores[10],"""
      12. Yahtzee        |""",scores[11],"""
      13. Chance         |""",scores[12],"""
      Bonus              |""",bonus2,"""
      Lower Total        |""",lower,"""
      Total              |""",total1,"""
      """)
def firstroll():
    print("\nHere is your first roll:")
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    die3=random.randrange(1,7)
    die4=random.randrange(1,7)
    die5=random.randrange(1,7)
    print([die1,die2,die3,die4,die5])
    return [die1,die2,die3,die4,die5]

def keep(roll1):
    keep=7
    five=[0,1,2,3,4,5]
    print("\nYou can choose which dice to roll again. Please press enter after typing in your number. When you're done, enter 0.\n Your first number for your roll is 1, Second number is 2 etc. ")
    while keep!=0:
        keep=int(input("Which dice do you want to keep? "))
        if keep in five:
            five.remove(keep)
        else:
            print("That is either not an option, or you are already keeping that die.")
    return five

def secondroll(roll1,keep1):
    print("\nHere is your second roll:")
    for i in keep1:
        roll1[i-1]=random.randrange(1,7)
    roll2=roll1
    print(roll2)
    return roll2

def thirdroll(roll2,keep2):
    print("\nHere is your third roll:")
    for i in keep2:
        roll2[i-1]=random.randrange(1,7)
        roll3=roll2
    print(roll3)
    return roll3

def score(pick,final,yahtzee):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    toak=0
    foak=0
    chance=0
    score=0
    for i in final:
        if i==1:
            a+=1
        elif i==2:
            b+=1
        elif i==3:
            c+=1
        elif i==4:
            d+=1
        elif i==5:
            e+=1
        else:
            f+=1
    rolls=[a,b,c,d,e,f]
    #1-6
    if pick in range(1,7):
        for i in final:
            if i==pick:
                score+=i
    #Three of a kind
    elif pick==7:
        for i in rolls:
            if i>=3:
                for j in final:
                    toak+=j
                    score=toak
                
    #Four of a kind
    elif pick==8:
        for i in rolls:
            if i>=4:
                for j in final:
                    foak+=j
                    score=foak
    #Full House
    elif pick==9:
        for i in rolls:
            if i==3:
                for j in rolls:
                    if j==2:
                        score=25
    #Small Straight
    elif pick==10:
        six=[1,2,3,4,5,6]
        for i in final:
            if i in six:
                six.remove(i)
            if six==[1] or six==[2] or six==[5] or six==[6] or six==[1,2] or six==[5,6]:
                score=30         
    #Large Straight
    elif pick==11:
        six=[1,2,3,4,5,6]
        for i in final:
            if i in six:
                six.remove(i)
            if six==[1] or six==[6]:
                score=40
    #Yahtzee
    elif pick==12:
        if final[0]==final[1]==final[2]==final[3]==final[4]:
            score=50
            print("Yahtzee!")
    #Chance
    elif pick==13:
        for i in final:
            chance+=i
            score=chance
    if final[0]==final[1]==final[2]==final[3]==final[4]:
       yahtzee+=1
    return score,yahtzee

def scoresheet(scores,yahtzee):
    upper=0
    lower=0
    bonus1=0
    bonus2=0
    print(scores)
    for i in range(6):
      if scores[i]!="":
        upper+=int(scores[i])
    if upper>=63:
      bonus1=35
      upper=upper+bonus1
    lower=0
    for i in range(6,13):
      if scores[i]!="":
        lower+=int(scores[i])
    if yahtzee>=2:
      bonus2=100
    total=lower+upper+bonus1+bonus2
    print("""
    1. Aces            |""",scores[0],"""
    2. Twos            |""",scores[1],"""
    3. Threes          |""",scores[2],"""
    4. Fours           |""",scores[3],"""
    5. Fives           |""",scores[4],"""
    6. Sixes           |""",scores[5],"""
    Upper Total        |""",upper,"""
    Bonus              |""",bonus1,"""
    7. 3-of-a-kind     |""",scores[6],"""
    8. 4-of-a-kind     |""",scores[7],"""
    9. Full House      |""",scores[8],"""
    10. Small Straight |""",scores[9],"""
    11. Large Straight |""",scores[10],"""
    12. Yahtzee        |""",scores[11],"""
    13. Chance         |""",scores[12],"""
    Bonus              |""",bonus2,"""
    Lower Total        |""",lower,"""
    Total              |""",total,"""
    """)
    return total
    
def main():
    introduction()
    choice=input("Would you like to play a game of Yahtzee? Y/N: ").upper()
    while choice=="Y":
        look=""
        total=0
        yahtzee=0
        scores=["","","","","","","","","","","","",""]
        count=1
        while count!=14:
            print("\nRound",count)
            input("\nPress Enter to roll the dice. ")
            roll1=firstroll()
            ans1=input("\nDo you want to roll any of the dice again? Y/N: ").upper()
            if ans1=="Y":
                keep1=keep(roll1)
                roll2=secondroll(roll1,keep1)
                ans2=input("\nDo you want to roll any of the dice again? Y/N: ").upper()
                if ans2=="Y":
                    keep2=keep(roll2)
                    final=thirdroll(roll2,keep2)
                else:
                    final=roll2
            else:
                final=roll1
            count+=1
            choose=1
            while choose!=0:
                options(scores,yahtzee)
                pick=int(input("Which category do you want to score in? (1-13): "))
                if pick in range(1,14):
                    if scores[pick-1]!="":
                        print("You cannot score in that category again. Pick again.\n")
                    else:
                        choose=0
                else:
                    print("That is not a category. Try again\n")
            print("Dice:",final)
            add,yahtzee=score(pick,final,yahtzee)
            scores[pick-1]=str(add)
            look=input("Would you like to see your score sheet? Y/N: ").upper()
            if look=="Y":
              total=scoresheet(scores,yahtzee)
              print("\nYour total score is:",total)
        print("\nYour total score for the game is",total,"points.")
        choice=input("Would you like to play another game of Yahtzee? Y/N: ").upper()
    input("Press Enter to exit. ")
main()



