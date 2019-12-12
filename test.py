#!/usr/bin/env python3

import re
import pprint


# 11/29/19, 8:29 PM - Andile: Mondayjhdjshdjshdjhdjs# yewah.
# 11/29/19, 8:30 PM - Him: Will talk When I get home
# 11/29/19, 8:29 PM - Him: I will..
# 11/29/19, 8:30 PM - Andile: Nno maaan...suthi you wil, you will Lana...hamba now
# 11/29/19, 9:34 PM - Him: Got home a while ago
# 11/29/19, 9:35 PM - Him: Had some food and put some clove on my tooth
# 11/29/19, 8:30 PM - Andile: Okay
# 11/29/19, 9:35 PM - Him: If it doesn't work I'll take a grandpa
# 11/29/19, 11:06 PM - Andile: Oh...was watching some movie...

read_chat_file = open("tes.txt", encoding="utf-8")
chat = read_chat_file.readlines()

def countwords(chat_read):
    #exlcude_date = re.match("(\d{2}/{3}),\s", chat_read, re.I)
    word_counter = 1
    # for line in chat_read:
    for i in range(len(chat_read)):
        if(chat_read[i] == ' ' or chat_read == '\n' or chat_read == '\t'):
            word_counter = word_counter + 1
    return(word_counter)

def TTotalNumberOfMessages(chat_read):
    message_counter = 0
    pattern  = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s")
    for line in chat_read:
        if pattern.match(line):
            message_counter+=1
    return(message_counter)

# test = "11/29/19, 8:30 PM - Andile: Nno maaan...suthi you wil, you will Lana...hamba now"



# exclude_date = re.match("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:", chat)

# reg_to_excl = exclude_date.group()

# excl = chat.strip(reg_to_excl)
# pattern = re.compile("\d{2}/")

array_pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")

# for i in range(len(chat)):
#     if array_pattern.match(chat[i]):
#         print(i, end="\t")
#         print(chat[i])
    # else:
        # conc = chat[i-1] + chat[i]
        # print(i, end= "\t")
        # print(conc)
        
"""""
SOLVING THE PROBLEM OF NOT PRINTING THE WHOLE TEXT, BECAUSE THE READLINE FUNCTION READS LINES AND TURNS THEN INTO ARRAY ELENEBTS
if the next element in the array doesn't natch the date pattern at the begigining 
    #concatinate the elements
    #else move to the next line
"""""

def StripDateInLine(chat_read):
    pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")
    pp = pprint.PrettyPrinter(indent=3)
    for line in chat_read:
        if pattern.match(line):
            remove = re.sub(pattern,'', line) #remove the date for every line
            words = remove.lstrip()
            pp.pprint(words)

# print(chat)
# print(exclude_date.groups())


# print(countwords("Oh...was watching some movie..."))

read_chat_file.close()