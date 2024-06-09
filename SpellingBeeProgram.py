import csv
import pandas as pd


def main():
    # Asks the teacher for the student they would like to test.
    def validation():
        while True:
            student = int(input("Enter a number between 1 and 25: "))
            if student.isdigit() and 1 <= int(student) <= 25:
                # The reason we have to -1 from the student value is because computers start from 0 so if a user inputs 1 it
                # would be 2 in the computers eyes.
                date = int(input("What is the current week? : "))
                studentFinal = student - 1
                # Pandas has a specified function to read the class_list.csv into a table this makes the data.loc function usable.
                data = pd.read_csv("class_list.csv")
                value = data.loc[studentFinal, 'Word Count']
                valueDeComputerized = value - 1
                wordcountFinal = valueDeComputerized + 10
                with open('words.csv') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    rows = list(csv_reader)
                    words = [row[0] for row in rows[valueDeComputerized:wordcountFinal]]
                    print(words), print("Week" + str(date))
                    export = input("Do you want to export this file as a txt? y/n : ")
                    if export == "y":
                        nameOfFile = "Student " + str(student) + " Week " + str(date) + ".txt"
                        with open(nameOfFile, mode="a") as f:
                            writerN = csv.writer(f, delimiter=",")
                            writerN.writerow([words, "Week", date])
            else:
                print("Invalid input. Please enter a number between 1 and 25.")


def login():
    email = input("Please enter a valid email : ")
    password = input("Please enter a valid password that you used with this email. : ")
    # Opens the CSV file in reader mode so that we can get the username and password
    with open("username&password.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        # This for loop runs through all the rows in our csv file causing it to get a correct email & password.
        for row in reader:
            if row == [email, password]:
                # If the email & password match then the program returns a true value else it returns false.
                choice()
    return False


def register():
    # Makes a new CSV file that creates a place where the teachers email and password will be stored
    with open("username&password.csv", mode="a", newline="") as f:
        # Makes the writer, so we can write to our csv file using the email and password the user will supply.
        writer = csv.writer(f, delimiter=",")
        email = input("Please Enter Your Email Address Ms Santander :  ")
        password = input("Please enter a valid password Ms Santander  : ")
        verification = input("Please enter your password again to validate it Ms Santander : ")
        # Verification of the password to check if the passwords match.
        if verification == password:
            writer.writerow([email, password])
            print("Successfully Registered Ms Santander")
            login()
        else:
            print("Please try again.")


def choice():
    whatToDo = input(
        "Hello Ms Santander! Would you like to make changes to your existing csv or generate words? Option A/B : ")
    if whatToDo == "A":
        with open("class_list.csv", mode="a") as f:
            print("So you have chosen to modify the existing csv file.")
            changingSome = input("Are you changing word count or level? wc/l : ")
            if changingSome == "wc":
                data = pd.read_csv("class_list.csv")
                print(data)
                student_choice = int(input("What student's word count would you like to change ? : "))
                value = data.loc[student_choice, 'Word Count']
                replacedAmount = int(input("What would you like to change this word count to? : "))
                df = pd.read_csv("class_list.csv")
                df.replace({replacedAmount: value}, inplace=True)
                df.to_csv('class_list.csv', index=False)
    if whatToDo == "B":
        main()


check = input("Have you registered? y/n : ")
if check == "n":
    register()
if check == "y":
    login()
