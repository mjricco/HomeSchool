print "Content-Type: text/plain"
print ""
import os.path
from os import path
import random
gamepath = os.path.dirname(__file__)
lessonpath = os.path.join(gamepath, "Lessons")
Lessons = []
f= open(os.path.join(lessonpath, "AllLessons.txt"),"r+")
f1 = f.readlines()
QuitApplication = False
for x in f1:
    Lessons.append(x.replace("\n",""))
while True:
    print("HomeSchool")
    while True:
        School = input("What school are you in? If you would like to create a new school, type Create. To quit the application, type Quit.").lower()
        if path.exists(School) and School != "lessons":
            break
        elif School == "create":
            NewSchool = input("What is your school's name?").lower()
            if not os.path.exists(NewSchool) and not NewSchool == "quit":
                os.mkdir(NewSchool)
                schooldatapath = os.path.join(gamepath, NewSchool)
                TeacherName = input("What is your name, as students know you?")
                TeacherPassword = input("Give yourself a password.")
                f= open(os.path.join(schooldatapath, "Activity.txt"), "w+")
                f.close()
                f= open(os.path.join(schooldatapath, "Assignments.txt"), "w+")
                f.close()
                f= open(os.path.join(schooldatapath, "OpenMessages.txt"), "w+")
                f.write("- \n")
                f.close()
                f= open(os.path.join(schooldatapath, "Passwords.txt"), "w+")
                f.write(TeacherPassword + "\n")
                f.close()
                f= open(os.path.join(schooldatapath, "Points.txt"), "w+")
                f.write("0 \n")
                f.close()
                f= open(os.path.join(schooldatapath, "Users.txt"), "w+")
                f.write(TeacherName + "\n")
                f.close()
                print("School created.")
            else:
                print("That school already exists.")
        elif School == "quit":
            QuitApplication = True
            break
        else:
            print("That school does not exist.")
    if QuitApplication:
        break
    schooldatapath = os.path.join(gamepath, School)
    Students = []
    Passwords = []
    Points = []
    Activity = []
    Assignments = []
    OpenMessages = []
    f= open(os.path.join(schooldatapath, "Users.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        Students.append(x.replace("\n",""))
    f= open(os.path.join(schooldatapath, "Passwords.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        Passwords.append(x.replace("\n",""))
    f= open(os.path.join(schooldatapath, "Points.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        Points.append(x.replace("\n",""))
    f= open(os.path.join(schooldatapath, "Activity.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        Activity.append(x.replace("\n",""))
    f= open(os.path.join(schooldatapath, "Assignments.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        Assignments.append(x.replace("\n",""))
    f= open(os.path.join(schooldatapath, "OpenMessages.txt"),"r+")
    f1 = f.readlines()
    for x in f1:
        OpenMessages.append(x.replace("\n",""))

    while True:
        User = input("Who are you?")
        if User in Students:
            break
        print("That student does not exist.")
    while True:
        Password = input("What is the password?")
        if Password in Passwords:
            if Students.index(User) == Passwords.index(Password):
                break
        print("Wrong password.")
    while True:
        if Students.index(User) == 0:
            print("Welcome back", User, ". To add a student, type Add Student. To delete a student, type Delete Student. To add an assignment, type Add Assignment. To view assignment progress, type Assignments. To view recent activity, type Activity. To find and edit a student's password, type Find Password. To change a student's points, type Change Points. To add student messages, type Talk. To create a lesson, type Create Lesson. To log out, type Quit.")
            Input = input("What do you want to do?").lower()
            if Input == "add student":
                Points.append(0)
                f=open(os.path.join(schooldatapath, "Points.txt"),"w+")
                i = 0
                while i < len(Points):
                    Message = str(Points[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                OpenMessages.append("Hi!")
                f=open(os.path.join(schooldatapath, "OpenMessages.txt"),"w+")
                i = 0
                while i < len(OpenMessages):
                    Message = str(OpenMessages[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                Students.append(input("What is the student's name?"))
                f=open(os.path.join(schooldatapath, "Users.txt"),"w+")
                i = 0
                while i < len(Students):
                    Message = str(Students[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                Passwords.append(input("Set a password for the student."))
                f=open(os.path.join(schooldatapath, "Passwords.txt"),"w+")
                i = 0
                while i < len(Passwords):
                    Message = str(Passwords[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                Activity.append("You added " + Students[len(Students) - 1] + "to the class.")
                f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                i = 0
                while i < len(Activity):
                    Message = str(Activity[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                print("Student set!")
            elif Input == "delete student":
                StudentToDelete = input("Who do you want to delete?")
                if StudentToDelete == User:
                    print("You can't delete yourself!")
                elif StudentToDelete in Students:
                    if input("ARE YOU SURE? The data can NEVER be recovered.").lower() == "yes":
                        StudentDeleteNumber = Students.index(StudentToDelete)
                        del Students[StudentDeleteNumber]
                        del Points[StudentDeleteNumber]
                        del Passwords[StudentDeleteNumber]
                        del OpenMessages[StudentDeleteNumber]
                        i = len(Assignments)
                        while i > 0:
                            i = i - 1
                            if Assignments[i] == StudentToDelete:
                                del Assignments[i]
                        Activity.append("You deleted " + StudentToDelete + " from the class.")
                        f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                        i = 0
                        while i < len(Activity):
                            Message = str(Activity[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        f=open(os.path.join(schooldatapath, "Points.txt"),"w+")
                        i = 0
                        while i < len(Points):
                            Message = str(Points[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        f=open(os.path.join(schooldatapath, "OpenMessages.txt"),"w+")
                        i = 0
                        while i < len(OpenMessages):
                            Message = str(OpenMessages[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        f=open(os.path.join(schooldatapath, "Users.txt"),"w+")
                        i = 0
                        while i < len(Students):
                            Message = str(Students[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        f=open(os.path.join(schooldatapath, "Passwords.txt"),"w+")
                        i = 0
                        while i < len(Passwords):
                            Message = str(Passwords[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        f=open(os.path.join(schooldatapath, "Assignments.txt"),"w+")
                        i = 0
                        while i < len(Assignments):
                            Message = str(Assignments[i]) + "\n"
                            f.write(Message)
                            i = i + 1
                        f.close()
                        print("Student sucsessfully deleted.")
                        
                else:
                    print("That's not a student.")
            elif Input == "add assignment":
                print("Here are the possible assignments.")
                for i in range(len(Lessons)):
                    print(Lessons[i])
                while True:
                    ChosenLesson = input("What assignment do you want to set?")
                    if ChosenLesson in Lessons:
                        break
                    print("That assignment does not exist.")
                Assignments.append("---" + ChosenLesson)
                while True:
                    ChosenPupil = input("Who do you want to set the assignment for? To add the whole school, type All. If you are finished, type Done.")
                    if ChosenPupil in Students:
                        Assignments.append(ChosenPupil)
                    elif ChosenPupil == "Done":
                        break
                    elif ChosenPupil == "All":
                        i = 1
                        while i < len(Students):
                            Assignments.append(Students[i])
                            i = i + 1
                    else:
                        print("That is not a student.")
                f=open(os.path.join(schooldatapath, "Assignments.txt"),"w+")
                i = 0
                while i < len(Assignments):
                    Message = str(Assignments[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                Activity.append("Added assignment " + ChosenLesson + ".")
                f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                i = 0
                while i < len(Activity):
                    Message = str(Activity[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
            elif Input == "quit":
                break
            elif Input == "assignments":
                i = 0
                while i < len(Assignments):
                    if Assignments[i].find("---") != -1:
                        if i + 1 == len(Assignments):
                            del Assignments[i]
                            i = i - 1
                        else:
                            if Assignments[i + 1].find("---") != -1:
                                del Assignments[i]
                                i = i - 1
                    i = i + 1
                f=open(os.path.join(schooldatapath, "Assignments.txt"),"w+")
                i = 0
                while i < len(Assignments):
                    Message = str(Assignments[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                print("These are the assignments and students who haven't completed them.")
                if len(Assignments) == 0:
                    print("There are no assignments still in progress.")
                else:
                    for i in range(len(Assignments)):
                        print(Assignments[i])
            elif Input == "activity":
                ListScroll = len(Activity)
                while True:
                    for i in range(10):
                        ListScroll = ListScroll - 1
                        if ListScroll >= 0:
                            print(Activity[ListScroll])
                    if input("More?").lower() == "no":
                        break
            elif Input == "find password":
                while True:
                    ChosenPupil = input("Whose password do you want to find?")
                    if ChosenPupil in Students:
                        break
                    print("That isn't a student.")
                print(ChosenPupil + "'s password is " + Passwords[Students.index(ChosenPupil)] + ".")
                if input("Do you want to change it?").lower() == "yes":
                    Passwords[Students.index(ChosenPupil)] = input("What do you want to change it to?")
                    Activity.append(ChosenPupil + "'s password was changed to " + Passwords[Students.index(ChosenPupil)] + ".")
                    f=open(os.path.join(schooldatapath, "Passwords.txt"),"w+")
                    i = 0
                    while i < len(Passwords):
                        Message = str(Passwords[i]) + "\n"
                        f.write(Message)
                        i = i + 1
                    f.close()
                    f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                    i = 0
                    while i < len(Activity):
                        Message = str(Activity[i]) + "\n"
                        f.write(Message)
                        i = i + 1
                    f.close()
            elif Input == "change points":
                while True:
                    ChosenPupil = input("Whose points do you want to change?")
                    if ChosenPupil in Students:
                        break
                    print("That isn't a student.")
                print(ChosenPupil + " has " + Points[Students.index(ChosenPupil)] + " points.")
                ChangeNumber = int(input("How many points do you want to change it by?"))
                Points[Students.index(ChosenPupil)] = int(Points[Students.index(ChosenPupil)]) + ChangeNumber
                Activity.append(ChosenPupil + "'s points were changed by " + str(ChangeNumber) + ".")
                f=open(os.path.join(schooldatapath, "Points.txt"),"w+")
                i = 0
                while i < len(Points):
                    Message = str(Points[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                i = 0
                while i < len(Activity):
                    Message = str(Activity[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
            elif Input == "talk":
                while True:
                    ChosenPupil = input("Whose message do you want to change?")
                    if ChosenPupil in Students:
                        break
                    print("That isn't a student.")
                OpenMessages[Students.index(ChosenPupil)] = input("What should your new message be?")
                Activity.append(User + " sent a new message to " + ChosenPupil + ":" + OpenMessages[Students.index(ChosenPupil)])
                f=open(os.path.join(schooldatapath, "OpenMessages.txt"),"w+")
                i = 0
                while i < len(OpenMessages):
                    Message = str(OpenMessages[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                i = 0
                while i < len(Activity):
                    Message = str(Activity[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
            elif Input == "create lesson":
                LessonName = input("What should you call your lesson?")
                NewLessonData = []
                while True:
                    Input = input("What is next in the lesson? For text, type normally. For a question, start with --Q and put the answer in the next turn all lowercase. For a motivational message, type --M. For a motivational game, type --G. Type Done when finished.")
                    if Input == "Done":
                        break
                    NewLessonData.append(Input)
                f=open(os.path.join(lessonpath, LessonName + ".txt"),"w+")
                i = 0
                while i < len(NewLessonData):
                    Message = str(NewLessonData[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                f=open(os.path.join(lessonpath, "AllLessons.txt"), "a+")
                Message = LessonName + "\n"
                f.write(Message)
                f.close()
                Activity.append(User + " created the lesson:" + LessonName)
                f=open(os.path.join(schooldatapath, "Activity.txt"),"w+")
                i = 0
                while i < len(Activity):
                    Message = str(Activity[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
                print("Lesson created. To use it, quit the whole application then log back in.")
            else:
                print("I do not recognise that.")
        else:
            print("Hello", User, "! To do an assignment, write Assignment. To practice, write Practice. To talk to", Students[0],", write Talk. To log out, type Quit.")
            i = 0
            CurrentPointWinner = "No-one"
            NumberForLeadingPoints = 0
            while i < len(Students):
                if int(Points[i]) == NumberForLeadingPoints:
                    CurrentPointWinner = "No-one"
                elif int(Points[i]) > NumberForLeadingPoints:
                    NumberForLeadingPoints = int(Points[i])
                    CurrentPointWinner = (Students[i])
                i = i + 1
            print(CurrentPointWinner + ", at " + str(NumberForLeadingPoints) + ", currently has the most points.")
            if User == CurrentPointWinner:
                print("Well done! Keep practicing to maintain your lead!")
            else:
                print("You have " + (Points[Students.index(User)]) + " points. With a bit more practice, could you take the lead?")
            print(Students[0] + "'s message: " + OpenMessages[Students.index(User)])
            Input = input("So what shall we do?").lower()
            if Input == "talk":
                Message = input("What do you want to say?")
                Message = User + " sent you a message: " + Message + "\n"
                f=open(os.path.join(schooldatapath, "Activity.txt"),"a+")
                f.write(Message)
                f.close()
                print("Message was sent sucsessfully.")
            elif Input == "practice":
                print("Here are the possible lessons.")
                for i in range(len(Lessons)):
                    print(Lessons[i])
                while True:
                    ChosenLesson = input("What lesson do you want to do?")
                    if ChosenLesson in Lessons:
                        break
                    print("That lesson does not exist.")
                lessonData = []
                f= open(os.path.join(lessonpath, ChosenLesson+".txt"),"r+")
                f1 = f.readlines()
                for x in f1:
                    lessonData.append(x.replace("\n",""))
                Message = User + " has started practicing " + ChosenLesson + "\n"
                f=open(os.path.join(schooldatapath, "Activity.txt"),"a+")
                f.write(Message)
                f.close()
                i = 0
                while i < len(lessonData):
                    if lessonData[i].find("--") == -1:
                        print(lessonData[i])
                    elif lessonData[i].find("--Q") != -1:
                        while True:
                            print(lessonData[i].replace("--Q",""))
                            Answer = str(input("Answer:")).lower()
                            IntendedAnswer = str(lessonData[i + 1])
                            if Answer == IntendedAnswer:
                                break
                            print("Wrong! If you're finding this lesson too difficult, send a message to", Students[0],", who will help you.")
                        i = i + 1
                    elif lessonData[i].find("--M") != -1:
                        print("A special message from",Students[0])
                        if random.randrange(3) == 1:
                            if random.randrange(3) == 1:
                                print("Hi", User, ". I know this is a tough time, but you're pushing through really well! I'm very sure you can complete this lesson, if not, more!")
                            else:
                                print("Hi", User, ". I can see what you do on HomeSchool - from what I'm seeing, you're doing really well! Keep going!")
                        else:
                            if random.randrange(3) == 1:
                                print("Hi", User, ". You're doing super well at this lesson - keep the good work coming!")
                            else:
                                print("Hi", User, ". I'm impessed with your persaverance, esecially during this difficult time. You'll smash this lesson!")
                        print("From", Students[0])
                    elif lessonData[i].find("--G") != -1:
                        print("You're doing really well! You deserve a break.")
                        if random.randrange(3) == 1:
                            print("Random Number Guessing Game")
                            print(Students[0], "is thinking of a number between one and a hundred. You have five guesses to guess the number.")
                            number = random.randrange(1,100)
                            GuessLeft = 5
                            while True:
                                print("Guesses Left:", GuessLeft)
                                Guess = int(input("What will you guess?"))
                                if Guess == number:
                                    print("You guessed correctly! Well done!")
                                    print("Your score is", GuessLeft)
                                    break     
                                elif Guess < number:
                                    print("Too low!")
                                else:
                                    print("Too high!")
                                GuessLeft = GuessLeft - 1
                                if GuessLeft == 0:
                                    print("You ran out of guesses! The secret number was actually", number) 
                                    break
                        else:
                            print("FizzBuzz")
                            print("Say numbers in ascending order. If it is a multiple of three, say fizz. Five, say buzz. Both, say fizzbuzz.")
                            difficulty = int(input("Computer difficulty: Choose from 1 (easy) to 50 (impossible)"))
                            j = 0
                            while True:
                                j = j + 1
                                if j % 3 == 0 and j % 5 == 0:
                                    intendedResponse = "FizzBuzz"
                                elif j % 3 == 0:
                                    intendedResponse = "Fizz"
                                elif j % 5 == 0:
                                    intendedResponse = "Buzz"
                                else:
                                    intendedResponse = str(j)
                                if j % 2 == 1:
                                    if input("Your turn:").lower() == intendedResponse.lower():
                                        print("Correct!")
                                    else:
                                        print("Wrong! The correct answer was ", intendedResponse)
                                        print("The Computer Wins")
                                        break
                                else:
                                    print("Computer's Turn")
                                    if random.randrange(1,100) > difficulty + 50:
                                        if intendedResponse == "Buzz":
                                            print("FizzBuzz")
                                        else:
                                            print("Buzz")
                                        print("Wrong! The correct answer was ", intendedResponse)
                                        print("You win!")
                                        break
                                    else:
                                        print(intendedResponse)
                                    print("Correct!")
                    i = i + 1
                print("You finished! Well done!")
                Message = User + " has finished practicing " + ChosenLesson + ", earning 1 point.\n"
                f=open(os.path.join(schooldatapath, "Activity.txt"),"a+")
                f.write(Message)
                f.close()
                Points[Students.index(User)] = str(int(Points[Students.index(User)]) + 1)
                f=open(os.path.join(schooldatapath, "Points.txt"),"w+")
                i = 0
                while i < len(Points):
                    Message = str(Points[i]) + "\n"
                    f.write(Message)
                    i = i + 1
                f.close()
            elif Input == "quit":
                break
            elif Input == "assignment":
                i = 0
                ValidAssignments = []
                while i < len(Assignments):
                    if Assignments[i] == User:
                        j = i
                        while True:
                            j = j - 1
                            if Assignments[j].find("---") != -1:
                                ValidAssignments.append(Assignments[j].replace("---",""))
                                break
                    i = i + 1
                if ValidAssignments == []:
                    print("You have no assignments. Good work!")
                else:
                    for i in range(len(ValidAssignments)):
                        print(ValidAssignments[i])
                    while True:
                        ChosenLesson = input("What assignment do you want to do?")
                        if ChosenLesson in ValidAssignments:
                            break
                        print("That assignment does not exist.")
                    lessonData = []
                    f= open(os.path.join(lessonpath, ChosenLesson+".txt"),"r+")
                    f1 = f.readlines()
                    for x in f1:
                        lessonData.append(x.replace("\n",""))
                    Message = User + " has started the assignment " + ChosenLesson + "\n"
                    f=open(os.path.join(schooldatapath, "Activity.txt"),"a+")
                    f.write(Message)
                    f.close()
                    i = 0
                    while i < len(lessonData):
                        if lessonData[i].find("--") == -1:
                            print(lessonData[i])
                        elif lessonData[i].find("--Q") != -1:
                            while True:
                                print(lessonData[i].replace("--Q",""))
                                Answer = str(input("Answer:")).lower()
                                IntendedAnswer = str(lessonData[i + 1])
                                if Answer == IntendedAnswer:
                                    break
                                print("Wrong! If you're finding this lesson too difficult, send a message to", Students[0],", who will help you.")
                            i = i + 1
                        elif lessonData[i].find("--M") != -1:
                            print("A special message from",Students[0])
                            if random.randrange(3) == 1:
                                if random.randrange(3) == 1:
                                    print("Hi", User, ". I know this is a tough time, but you're pushing through really well! I'm very sure you can complete this lesson, if not, more!")
                                else:
                                    print("Hi", User, ". I can see what you do on HomeSchool - from what I'm seeing, you're doing really well! Keep going!")
                            else:
                                if random.randrange(3) == 1:
                                    print("Hi", User, ". You're doing super well at this lesson - keep the good work coming!")
                                else:
                                    print("Hi", User, ". I'm impessed with your persaverance, esecially during this difficult time. You'll smash this lesson!")
                            print("From", Students[0])
                        elif lessonData[i].find("--G") != -1:
                            print("You're doing really well! You deserve a break.")
                            if random.randrange(3) == 1:
                                print("Random Number Guessing Game")
                                print(Students[0], "is thinking of a number between one and a hundred. You have five guesses to guess the number.")
                                number = random.randrange(1,100)
                                GuessLeft = 5
                                while True:
                                    print("Guesses Left:", GuessLeft)
                                    Guess = int(input("What will you guess?"))
                                    if Guess == number:
                                        print("You guessed correctly! Well done!")
                                        print("Your score is", GuessLeft)
                                        break     
                                    elif Guess < number:
                                        print("Too low!")
                                    else:
                                        print("Too high!")
                                    GuessLeft = GuessLeft - 1
                                    if GuessLeft == 0:
                                        print("You ran out of guesses! The secret number was actually", number) 
                                        break
                            else:
                                print("FizzBuzz")
                                print("Say numbers in ascending order. If it is a multiple of three, say fizz. Five, say buzz. Both, say fizzbuzz.")
                                difficulty = int(input("Computer difficulty: Choose from 1 (easy) to 50 (impossible)"))
                                j = 0
                                while True:
                                    j = j + 1
                                    if j % 3 == 0 and j % 5 == 0:
                                        intendedResponse = "FizzBuzz"
                                    elif j % 3 == 0:
                                        intendedResponse = "Fizz"
                                    elif j % 5 == 0:
                                        intendedResponse = "Buzz"
                                    else:
                                        intendedResponse = str(j)
                                    if j % 2 == 1:
                                        if input("Your turn:").lower() == intendedResponse.lower():
                                            print("Correct!")
                                        else:
                                            print("Wrong! The correct answer was ", intendedResponse)
                                            print("The Computer Wins")
                                            break
                                    else:
                                        print("Computer's Turn")
                                        if random.randrange(1,100) > difficulty + 50:
                                            if intendedResponse == "Buzz":
                                                print("FizzBuzz")
                                            else:
                                                print("Buzz")
                                            print("Wrong! The correct answer was ", intendedResponse)
                                            print("You win!")
                                            break
                                        else:
                                            print(intendedResponse)
                                            print("Correct!")
                        i = i + 1
                    print("You finished! Well done!")
                    Message = User + " has finished the assignment " + ChosenLesson + ", earning 1 point.\n"
                    f=open(os.path.join(schooldatapath, "Activity.txt"),"a+")
                    f.write(Message)
                    f.close()
                    Points[Students.index(User)] = str(int(Points[Students.index(User)]) + 1)
                    f=open(os.path.join(schooldatapath, "Points.txt"),"w+")
                    i = 0
                    while i < len(Points):
                        Message = str(Points[i]) + "\n"
                        f.write(Message)
                        i = i + 1
                    f.close()
                    i = Assignments.index("---"+ChosenLesson)
                    i = 0
                    while True:
                        i = i + 1
                        if Assignments[i] == User:
                            del Assignments[i]
                            break
                    f=open(os.path.join(schooldatapath, "Assignments.txt"),"w+")
                    i = 0
                    while i < len(Assignments):
                        Message = str(Assignments[i]) + "\n"
                        f.write(Message)
                        i = i + 1
                    f.close()
            else:
                print("I don't recognise that. Try again.")
