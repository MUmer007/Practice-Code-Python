# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def is_leap(year):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Example usage:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # year = int(input())  # Read an integer year from input
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(is_leap(year))  # Print the result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # marks = int(input("Please enter your marks: "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if marks >= 90:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     grade = "A"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif marks >= 80 and marks < 90:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     grade = "B"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif marks >= 70 and marks < 80:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     grade = "C"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     grade = "D"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Grade of the student is = ", grade)            







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Even_ODD = int(input("Please Enter a number "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if (Even_ODD % 2 == 0):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("THIS IS AN EVEN NUMBER")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(Even_ODD % 3 != 0):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("THIS IS AN ODD NUMBER")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("NEITHER EVEN OR ODD")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(Even_ODD)    



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = int(input("Please Enter first number "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = int(input("Please Enter second number "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = int(input("Please Enter third number "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = int(input("Please Enter fourth number "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(a > b or a > c and a > d):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("first number is the largest", a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(b > c and b > d):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("second number is the largest", b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(c > d):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("third number is the largest", c)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Fourth is the largest", d)    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num1 = [1,3,4,6,7]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num1.pop(0)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # MOV_fav = []
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # favMOv1 = (input("ENTER YOUR FAV MOVIE NO 1 "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # favMOv2 = (input("ENTER YOUR FAV MOVIE NO 2 "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # favMOv3 = (input("ENTER YOUR FAV MOVIE NO 3 "))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # MOV_fav.append(favMOv1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # MOV_fav.append(favMOv2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # MOV_fav.append(favMOv3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(MOV_fav)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # list1 = ["m","a","a"]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Copy_list = list1.copy()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Copy_list.reverse()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(Copy_list == list1):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    print("PALINDROME")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("NOT PALINDROME")    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # SRT = [1,2,5,4,3,6]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # SRT.sort()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(SRT)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 100 days of coding python



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("---your poem here \n and must read this")
   
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'time' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         current_time = datetime.datetime.now().strftime("%H:%M:%S")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak(f"The time is {current_time}")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'date' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         current_date = datetime.datetime.now().strftime("%B %d, %Y")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak(f"Today's date is {current_date}")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'wikipedia' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak("Searching Wikipedia...")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         query = command.replace('wikipedia', '').strip()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             result = wikipedia.summary(query, sentences=1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak(result)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         except wikipedia.exceptions.DisambiguationError as e:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak(f"Multiple results found, please be more specific. Here are some options: {e.options}")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         except wikipedia.exceptions.HTTPError:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak("Sorry, I couldn't fetch data from Wikipedia.")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'open' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         if 'google' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak("Opening Google")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             webbrowser.open("https://www.google.com")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         elif 'youtube' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak("Opening YouTube")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             webbrowser.open("https://www.youtube.com")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             speak("Which website would you like to open?")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             website = listen()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             if website:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                 webbrowser.open(f"https://{website}.com")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'play' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         song = command.replace('play', '').strip()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak(f"Playing {song}")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         os.system(f"start https://www.youtube.com/results?search_query={song}")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif 'stop' in command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak("Goodbye!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         exit()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         speak("Sorry, I didn't understand that command.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Main function to run the assistant
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def run_assistant():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     speak("Jarvis at your service. How can I help you today?")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     while True:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         command = listen()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         if command:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             process_command(command)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Start the assistant
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     run_assistant()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num1 = int(input("enter num 1 "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num2 = int(input("enter num 2 "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # operators = ("+", "-",)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 + num2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 - num2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 * num2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 / num2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 // num2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(num1 % num2)








# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # name1 = """ A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs. This is because paragraphs show a reader where the subdivisions of an essay begin and end, and thus help the reader see the organization of the essay and grasp its main points.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Paragraphs can contain many different kinds of information. A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects. Regardless of the kind of information they contain, all paragraphs share certain characteristics. One of the most important of these is a topic sentence."""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(name1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = "umer, Shaikh@"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.lower())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.upper())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.strip())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.rstrip("@"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.replace("umer", "MUHAMMAD"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.split(" "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.capitalize())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.center(50, "_"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.count("a"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.endswith("@"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.find("umer"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print (a.islower())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # str2 = "He's name is Dan. He is"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(len (str2))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # str1 = "He's name is Dan. Dan is an honest man."
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(str1.index("Dan"))




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # str1 = "WelcomeToTheConsole"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(str1.isalnum())


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # str1 = "Welcome"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(str1.isalpha())


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = int(input("Enter your age: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Your age is: ", a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(a>18):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("You can vote")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("You cannot vote")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # isEven = int(input("Enter a number: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Your number is: ", isEven)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(isEven%2==0):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Your number is even")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Your number is odd")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = int(input("Enter a number: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Your number is: ", a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(a>100):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Your number is greater than 100")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Your number is less than 100")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1 = int(input("Enter your marks: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Your marks are: ", student1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(student1>=90):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is A")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(student1>=80):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is B")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(student1>=70):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is C")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(student1>=60):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is D")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # elif(student1>=50):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is E")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  print("Your grade is F")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # timeCheck = time.strftime("%H:%M:%S")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(timeCheck)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # timeCheck = time.strftime('%H ')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(timeCheck)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # timeCheck = time.strftime('%M ')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(timeCheck)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # timeCheck = time.strftime('%S ')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(timeCheck)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # x = int(input("Enter a value "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # match x:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case 0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("x is zero")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case 4:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("case is 4")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case _ if x !=90:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #          print(x,"x is not 90")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case _ if x !=80:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #          print(x,"x is not 80")     
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case _:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #          print("x")  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #          # SWITCH CASE 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # age = int(input("Enter your age: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # match age:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case 1 if age >=18:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #            print("you are ready to vote")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case 2 if age <=18:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #            print("you are not ready  to vote")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     case _ if age >=65:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             print("you are retired now cannot vote! ")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                    # FOR LOOP




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # name = "MUHAMMAD UMER"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in name:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if (i =="b"):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("This is something speacial!")    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # colors = ["Red" , "Green" , "Yellow"] 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for color in colors:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(color)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in color:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)           

                
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for k in range(1, 200):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   print(k)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                   # WHILE LOOP
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # i = int(input("Enter your number: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while(i<=35):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     i = int(input("Enter your number: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     i = i + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if(i>=35):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("loop is end")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     # DECRIMENTING WHILE LOOP


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # i = 6
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while(i > 0):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     i = i - 1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                              # BREAK & CONTINUE


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(11):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if (i == 10):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("5 X",i +1, "=", 5 *(i +1))
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(13):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if(i == 10):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Skip the iteration")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     continue
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("5 X", i , "=", 5 * i)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #                       # DO WHILE LOOP

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # i = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     i = i + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if(i%100 == 0):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         


# # # # # # # # # # # # # # # # # # # # # # # # # # # #                      # fuction of python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def CalcGmean(a,b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     mean = (a*b) / (a+b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(mean)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # def isGreater(a,b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     if(a>=b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("First number is Greater")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #          print("Second number is Greater or equal")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # def isLess(a,b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     if(a<=b):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("first number is lesser or equal")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #          print("Second number is lesser or equal")    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # a = 5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # b = 3
# # # # # # # # # # # # # # # # # # # # # # # # # # # # isGreater(a,b)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # CalcGmean(a,b)             
# # # # # # # # # # # # # # # # # # # # # # # # # # # # isLess(a,b)



# # # # # # # # # # # # # # # # # # # # # # # # # # # def name(fname, mname = "Jhon", lname = "Whatson"):
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Hello,", fname, mname, lname)

# # # # # # # # # # # # # # # # # # # # # # # # # # # name("Umer","Shaikh","BSDS")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # Hence, the the order in which the arguments are passed does not matter.

# # # # # # # # # # # # # # # # # # # # # # # # # # # def name(fname, mname, lname):
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Hello,", fname, mname, lname)

# # # # # # # # # # # # # # # # # # # # # # # # # # # name(mname = "Peter", lname = "Wesker", fname = "Jade")



# # # # # # # # # # # # # # # # # # # # # # # # # # # def name(fname, mname, lname):
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Hello,", fname, mname, lname)

# # # # # # # # # # # # # # # # # # # # # # # # # # # name("Peter", "Quill", "abc")



# # # # # # # # # # # # # # # # # # # # # # # # # # # def average(*numbers):
# # # # # # # # # # # # # # # # # # # # # # # # # # #   sum = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # #   for i in numbers:
# # # # # # # # # # # # # # # # # # # # # # # # # # #     sum = sum + i 
# # # # # # # # # # # # # # # # # # # # # # # # # # #   return sum / len(numbers)

# # # # # # # # # # # # # # # # # # # # # # # # # # # c = average(1,2,3,4,5,6,7,8,9,11,12,13,14,15,16.17,18,19)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(c)  

# # # # # # # # # # # # # # # # # # # # # # # # # #   # LIST


# # # # # # # # # # # # # # # # # # # # # # # # # # # We can check if a given item is present in the list. This is done using the in keyword




# # # # # # # # # # # # # # # # # # # # # # # # # # colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# # # # # # # # # # # # # # # # # # # # # # # # # # if "Red" in colors:
# # # # # # # # # # # # # # # # # # # # # # # # # #     print("is present.")
# # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # #     print("not present")    


# # # # # # # # # # # # # # # # # # # # # # # # # # #                       Range of Index:
# # # # # # # # # # # # # # # # # # # # # # # # # # # You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

# # # # # # # # # # # # # # # # # # # # # # # # # # # Syntax:

# # # # # # # # # # # # # # # # # # # # # # # # # # # listName[start : end : jumpIndex]   

# # # # # # # # # # # # # # # # # # # # # # # # # # animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(animals[3:7])	#using positive indexes
# # # # # # # # # # # # # # # # # # # # # # # # # # print(animals[-7:-2])	#using negative indexes'


# # # # # # # # # # # # # # # # # # # # # # # # # # names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# # # # # # # # # # # # # # # # # # # # # # # # # # namesWith_a = [item for item in names if "a" in item]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(namesWith_a)


# # # # # # # # # # # # # # # # # # # # # # # # # #                          # LIST METHODS

# # # # # # # # # # # # # # # # # # # # # # # # # # colors = ["voilet", "green", "indigo", "blue", "green"]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(colors.count("green"))

# # # # # # # # # # # # # # # # # # # # # # # # # # num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(num.count(2))

# # # # # # # # # # # # # # # # # # # # # # # # # # l = [11, 45, 1, 2, 4, 6, 1, 1]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(l)
# # # # # # # # # # # # # # # # # # # # # # # # # # # l.append(7)
# # # # # # # # # # # # # # # # # # # # # # # # # # # l.sort(reverse=True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # l.reverse()
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(l.index(1))
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(l.count(1))
# # # # # # # # # # # # # # # # # # # # # # # # # # # m = l.copy()
# # # # # # # # # # # # # # # # # # # # # # # # # # # m[0] = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # l.insert(1, 899)
# # # # # # # # # # # # # # # # # # # # # # # # # # m = [900, 1000, 1100]
# # # # # # # # # # # # # # # # # # # # # # # # # # k = l + m
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(k)
# # # # # # # # # # # # # # # # # # # # # # # # # # # l.extend(m)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(l)



# # # # # # # # # # # # # # # # # # # # # # # # #                              # TUPLES AND ITS METHODS

# # # # # # # # # # # # # # # # # # # # # # # # # tup1 = (1,2,3,4,5,6,7)
# # # # # # # # # # # # # # # # # # # # # # # # # tup2 = ("RED","GREEN" , "BLUE")
# # # # # # # # # # # # # # # # # # # # # # # # # print(tup1)
# # # # # # # # # # # # # # # # # # # # # # # # # print(tup2)
# # # # # # # # # # # # # # # # # # # # # # # # # print(type(tup1))

# # # # # # # # # # # # # # # # # # # # # # # # # details = ("Abhijeet", 18, "FYBScIT", 9.8)
# # # # # # # # # # # # # # # # # # # # # # # # # print(details)


# # # # # # # # # # # # # # # # # # # # # # # # # # NEGATIVE INDEXING

# # # # # # # # # # # # # # # # # # # # # # # # # country = ("Spain", "Italy", "India", "England", "Germany")
# # # # # # # # # # # # # # # # # # # # # # # # # #            [0]      [1]      [2]       [3]        [4]
# # # # # # # # # # # # # # # # # # # # # # # # # print(country[len(country) - 1])
# # # # # # # # # # # # # # # # # # # # # # # # # print(country[-3])
# # # # # # # # # # # # # # # # # # # # # # # # # print(country[-4])





# # # # # # # # # # # # # # # # # # # # # # # # # country = ("Spain", "Italy", "India", "England", "Germany")
# # # # # # # # # # # # # # # # # # # # # # # # # if "German" in country:
# # # # # # # # # # # # # # # # # # # # # # # # #     print("Germany is present.")
# # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # #     print("Germany is absent.")


# # # # # # # # # # # # # # # # # # # # # # # # #     tep1 = ("a","b","c","d","e")
# # # # # # # # # # # # # # # # # # # # # # # # #     print(tep1)
# # # # # # # # # # # # # # # # # # # # # # # # #     temp1 = list(tep1)
# # # # # # # # # # # # # # # # # # # # # # # # #     temp1.append("f")
# # # # # # # # # # # # # # # # # # # # # # # # #     temp1.pop(2)
# # # # # # # # # # # # # # # # # # # # # # # # #     tep1 = tuple(temp1)
# # # # # # # # # # # # # # # # # # # # # # # # #     print(tep1)



# # # # # # # # # # # # # # # # # # # # # # # # #     # EXERCISE 2 TIME ZOZE
    

# # # # # # # # # # # # # # # # # # # # # # # # #     import time
# # # # # # # # # # # # # # # # # # # # # # # # # t = time.strftime('%H:%M:%S') 
# # # # # # # # # # # # # # # # # # # # # # # # # hour = int(time.strftime('%H'))
# # # # # # # # # # # # # # # # # # # # # # # # # # hour = int(input("Enter hour: "))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(hour)

# # # # # # # # # # # # # # # # # # # # # # # # # if(hour>=0 and hour<12):
# # # # # # # # # # # # # # # # # # # # # # # # #   print("Good Morning Sir!")
# # # # # # # # # # # # # # # # # # # # # # # # # elif(hour>=12 and hour<17):
# # # # # # # # # # # # # # # # # # # # # # # # #   print("Good Afternoon Sir!")
# # # # # # # # # # # # # # # # # # # # # # # # # elif(hour>=17 and hour<0):
# # # # # # # # # # # # # # # # # # # # # # # # #   print("Good Night Sir!")
    

# # # # # # # # # # # # # # # # # # # # # # # # #     # PRINT F STRING


# # # # # # # # # # # # # # # # # # # # # # # # # # letter = "Hey my name is {1} and I am from {0}"
# # # # # # # # # # # # # # # # # # # # # # # # # # country = "India"
# # # # # # # # # # # # # # # # # # # # # # # # # # name = "Harry"

# # # # # # # # # # # # # # # # # # # # # # # # # # print(letter.format(country, name))
# # # # # # # # # # # # # # # # # # # # # # # # # # print(f"Hey my name is {name} and I am from {country}")
# # # # # # # # # # # # # # # # # # # # # # # # # # print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
# # # # # # # # # # # # # # # # # # # # # # # # # # price = 49.09999
# # # # # # # # # # # # # # # # # # # # # # # # # # txt = f"For only {price:.2f} dollars!"
# # # # # # # # # # # # # # # # # # # # # # # # # # print(txt)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(txt.format())
# # # # # # # # # # # # # # # # # # # # # # # # # # print(type(f"{2 * 30}"))




# # # # # # # # # # # # # # # # # # # # # # # # # val = 'Geeks'  
# # # # # # # # # # # # # # # # # # # # # # # # # print(f"{val}for{val} is a portal for {val}.")  
# # # # # # # # # # # # # # # # # # # # # # # # # name = 'Tushar'  
# # # # # # # # # # # # # # # # # # # # # # # # # age = 23  
# # # # # # # # # # # # # # # # # # # # # # # # # print(f"Hello, My name is {name} and I'm {age} years old.")



# # # # # # # # # # # # # # # # # # # # # # # # name = input("ENTER YOUR NAME: ")
# # # # # # # # # # # # # # # # # # # # # # # # cLASS = input("ENTER YOUR CLASS: ") 
# # # # # # # # # # # # # # # # # # # # # # # # Roll_No = int(input("ENTER YOUR ROLL NO: "))
# # # # # # # # # # # # # # # # # # # # # # # # print(f"MY NAME IS {name} AND IAM A STUDENT OF {cLASS} AND MY ROLL NO : A{Roll_No} ")

                              
                   
# # # # # # # # # # # # # # # # # # # # # # #  # DOC STRING




# # # # # # # # # # # # # # # # # # # # # # # def square(n):
# # # # # # # # # # # # # # # # # # # # # # #     '''Takes in a number n, returns the square of n '''
# # # # # # # # # # # # # # # # # # # # # # #     return n**2

# # # # # # # # # # # # # # # # # # # # # # # print(square(5))


# # # # # # # # # # # # # # # # # # # # # # # def is_Even(n):
# # # # # # # # # # # # # # # # # # # # # # #     ''' Returns true if n is even, false otherwise'''
# # # # # # # # # # # # # # # # # # # # # # #     return n % 2 == 0
# # # # # # # # # # # # # # # # # # # # # # # print(is_Even(2))


# # # # # # # # # # # # # # # # # # # # # #                                 PEP 8
# # # # # # # # # # # # # # # # # # # # # # PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# # # # # # # # # # # # # # # # # # # # # # PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.   
 

# # # # # # # # # # # # # # # # # # # # #                                   # RECURSION

# # # # # # # # # # # # # # # # # # # # # def Factorial(n):
# # # # # # # # # # # # # # # # # # # # #     if(n==0 or n==1):
# # # # # # # # # # # # # # # # # # # # #         return 1
# # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # #         return n * Factorial(n-1)
# # # # # # # # # # # # # # # # # # # # # print(Factorial(5))


# # # # # # # # # # # # # # # # # # # # def Fac(n):
# # # # # # # # # # # # # # # # # # # #    if(n==0 or n==1):
# # # # # # # # # # # # # # # # # # # #        return 1
# # # # # # # # # # # # # # # # # # # #    else:
# # # # # # # # # # # # # # # # # # # #      return n * Fac(n-1)
# # # # # # # # # # # # # # # # # # # # print(Fac(6))


# # # # # # # # # # # # # # # # # # # # # factorial(7) = 7*6*5*4*3*2*1
# # # # # # # # # # # # # # # # # # # # # factorial(6) = 6*5*4*3*2*1
# # # # # # # # # # # # # # # # # # # # # factorial(5) = 5*4*3*2*1
# # # # # # # # # # # # # # # # # # # # # factorial(4) = 4*3*2*1
# # # # # # # # # # # # # # # # # # # # # factorial(0) = 1


# # # # # # # # # # # # # # # # # # # # # factorial(n) = n * factorial(n-1)
# # # # # # # # # # # # # # # # # # # # def factorial(n):
# # # # # # # # # # # # # # # # # # # #   if (n == 0 or n == 1):
# # # # # # # # # # # # # # # # # # # #     return 1
# # # # # # # # # # # # # # # # # # # #   else:
# # # # # # # # # # # # # # # # # # # #     return n * factorial(n - 1)


# # # # # # # # # # # # # # # # # # # # # print(factorial(5))
# # # # # # # # # # # # # # # # # # # # # 5 * factorial(4)
# # # # # # # # # # # # # # # # # # # # # 5 * 4 * factorial(3)
# # # # # # # # # # # # # # # # # # # # # 5 * 4 * 3 * factorial(2)
# # # # # # # # # # # # # # # # # # # # # 5 * 4 * 3 * 2 * factorial(1)
# # # # # # # # # # # # # # # # # # # # # 5 * 4 * 3 * 2 * 1

# # # # # # # # # # # # # # # # # # # # # Quick Quiz: Write a program to print the Fibonacci sequence
# # # # # # # # # # # # # # # # # # # # # f(0) = 0
# # # # # # # # # # # # # # # # # # # # # f(1) = 1
# # # # # # # # # # # # # # # # # # # # # f(2) = f(1) + f(0)
# # # # # # # # # # # # # # # # # # # # # f(n) = f(n-1) + f(n-2)

# # # # # # # # # # # # # # # # # # # # # 0 1 1 2 3 5 8....







# # # # # # # # # # # # # # # # # # # # The Fibonacci numbers

# # # # # # # # # # # # # # # # # # # def Fibonacci(n):
# # # # # # # # # # # # # # # # # # #   if n<= 1:
# # # # # # # # # # # # # # # # # # #     return n
# # # # # # # # # # # # # # # # # # #   else:
# # # # # # # # # # # # # # # # # # #     return Fibonacci(n-1) + Fibonacci(n-2)
# # # # # # # # # # # # # # # # # # # print(Fibonacci(7))



# # # # # # # # # # # # # # # # # #                       # SET DATA TYPE


# # # # # # # # # # # # # # # # # # S = {2,2,4,5,5,2,5,7,3,7,2,9,}
# # # # # # # # # # # # # # # # # # print(S)


# # # # # # # # # # # # # # # # # # umer = set()
# # # # # # # # # # # # # # # # # # print(type(umer))

# # # # # # # # # # # # # # # # # info = {"umer", "Shaikh", 63, True, 4.4}
# # # # # # # # # # # # # # # # # print(type(info))


# # # # # # # # # # # # # # # # # for value in info:
# # # # # # # # # # # # # # # # #     print(value)

# # # # # # # # # # # # # # # # def Fabro(n):
# # # # # # # # # # # # # # # #     if n<= 1:
# # # # # # # # # # # # # # # #         return n
# # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # #         return Fabro(n-1) + Fabro(n-2)
# # # # # # # # # # # # # # # # print(Fabro(9))

# # # # # # # # # # # # # # # def is_Even(n):
# # # # # # # # # # # # # # #     return n % 2 == 0

# # # # # # # # # # # # # # # print(is_Even) (int(input("Enter a number  ")))



# # # # # # # # # # # # # # num = int(input("Enter a number  "))
# # # # # # # # # # # # # # if num >= 100:
# # # # # # # # # # # # # #     print("num is greater than 100")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("you write a right number") 

# # # # # # # # # # # # #            #NUMBER GUESSING GAME 
# # # # # # # # # # # # # import random
# # # # # # # # # # # # # def Num_Guess_Game():
                
# # # # # # # # # # # # #  Num_Guess_Game = random.randint(1,5)
# # # # # # # # # # # # #  guess = None
# # # # # # # # # # # # #  attempt = 0
# # # # # # # # # # # # #  print("Welcome to the Number guessing Game! ")
# # # # # # # # # # # # #  print("Iam thinking the number between 1 and 100, ")
# # # # # # # # # # # # #  while guess != Num_Guess_Game:
# # # # # # # # # # # # #     guess = int(input("Take a guess: "))
# # # # # # # # # # # # #     attempt += 1
# # # # # # # # # # # # #     if guess < Num_Guess_Game:
# # # # # # # # # # # # #       print("Too low! ")
# # # # # # # # # # # # #     elif guess > Num_Guess_Game:
# # # # # # # # # # # # #       print("Too High! ")
# # # # # # # # # # # # #       print(f"Congratulations! You've guessed the number in {attempt} attempts. ")  
# # # # # # # # # # # # # Num_Guess_Game()

 
# # # # # # # # # # # # # SET AND ITS METHODS
# # # # # # # # # # # # s1 = {1,3,5,7,9}
# # # # # # # # # # # # s2 = {2,4,6,8,10}
# # # # # # # # # # # # print(s1.intersection(s2))


# # # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # # # # # # # # # # # cities3 = cities.intersection_update(cities2)
# # # # # # # # # # # # print(cities3)


# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # # # # # # # # # # cities3 = cities.symmetric_difference(cities2)
# # # # # # # # # # # print(cities3)

# # # # # # # # # # # The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# # # # # # # # # # # isdisjoint():

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # # # # # # # # # # print(cities.isdisjoint(cities2))
# # # # # # # # # # # Output:
# # # # # # # # # # # False

# # # # # # # # # # # issuperset():
# # # # # # # # # # # The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities2 = {"Seoul", "Kabul"}
# # # # # # # # # # # print(cities.issuperset(cities2))
# # # # # # # # # # # cities3 = {"Seoul", "Madrid","Kabul"}
# # # # # # # # # # # print(cities.issuperset(cities3))
# # # # # # # # # # # Output:
# # # # # # # # # # # False
# # # # # # # # # # # False

# # # # # # # # # # # issubset():
# # # # # # # # # # # The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities2 = {"Delhi", "Madrid"}
# # # # # # # # # # # print(cities2.issubset(cities))
# # # # # # # # # # # Output:
# # # # # # # # # # # True

# # # # # # # # # # # add()
# # # # # # # # # # # If you want to add a single item to the set use the add() method.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities.add("Helsinki")
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # {'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

# # # # # # # # # # # update()
# # # # # # # # # # # If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities2 = {"Helsinki", "Warsaw", "Seoul"}
# # # # # # # # # # # cities.update(cities2)
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # {'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}

# # # # # # # # # # # remove()/discard()
# # # # # # # # # # # We can use remove() and discard() methods to remove items form list.

# # # # # # # # # # # Example :
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities.remove("Tokyo")
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # {'Delhi', 'Berlin', 'Madrid'}

# # # # # # # # # # # The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities.remove("Seoul")
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # KeyError: 'Seoul'

# # # # # # # # # # # pop()
# # # # # # # # # # # This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # item = cities.pop()
# # # # # # # # # # # print(cities)
# # # # # # # # # # # print(item)
# # # # # # # # # # # Output:
# # # # # # # # # # # {'Tokyo', 'Delhi', 'Berlin'} Madrid

# # # # # # # # # # # del
# # # # # # # # # # # del is not a method, rather it is a keyword which deletes the set entirely.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # del cities
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

# # # # # # # # # # # What if we don’t want to delete the entire set, we just want to delete all items within that set?

# # # # # # # # # # # clear():
# # # # # # # # # # # This method clears all items in the set and prints an empty set.

# # # # # # # # # # # Example:
# # # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # # cities.clear()
# # # # # # # # # # # print(cities)
# # # # # # # # # # # Output:
# # # # # # # # # # # set()

# # # # # # # # # # # Check if item exists
# # # # # # # # # # # You can also check if an item exists in the set or not.

# # # # # # # # # # # Example
# # # # # # # # # # # info = {"Carla", 19, False, 5.9}
# # # # # # # # # # # if "Carla" in info:
# # # # # # # # # # #     print("Carla is present.")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("Carla is absent.")


# # # # # # # # # # a = {1,2,3}

# # # # # # # # # # a.add(4)
# # # # # # # # # # print(a)


# # # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # # cities.remove("Tok")
# # # # # # # # # # print(cities)

# # # # # # # # # # DISCARRD METHOD DOES NOT THROW ANY ERROR IF WE REMOVE ITEM THAT IS NOT PRESENT IN THE SET WHILE REMOVE METHOD DOES 

# # # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # # item = cities.pop()
# # # # # # # # # print(cities)
# # # # # # # # # print(item)

# # # # # # # # # pop()
# # # # # # # # # This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.



# # # # # # # # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # # # # # # # cities.clear()
# # # # # # # # print(cities)


# # # # # # # # info = {"UMER", 21, False, 5.9}
# # # # # # # # if "U" in info:
# # # # # # # #     print("UMER is present.")
# # # # # # # # else:
# # # # # # # #     print("UMER is absent.")

# # # # # # # #     # MARKS OF STUDENT IN BSDS 

# # # # # # # # Marks1 = {
# # # # # # # #   "NAME: ": "UMER",
# # # # # # # #   "CLASS: ": "2k24/BSDS/63",
# # # # # # # #   "Subjects:": ["ENGLISH, URDU ,SINDI ,ISL, ARABIC, OOPS"],
# # # # # # # #   "MARKS: ":  [90, 88 , 99 , 98 ,78 , 98]
# # # # # # # #  }   
# # # # # # # # # print(Marks1["MARKS: "])
# # # # # # # # # print(Marks1["Subjects:"])

# # # # # # # # for key in Marks1.keys():
# # # # # # # #     print(Marks1[key])

# # # # # # # # info = {'name':'Karan', 'age':19, 'eligible':True}
# # # # # # # # info.pop("age")
# # # # # # # # print(info)

# # # # # # # info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# # # # # # # info.popitem()
# # # # # # # print(info)

# # # # # # FOR LOOP WITH ELSE HANDLING


# # # # i = 0
# # # # while i<5:
# # # #     print(i)
# # # #     i = i + 1
# # # #     if i == 4:
# # # #         break
# # # # else:
# # # #         print("loop is end")

# # # # # i = 0
# # # # # while i<7:
# # # # #   print(i)
# # # # #   i = i + 1
# # # # #   if i == 4:
# # # # #      break

# # # # # else:
# # # # #   print("Sorry no i")


# # # for r in range(5):
# # #     print("Iteration No {} in for loop".format(r+1))
# # # else:
# # #     print("Else block in loop")
# # # print("Out of the loop ")

# # # # Exception Handling in Python: Examples
# # try:
# #     age = int(input("Enter your Age: "))
# # except ValueError:
# #     print("Enter a valid integer")
# # else:
# #     if age <= 18:
# #         print("You are an adult")
# #     else:
# #         print("You are not adult")  
# # try:
# #     num = int(input("Enter a number: "))
# #     result = 100 / num
# #     print("Result is:", result)
# # except ValueError:
# #     print("Error: That's not a valid number!")
# # except ZeroDivisionError:
# #     print("Error: Cannot divide by zero!")


 
# #     Finally Clause


# # The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.



# try:
#     user_input = input("Enter any value between 5 and 9 (or 'quit' to exit): ")
    
#     if user_input.lower() == "quit":
#         print("Program is ended. Congrats!")
#     else:
#         a = int(user_input)
#         if a < 5 or a > 9:
#             raise ValueError("Value should be between 5 and 9")
#         print(f"You entered: {a}")
        
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     user_input = input("Enter any value between 5 and 9 (or 'quit' to exit :")
#     if user_input.lower() == "quit":
#         print("Program is ended. Congrats!")
#     else:
#          a = int(user_input)
#          if a < 5 or a > 9:
#             raise ValueError ("val should be between 5 and 9 ")
#     print(f"enter {a}")
# except ValueError as e:
#     print(f"error {e}")


# simple if else

a = 12
b = 24
print("A is greater" if a > b else "B is greater" if b > a else "A and B are equal")