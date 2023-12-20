print("\n**********************HANGMAN GAME*********************\n")
import random
words=["YELLOW","PEA","BANANA","COW","RIGHT","WRONG","EA",'NICE',"PAPAYA","ORANGE","RAT","GUAVA","PATATO","MANGO","PINK","JUG","CROW","TEA"]

def hangman(i,user,word):
    print(f"   Sorry!!This alphabet i.e {user} is not in that random word..")
    print(f"   Number of lives you lost:-- {i}")
    print(f"   Number of lives left:-- {6-i}\n")

    if i==1:
        print("          O           \n\n")
    if i==2:
        print("          O           ")
        print("          |           \n\n")

    if i==3:
        print("          O           ")
        print("         /|           \n\n")

    if i==4:
        print("          O           ")
        print("         /|\          \n\n")

    if i==5:
        print("          O           ")
        print("         /|\          ")
        print("         /           \n\n")

    if i==6:
        print("           ______")
        print("             |")
        print("          O__|         ")
        print("         /|\          ----->  HANGMAN")
        print("         / \          \n")
        print(f"   Oops!! You does not guess the random word:-- {word}\n   You lost the game!!!")
        deci=int(input("\nDo you want to play again(Enter 0 or 1):-"))
        if deci==1:
            print()
            play()
        else:
            print("\n   Thanks for playing!!!")


    if i!=6:
        print("--> Guess the word with another alphabet..")
        return



def play():
    word=random.choice(words)
    le=len(word)
    s_word=word
    derive=le*"-"
    lives_lost=0
    print(f"--> Guess the word:--    {derive}")
    while lives_lost<6 and word!=derive:
        user=input("   Enter alphabet for guessing the random word:--  ").upper()
        if user in s_word:
            while user in s_word:
                i=s_word.index(user)
                s_word=list(s_word)
                s_word[i]='*'
                s_word="".join(s_word)
                derive=list(derive)
                derive[i]=user
                derive="".join(derive)
            print(f"   Now your word:--    {derive}\n")

        elif user not in s_word:
            lives_lost+=1
            hangman(lives_lost,user,word)

    if word==derive:
        print(f"   Congratulation!!\n   You guess the word:--    {derive}")
        deci=int(input("   Do you want to play again(Enter 0 or 1):-"))
        if deci==1:
            print()
            play()
        else:
            print("\n   Thanks for playing!!!")


play()