

import time
import threading 
  
def countdown():
    global my_timer

    my_timer=45
    for i in range(45):
        my_timer-=1
        time.sleep(1)
    print("Time up")
    def name():
        a=input("Enter new Question")
        

count_thread=threading.Thread(target=countdown)
count_thread.start()
#Asking questions
print("--------QUIZ TRIVIA---------")
while my_timer>0:
   
    print("------------------ ONE WORD QUESTIONS ------------------")
    score=0
    q1=print("CD and DVD drives are the examples of")
    a1=input("Enter answer:")

    if a1=='Storage Devices':
        print("Correct answer :)")
        print("\n")
    elif a1=='storage devices':
        print("Correct answer :) ")
        print("\n")
    else:
        print("Wrong answer :(, Correct answer is Storage Devices")
        print("\n")
    if a1.lower()=='storage devices':
        score+=1
    if my_timer==0:
        break

    q2=print("ROM is an example of what type of memory?")
    a2=input("Enter answer:")

    if a2=='Non volatile':
        print("Correct answer :)")
        print("\n")
    elif a2=='non volatile':
        print("Correct answer :)")
        print("\n")
    else:
        print("Wrong answer :(. Correct answer is Non volatile")
        print("\n")
    if a2.lower()=='non volatile':
        score+=1
    if my_timer==0:
        break 
  
    q3=print("A permanent memory is called")
    a3=input("Enter answer:")
    if a3=='ROM':
        print("Correct answer")
        print("\n")
    elif a3=='rom':
        print("Correct answer")
        print("\n")
    else:
        print("Wrong answer, Correct answer is ROM")
        print("\n")
    if a3.lower()=='rom':
        score+=1
    if my_timer==0:
        break 

    q4=print("Which memory does not store data permanantly?")
    a4=input("Enter answer:")
    if a4=='RAM':
        print("Correct answer")
        print("\n")
    elif a4=='ram':
        print("Correct answer")
        print("\n")
    else:
        print("Wrong answer, Correct answer is RAM")
        print("\n")
    if a4.lower()=='ram':
        score+=1
    if my_timer==0:
        break 

    
    q5=print("Which is the first computer in the world?")
    a5=input("Enter answer:")
    if a5=='ENIAC computing system':
        print("Correct answer")
        print("\n")
    elif a5=='eniac computing system':
        print("Correct answer")
        print("\n")
    else:
        print('Wrong answer, Correct answer is eniac computing system')
        print("\n")
    if a5.lower()=='eniac computing system':
        score+=1
    if my_timer==0:
        break 
    

    print("------------------MCQ QUESTIONS------------------")

#Q1   
    a1 = input("Which movie has the highest box office collection? \na)Avengers Endgame \nb)Titanic \nc)Avatar \nd)The Matrix \nAnswer: ")
    if a1 == "c" or a1 == "Avatar" :
        score +=1
        print("Correct answer!")
        print("\n")
    else:
        print("Incorrect :(  , the correct answer is Avatar")
        print("\n")
    if my_timer==0:
        break 

#Q2
    a2 = input("This actor got an oscar for his performance in the movie Revenant? \na)Tom hardy \nb)Leonardo DiCaprio \nc)Denzel Washington \nd)Ben Affleck \nAnswer: ")
    if a2 == "b" or a2 == "Leonardo DiCaprio" :
            score +=1
            print("Correct answer!")
            print("\n")
    else:
            print("Incorrect :( , the correct answer is Leonardo DiCaprio")
            print("\n")
    if my_timer==0:
        break 

#Q3
    a3 = input("In the matrix what colourpill does Neo take? \na)blue \nb)white \nc)black \nd)red  \nAnswer: ")
    if a3 == "d" or a3 == "red" :
            score +=1
            print("Correct answer!")
            print("\n")
    else:
            print("Incorrect :( ,  the correct answer is red")
            print("\n")
    if my_timer==0:
        break 

#Q4
    a4 = input("How many suns does Luke’s home planet of Tatooine have in Star Wars? \na)4 \nb)2 \nc)3 \nd)5 \nAnswer: ")
    if a4 == "b" or a4 == "2" :
            score +=1
            print("Correct answer!")
            print("\n")
    else:
            print("Incorrect :( ,  the correct answer is 2")
            print("\n")
    if my_timer==0:
        break 

#Q5

    a5 = input  ("Who played the Green Goblin in 2002 box-office smash Spider-Man? \na) William Dafoe \nb)James franco \nc)Dane DeHaan \nd)Jamie foxx \nAnswer: ")
    if a5 == "a" or  a5== " William Dafoe" :
            score +=1
            print("Correct answer!")
            print("\n")
    else:
            print("Incorrect :( ,  the correct answer isWilliam Dafoe ")
            print("\n")
    if my_timer==0:
        break 


    print("------------------TRUE AND FALSE------------------")

#Q1
    a1 = input("1) a strawberrry has 200 seeds (T/F): ")
    if a1.lower() == "t" or a1.lower() == "true":
        score += 1
        print("correct!")
        print("\n")
    else:
        print("Wrong Answer")
        print("\n")
    if my_timer==0:
        break 
#Q2
    a1 = input("2) potatoes are the most popular fruit in the world (T/F): ")
    if a1.lower() == "f" or a1.lower() == "false":
        score += 1
        print("correct! It was actually tomatoes.")
        print("\n")
    else:
        print("Wrong Answer")
        print("\n")
    if my_timer==0:
        break 

#Q3
    a1 = input("3) carrots help you see better in the dark (T/F): ")
    if a1.lower() == "f" or a1.lower() == "false":
        score += 1
        print("correct!carrots dont actually help you see better in the dark.")
        print("\n")
    else:
        print("Wrong Answer")
        print("\n")
    if my_timer==0:
         break

#Q4
    a1 = input("4) kiwi contain more vitamin c  then oranges (T/F): ")
    if a1.lower() == "t" or a1.lower() == "true":
        score += 1
        print("correct!")
        print("\n")
    else:
        print("Wrong Answer")
        print("\n")
    if my_timer==0:
        break

#Q5
    a1 = input("5) beetroot were the first vegetable to be grown in space (T/F): ")
    if a1.lower() == "f" or a1.lower() == "false":
        score += 1
        print("correct!it was actually patatoes.")
        print("\n")
    else:
        print("Wrong Answer")
        print("\n")
    if my_timer==0:
         break
    break
print("Your score is", score,'/15')
print("Thank You For attempting our Quiz")



    










