import subprocess
from cleaner import clean_chat      # we will import the cleaned chat dataset from the other file after execution
from chatterbot import ChatBot      # used to create the chatbot instance
from chatterbot.trainers import ListTrainer # used to train the data given in the list format for the bot 

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)  # we now use the listTrainer on our chatbot instance we've created

subprocess.run("python cleaner.py", shell=True)   # the subprocess module is used to run the python file which handles on cleaning the whatsapp dataset

trainer.train(clean_chat)       # we now train the chatbot with the cleaned dataset

end = {"end":None, "stop":None, "q":None}   # end conditions for our code

while True:     # infinite loop

    user = input("User > ")     # get the input from the user

    if user.lower() in end:     # if the input consists end conditions then we just break the loop
        break

    response = chatbot.get_response(user)   # else we get the response for the user input and print it.

    print(f"Bot >  {response}")