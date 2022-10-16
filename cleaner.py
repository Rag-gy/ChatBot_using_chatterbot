import re   # we use regex module to clean the whatsapp chat dataset

date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"    # this is used to remove the date and time from the dataset from the dataset
username = r"([\w\s]+)"     # this is used to remove the username from the dataset
metadata_end = r":\s"       # this is used to remove the : after the username from the dataset

content = ""

# I have used my own personal chat, you can use your dataset

with open("Chat_dataset.txt", "r", encoding="utf-8") as chat_data:      # we use utf8 encoding to include emojis as well
    content = chat_data.read()      # we read the content from the chat

content = content.split("\n")[1:-1]     # we split the dataset on the basis of newline and remove the first and last lines ad they are mostly the information about encryption and safe conversation

for i in range(len(content)):           # we check for every dataset
    if "<Media omitted>" in content[i] or content[i] == "null":     # the dataset has no media information and thus we get these messages and so I remove them from the dataset
        content[i] = ""
    else:
        content[i] = re.sub(date_time, "", content[i])[6:]          # the date_time and username are removed and the elements from [6:] are chosen as the rest i.e [0:5] are just empty characters and whitespace
        content[i] = re.sub(username+metadata_end, "", content[i])  # we then remove the username as well.

clean_chat = [x for x in content if x!=""]  # we will finally put the data in the dataset. if they're not empty