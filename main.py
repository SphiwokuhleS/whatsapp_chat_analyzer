#!/usr/bin/env python3
import re

#SAMPLE DIALOG

# 11/29/19, 8:26 PM - Andile: Okay...sapumul kancane...
# I was studyin
# 11/29/19, 8:28 PM - Him: I know 🤦🏾‍♂.. It's just too painful right now
# 11/29/19, 8:29 PM - Him: Okay... Balanin?
# 11/29/19, 8:29 PM - Andile: Go home...babe😩
# 11/29/19, 8:29 PM - Andile: Monday
# 11/29/19, 8:29 PM - Him: I will..
# 11/29/19, 8:30 PM - Him: Will talk When I get home
# 11/29/19, 8:30 PM - Andile: Nno maaan...suthi you wil, you will Lana...hamba now
# 11/29/19, 8:30 PM - Andile: Okay
# 11/29/19, 9:34 PM - Him: Got home a while ago
# 11/29/19, 9:35 PM - Him: Had some food and put some clove on my tooth
# 11/29/19, 9:35 PM - Him: If it doesn't work I'll take a grandpa
# 11/29/19, 11:06 PM - Andile: Oh...was watching some movie...

read_chat_file = open("Andile_Chat.txt", encoding="utf-8")
#read_chat_file = open("tes.txt", encoding="utf-8")

chat = read_chat_file.readlines()

# def TotalNumberOfWords(chat_read):
#     word_counter = 0
#     for word in chat_read:

print(type(chat))
def TotalNumberOfMessagesS(chat_read):
    message_counter = 0
    pattern  = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s") #first regular expression  = (\d{1,2}/\d{1,2}/\d{1,2},\s)
    for line in chat_read:
        if pattern.match(line):
            message_counter = +1
    
    return(message_counter)

def TotalNumberOfMessages(user1, user2):
    total = user1  + user2
    return(total)

#logic idea.....
#if the line starts with regex = \d\d/\d\d/\\d\d,
def TotalUserMessages(chat_read, user):
    username  = "- " + user + ":"
    message_counter = 0
    for line in chat_read:
        if username in line:
            message_counter +=1    
            
    return(message_counter)


# print(TotalNumberOfMessages(chat))
user1 = TotalUserMessages(chat, "Him")
user2 = TotalUserMessages(chat, "Andile")
print(TotalNumberOfMessages(user1, user2))

read_chat_file.close()