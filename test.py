#!/usr/bin/env python3

import re
import pprint

read_chat_file = open("tes.txt", encoding="utf-8")
chat = read_chat_file.readlines()
frank = read_chat_file.readline()


# with open('tes.txt', 'r') as reader:
#     pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")
#     line = reader.readline()
#     while line != '':
#         if pattern.match(line):
#             remove = re.sub(pattern,'', line) #remove the date for every line
#             words = remove.lstrip()
#             print(words, end='')
#             line = reader.readline()
#         else: 
#             # pattern.match(line) == line != True
#             # print(words)
#             print("not")
#             line = reader.readline()

#     for line in reader:
# with open('tes.txt', 'r') as reader:
#         print(line, end=" ")



# print(chat)
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




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
array_pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")

index_display = 0
for i in range(len(chat)):
    if array_pattern.match(chat[i]):
        print(str(index_display) + "\t" + chat[i], end=" ")
        index_display += 1
    elif array_pattern.match(chat[i])!= chat[i]: #find a way to print the redundant arrat elements
        #print(i ,"Not True")
        #print(i, end= " ")
        print(chat[i],end = " ")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""""
SOLVING THE PROBLEM OF NOT PRINTING THE WHOLE TEXT, BECAUSE THE READLINE FUNCTION READS LINES AND TURNS THEN INTO ARRAY ELENEBTS
if the next element in the array doesn't natch the date pattern at the begigining 
    #concatinate the elements
    #else move to the next line
"""""

"""""
Print the texts
TODO 
"""""

def StripDateInLine(chat_read):
    pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")
    pp = pprint.PrettyPrinter(indent=3)
    for line in chat_read:
        if pattern.match(line):
            remove = re.sub(pattern,'', line) #remove the date for every line
            words = remove.lstrip()
            pp.pprint(words)
            

# StripDateInLine(chat)
# print(the)

# print(chat)
# print(exclude_date.groups())


# print(countwords("Oh...was watching some movie..."))

read_chat_file.close()
