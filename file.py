print("Addition")
def addition(x, y):
    result = x + y
    print(result)
    print()
addition(984,48)
print("Subtraction")
def subrtaction(x, y):
    result = x - y
    print(result)
    print()
subrtaction(984, 48)
print("Multiplication")
def multiplication(x, y):
    result = x * y
    print(result)
    print()
multiplication(984, 48)
print("Division")
def division(x, y):
    result = x / y
    print(result)
division(984,48)


score = 0

print("")

# print("******************************* ")
# print("**** MY PYTHON  QUIZ GAME****** ")
# print("*******************************")
# print()

# request = input("Do you want to play my quiz game?yes/no ")
#
# if request.lower() == 'yes':
#     if request.lower() == 'no(exit)':
#
#         answer = input("what is the past tense of learn")
#         if answer.lower()
# import time
# print("This is the timer")
# # Ask to Begin
# start = input("Would you like to begin Timing? (y/n): ")
# if start == "y":
#     timeLoop = True
# if start == "n":
#     timeLoop = False
# # Variables to keep track and display
# Sec = 0
# Min = 0
# # Begin Process
# timeLoop = start
# while timeLoop:
#     Sec += 1
#     print(str(Min) + " Mins " + str(Sec) + " Sec ")
#     time.sleep(1)
#     if Sec == 60:
#         Sec = 0
#         Min += 1
#         print(str(Min) + " Minute")
#         break
#
# "Program will cancel when user presses X button"

