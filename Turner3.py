#Name:Ethan Turner
#Date:September 9th 2016
#Description:A Trivia game of three questions that you can retake as many times as you want.
#Worth 10/10 points, all pieces done and a few extra prints for fun.

#This is the introduction
print("Welcome to Ethan's little trivia game! You will have three questions, and three points. Get them all right and you win!")

#This is to set the loop into action for the first game
Play = "y"
while Play == "y":

#This is the first question and answer, if you provide one of the answers given it will print correct, if not it will print differently
    Question = str(input("What is the country between Spain and France?"))
    Question = str(Question)
    Answer = "Andorra"
    answer = "andorra"
    if Question in [Answer, answer]:
        print("Correct!")
    else:
        print("That is incorrect. The answer is Andorra")
#This sets the score for the first question in order to create a grade
    if Question in [Answer, answer]:
        Score1 = 1
    else:
        Score1 = 0
#This is the second question, if you provide one of the answers given it will print correct, if not it will print differently
    Question2 = input("Who was the richest man to ever live?")
    Answer2 = "Mansa Musa"
    answer2 = "mansa musa"

    if Question2 in [Answer2, answer2]:
        print("Correct!")
    else:
        print("That is incorrect. The answer is Mansa Musa")
#This sets the score for the second question in order to create a grade
    if Question2 in [Answer2, answer2]:
        Score2 = 1
    else:
        Score2 = 0
#This is the third question, if you provide one of the answers given it will print correct, if not it will print differently
    Question3 = int(input("How many vowels are in this sentence?"))
    Answer3 = 12

    if Question3 ==  Answer3:
        print("Correct!")
    else:
        print("That is incorrect. The answer is 12")
#This sets the score for the third question in order to create a grade
    if Question3 == Answer3:
        Score3 = 1
    else:
        Score3 = 0
#This is the fourth and final question, if you provide one of the answers given it will print correct, if not it will print differently
    Question4 = float(input("What is 3 divided by 2?"))
    Answer4 = 1.5

    if Question4 ==  Answer4:
        print("Correct!")
    else:
        print("That is incorrect. The answer is 1.5")
#This sets the score for the fourth question in order to create a grade
    if Question4 == Answer4:
        Score4 = 1
    else:
        Score4 = 0
#This adds the score of all the questions together to make a final score
    TotalScore = Score1 + Score2 + Score3 + Score4
#This formats the grade into a percentage from points
    Grade = float(format(TotalScore/4,'.2f')) * 100

#This will tell you your grade and total score in the trivia game.
    print("Your score was ",TotalScore ,"and your grade was a ", Grade,"%")

#This prompts the user on if they would like to play again, and if not the game will end and say it was fun playing
    Play = str(input("Would you like to try again enter y for yes and n for no"))
    if Play == "n":
        break
print("It was fun playing!")



#http://stackoverflow.com/questions/6762959/if-statement-for-strings-in-python in order to do a string if statement with "IN"