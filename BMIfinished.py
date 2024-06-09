import matplotlib.pyplot as plt
import pandas
import csv

def register():
    with open("user.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        email = input("Enter your email. : ")
        password = input("Enter your password. : ")
        password_confirm = input("Re-enter your password to confirm it : ")
        if password == password_confirm:
            metric_imperial = input("Do you have a preferred measurement system? [M]metric or [I]imperial : ")
            writer.writerow([email, password, metric_imperial])
            print("Successfully registered!")
        else:
            print("Please try again !")


# noinspection PyAssignmentToLoopOrWithParameter
def login():
    email = input("Please enter your email : ")
    password = input("Please enter your password : ")
    with open("user.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("Successfully logged in. ")
            to_cont = input("To continue please type, y : ")
            if to_cont == "y":
                weight = int(input("What is your weight in kilograms : "))
                height = int(input("How tall are you in centimeters : "))
                age = int(input("How old are you : "))
                date = input("What is the current date? : ")
            height_conv = height / 100
            height_squared = height_conv ** 2
            BMI = weight / height_squared
            print("Your BMI is ", BMI, "!")
            with open("bmi.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([BMI, weight, height, age, date])
            have_you = input("Have you ran this program before? y/n : ")
            if have_you == "y":
                df = pandas.read_csv('bmi.csv')
                askgoal = input("Do you have a goal ? y/n : ")
                if askgoal == "y":
                    with open("usergo.csv", mode="a", newline="") as f:
                        writergo = csv.writer(f, delimiter=",")
                        print(df)


def registerim():
    with open("userim.csv", mode="a", newline="") as f:
        writerim = csv.writer(f, delimiter=",")
        emailim = input("Enter your email. : ")
        passwordim = input("Enter your password. : ")
        password_confirmim = input("Re-enter your password to confirm it : ")
        if passwordim == password_confirmim:
            metric_imperialim = input("Do you have a preferred measurement system? [M]metric or [I]imperial : ")
            writerim.writerow([emailim, passwordim, metric_imperialim])
            print("Successfully registered!")
        else:
            print("Please try again !")


def loginim():
    emailim = input("Please enter your email : ")
    passwordim = input("Please enter your password : ")
    with open("userim.csv", mode="r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if row == [emailim, passwordim]:
                print("Successfully logged in. ")
            to_cont = input("To continue please type, y : ")
            if to_cont == "y":
                height = int(input("What is your weight in feet : DO NO ADD TRAILING INCHES eg . 6, 8 : "))
                height_inch = int(input("Enter any trailing inches you had eg. the 8 in 6ft,8in : "))
                heightcalc = height * 12
                height_final = heightcalc + height_inch
                weightim = int(input("How much do you weigh in pounds? : "))
                ageim = int(input("How old are you : "))
                dateim = input("What is the current date? : ")
                bmiprep = height_final ** 2
                bmiprep2 = weightim / bmiprep
                bmiim = bmiprep2 * 703
            print("Your BMI is ", bmiim, "!")
            with open("bmiim.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([bmiim, weightim, height, ageim, dateim])
            have_you = input("Have you ran this program before? y/n : ")
            if have_you == "y":
                df = pandas.read_csv('bmiim.csv')
                askgoal1 = input("Do you have a goal ? y/n : ")
                if askgoal1 == "y":
                    with open("usergo.csv", mode="a", newline="") as f:
                        writergoim = csv.writer(f, delimiter=",")
                        print(df)





which = input("What system of measurement do you want to use ? m/i : ")
if which == "i":
    regiim = input("Have you registered before? y/n : ")
    if regiim == "y":
        loginim()

    if regiim == "n":
        registerim()
if which == "m":
    regi = input("Have you registered before? y/n : ")
    if regi == "n":
        register()
    if regi == "y":
        login()
