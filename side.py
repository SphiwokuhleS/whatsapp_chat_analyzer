import re
# def concatenate_list_data(list):
#     result= ''
#     sep = " "
#     for element in list:
#         if element.startswith("t"):
#             result += str(element)
#     return result

# print(concatenate_list_data(["one ", "two ", "three ", "four "]))

alist=["sphe\n", "shandu", "siyabonga", "sphiwokuhle", "sphedot", "kendrick"]


add = alist[0] + alist[1]
print(add)


read_chat_file = open("tes.txt", encoding="utf-8")
chat = read_chat_file.readlines()

pattern = re.compile("\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(A|P)M\s-\s\w+:")


# for i in range(len(chat)):
    # if pattern.match((chat[i+1])):
        # chat[i] + chat[i+1]
        # print(i, end=" ")
        # print(chat[i])

# for i in range(len(chat)):
    # if pattern.match((chat[i+1])):

# for el in range(len(chat)):
    # print(el, end=" ")
    # print(chat[el])

# print(chat[])
read_chat_file.close()
# print(chat)