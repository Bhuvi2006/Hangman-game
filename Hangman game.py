import random
name=input("Enter your name: ")
print("Welcome To The World Of Hangman (Movies) ")
print("Try to Guess within '10', All the best!",name) 
words=["friends","master","maattrran","teddy","madras","madrasapattinam","jeans","jail","sitaramamam","theri","three","pizza","thegidi","boys","ghajini","pokiri","jilla","ghilli","kaithi","pichaikkaran","beast","sooraraipottru","okkanmani","lovetoday","alaipayuthey","thiruchitrambalam","mersal"]
letters=[]
count=10

choice=random.choice(words).lower()
while count>0 :
    global wp 
    guess=input("Enter your letter:  ").lower()
    if guess in choice:
        letters.append(guess)
        wp=""	
        for letter in choice:
            if letter in letters:
                wp += letter
            else:
                wp +="  _  "
        print(wp)
    if wp == choice:
        print("Congragulations",name,"you guessed the correct word !!!  ")
        print("Enter y to play again, n to stop  ")
        x=input("Do you want to play again?")
        if x=="n":
            break
    if guess not in choice:
                count-=1
                if count==9:
                    print("--Only 9 chances left--")
                    print("  ----------  ")
                elif count == 8:
                    print("--Only 8 chances left--")
                    print("  ---------  ")
                    print("     O      ")
                elif count == 7:
                    print("--Only 7 chances left--")
                    print("  ---------  ")
                    print("     O      ")
                    print("     |      ")
                elif count == 6:
                    print("--Only 6 chances left")
                    print("  ---------  ")
                    print("    O      ")
                    print("    |      ")
                    print("   /       ")
                elif count == 5:
                    print("--Only 5 chances left--")
                    print("  ---------  ")
                    print("       O      ")
                    print("       |   ")
                    print("      / \     ")
                elif count == 4:
                    print("-- Only 4 chances left--")
                    print("  ----------  ")
                    print("   \  O      ")
                    print("      |      ")
                    print("     /  \     ")
                elif count== 3:
                    print("--Only 3 chances left--")
                    print("  ----------  ")
                    print("   \ O /    ")
                    print("     |      ")
                    print("    / \     ")
                elif count  == 2:
                    print("--Only 2 chances left-")
                    print("  ----------  ")
                    print("   \ O /   ")
                    print("     |      ")
                    print("    / \     ")
                elif count == 1:
                    print("Last chance left ")
                    print("  ---|------  ")
                    print("   \ O /   ")
                    print("     |      ")
                    print("    / \     ")
                elif count == 0:
                    print("  ---|-----  ")
                    print("     0   ")
                    print(" ======== ")
                    print("    /|\      ")
                    print("    / \     ")
                    print("As you left the last chance , the man left  the world......")
                    print("Save the next man, if you can ")
                    print("The word which killed the man is",choice)
                    break
                    
                    
     