# import explanation
# score =0
# def checkAnswer(userAnswer ,*correctAnswer):
#     if userAnswer in correctAnswer:
#         print("")
#     else:
#         print("")
#
#
# print()
# while True:
#     print("1. Play the game.")
#     print("2.Explain the concept of the game")
#     print("3.Exit")
#     choice = input("Enter your choice")
#     if choice =="1":
#         print("Okay.you can continue.")
#     elif choice =="2":
#         print(explanation,explanation)
#     if choice =="3":
#         print("exiting")
#         break
#
#
#     word1 ="big"
#     print("The first word is:")
#     import time
#     print(word1)
#     # start the countdown timer
#     start_time = time.time()
#     answer = input("Enter your answer: ")
#     end_time = time.time()
#     time_taken = end_time - start_time
#
#
#     checkAnswer(answer, "huge", "large")
#
#     if answer == "huge" or answer =="large":
#        print("Your answer is correct.")
#        score += 5
#
#    else:
#        print("Your answer is incorrect.The right answer is either HUGE or LARGE:")
#        print(f"You took{time_taken} seconds ")
#     word2 = "smart"
#     print("The second word is:")
#     import time
#     print(word2)
#     start_time =time.time()
#     answer = input("Enter the synonym:")
#     end_time =time.time()
#     time_taken = end_time - start_time
#
# checkAnswer(answer, "Intelligent","brilliant")
# if answer =="Intelligent" or answer =="brilliant":
#     print("Your answer is correct")
#     score += 5
# else:
#     print("Your answer is incorrect.The correct is either INTELLIGENT or BRILLIANT.")
#     print(f"You took {time_taken} seconds.")
#     word4 = "small"
#     import time
#     print(word4)
#     start_time = time()
#     answer = input("Enter the synonyms:")
#     end_time = time.time()
#     time_taken =end_time -start_time
#     checkAnswer(answer, "pretty", "attractive")
#     if answer == "pretty" or answer == "attractive":
#         print("Your answer is correct.")
#         score += 5
#
#     else:
#         print("Your answer is incorrect.the correct answer is either PRETTY or ATTRACTIVE")
#         print(f"You took {time_taken} second")
#         print("SMALL")
#         print("The fourth word is:")
#         import time
#         print(word4)
#         start_time = time.time()
#         time_taken = end_time - start_time
#         checkAnswer(answer, "tiny", "little")
#         if answer == "tiny" or answer == "little":
#             print("Your answer is correct.")
#             score += 5
#         else:
#             print("Your answer is incorrect.The correct answer is either TINY or LITTLE")
#             print(f"You took{time_taken} second.")
#             word5 = "NICE"
#             print("The fifth word is:")
#             print(word5)
#             start_time = time.time()
#             time_taken = end_time - start_time
# checkAnswer(answer,"afraid")
# if answer == "afraid":
# print("Your answer is correct.")
# score += 5
# else:
# print("Your answer is incorrect.The correct answer is either AFRAID")
# print(f"You took{time_taken} second.")
# word7 = "MEAN"
# print("The seventh word is:")
# print(word7)
# start_time = time.time()
# answer = input("Enter the synonyms")
# time_taken = end_time - start_time
# checkAnswer(answer ,"wicked")
#      if answer == "afraid":
#                     print("Your answer is correct.")
#                     score += 5
# else:
#                     print("Your answer is incorrect.The correct answer is either AFRAID")
#                     print(f"You took{time_taken} second.")
#                     word7 = "MEAN"
#                     print("The seventh word is:")
#                     print(word7)
#                     start_time = time.time()
#                     answer = input("Enter the synonyms")
#                     time_taken = end_time - start_time
#                     checkAnswer(answer, "wicked")
#                     if answer == "wicked":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is either WICKED")
#                         print(f"You took{time_taken} second.")
#
#                         word8 = "EASY"
#                         print("The eighth word is:")
#                         print(word8)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "simple")
#                     if answer == "easy":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is  simple")
#                         print(f"You took{time_taken} second.")
#
#                         word9 = "DARK"
#                         print("The NINTH word is:")
#                         print(word9)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "dull", "dim")
#                     if answer == "dull" or answer =="dim":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is either DULL or DIM.")
#                         print(f"You took{time_taken} second.")
#                         word10 = "LOVE"
#                         print("The TENTH word is:")
#                         print(word10)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "adore")
#                     if answer == "adore":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is either ADORE")
#                         print(f"You took{time_taken} second.")
#                         word11 = "HELP"
#                         print("The ELEVENTH word is:")
#                         print(word11)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "ASSIST")
#                     if answer == "assist":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is assist")
#                         print(f"You took{time_taken} second.")
#                         word12 = "ANGRY"
#                         print("The twelfth word is:")
#                         print(word12)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "furious")
#                     if answer == "furious":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is furious")
#                         print(f"You took{time_taken} second.")
#                         word13 = "BEGIN"
#                         print("The seventh word is:")
#                         print(word13)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "pleasant")
#                     if answer == "pleasant" or answer == "pleasant":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is either START")
#                         print(f"You took{time_taken} second.")
#                         word14 = "commence"
#                         print("The fourteen word is:")
#                         print(word14)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "continue")
#                     if answer == "kind" or answer =="pleasant":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is CONTINUE")
#                         print(f"You took{time_taken} second.")
#                         word15 = "WEALTHY"
#                         print("The fifteenth word is:")
#                         print(word15)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "rich")
#                     if answer == "kind" or answer == "pleasant":
#                         print("Your answer is correct.")
#                         score += 5
#                     else:
#                         print("Your answer is incorrect.The correct answer is RICH")
#                         print(f"You took{time_taken} second.")
#                         word16 = "DIFFICULT"
#                         print("The SIXTEENTH word is:")
#                         print(word16)
#                         start_time = time.time()
#                         answer = input("Enter the synonyms")
#                         time_taken = end_time - start_time
#                         checkAnswer(answer, "HARD")
#                         if answer == "HARD":
#                             print("Your answer is correct.")
#                             score += 5
#                         else:
#                             print("Your answer is incorrect.The correct answer is HARD")
#                             print(f"You took{time_taken} second.")
#                             word17 = "RESCUE"
#                             print("The SEVENTEENTH word is:")
#                             print(word17)
#                             start_time = time.time()
#                             answer = input("Enter the synonyms")
#                             time_taken = end_time - start_time
#                             checkAnswer(answer, "SAVE")
#                         if answer == "SAVE":
#                             print("Your answer is correct.")
#                             score += 5
#                         else:
#                             print("Your answer is incorrect.The correct answer is SAVE")
#                             print(f"You took{time_taken} second.")
#                             word18 = "UNDER"
#                             print("The EIGHTEENTH word is:")
#                             print(word18)
#                             start_time = time.time()
#                             answer = input("Enter the synonyms")
#                             time_taken = end_time - start_time
#                             checkAnswer(answer, "BELOW")
#                         if answer == "BELOW":
#                             print("Your answer is correct.")
#                             score += 5
#                         else:
#                             print("Your answer is incorrect.The correct answer is BELOW")
#                             print(f"You took{time_taken} second.")
#                             word19 = "UNHAPPY"
#                             print("The NINETEENTH word is:")
#                             print(word19)
#                             start_time = time.time()
#                             answer = input("Enter the synonyms")
#                             time_taken = end_time - start_time
#                             checkAnswer(answer, "SAD")
#                         if answer == "SAD":
#                             print("Your answer is correct.")
#                             score += 5
#                         else:
#                             print("Your answer is incorrect.The correct answer is SAD")
#                             print(f"You took{time_taken} second.")
#                             word20 = "QUICK"
#                             print("The TWENTY word is:")
#                             print(word20)
#                             start_time = time.time()
#                             answer = input("Enter the synonyms")
#                             time_taken = end_time - start_time
#                             checkAnswer(answer, "FAST")
#                         if answer == "FAST":
#                             print("Your answer is correct.")
# score += 5
# else:
# print("Your answer is incorrect.The correct answer is FAST")
# print(f"You took{time_taken} second.")
#
# else:
# print("OKAY. BYE BYE.")
#


