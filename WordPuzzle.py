import random


def shuffleWord(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)
    



def printPuzzleQuestion(word,score):
    problemWord=shuffleWord(word)   
    print("\n Arrange the letter to form a valid words")
    print(problemWord)   # print  shuffled word
    userWorld=input("Enter Your Answer")
    print()
    
    
    if userWorld.upper()==word:
        print("Correct✅")
        score+=1
        
    else:
        print("Wrong❌")   
        score-=1
        
    return score    
     
        
        
    
def main():
    print(" ***********WELCOME TO WORDS PUZZLE GAME************* ")
    print()
    print("---------Rules for Game-----------")
    print("\n 1.YOU HAVE 5 CHANCE TO GIVE ANSWER OF EVERY WORD")

    print("\n 2.EVERY RIGHT ANSWER GIVE +1 MARKS AND WRONG ANSWER GIVE -1 MARKS")

    print("\n 3.YOU CAN WRITE SMALL OR CAPITAL LETTER BOTH \n")
   
    print("--------Start Game---------")
    
    
   
        
    score=0
    words=["FATHER","LAPTOP","BOOK","COUNTRY","Mobile"]
    words=random.sample(words,k=len(words))
    
    for word in words:
        score=printPuzzleQuestion(word,score)
       
    print("Your Score is",score)
    print()   
    
main()        
    
     