#!/usr/bin/env python3
import re
import pprint

read_chat_file = open("Andile_Chat.txt", encoding="utf-8")
#read_chat_file = open("tes.txt", encoding="utf-8")

chat = read_chat_file.readlines()

# def TotalNumberOfWords(chat_read):
#     word_counter = 0
#     for word in chat_read:

# print(type(chat))

def StripDateInLine(chat_read):
    pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")
    pp = pprint.PrettyPrinter(indent=3)
    for line in chat_read:
        if pattern.match(line):
            remove = re.sub(pattern,'', line) #remove the date for every line
            words = remove.lstrip()
            pp.pprint(words)

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
user2 = TotalUserMessages(chat, "Her")
print("Total number of messages: " + TotalNumberOfMessages(user1, user2))

read_chat_file.close()