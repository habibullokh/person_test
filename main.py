# degree of numbers
# someone adds something here

# l1 = [1, 2, 3, 4, 5, 6, 7]

# for n in l1:
#     print(n ** 2)

# #################################### NESTED LOOPS #######################################

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]
# l2 = [2, 3, 6, 7, 8, 10, 11, 6, 9, 12]
# l3 = []

# for n in l1:
#     for i in l2:
#         n += i
#     if n % 2 == 0:
#         l3.append(n)

# print(l3)

# ############################# DICTIONARY ######################################

# abdulla = {"name" : "Abdulla" , "surname" : "abdurazzoqov" , "age" : 26}

# print(abdulla)

# abdulla["language"] = "Uzbek"
# abdulla["Gender"] = "Man"

# print(abdulla)
login_ask = input("Login kiriting: ")
passw_ask = input("parolni kiriting: ")

abdulla = {"login" : "python" , "password" : "test"}

if login_ask == abdulla["login"] and passw_ask == abdulla["password"]:
    print("you can enter")
else:
    print("you cannot enter")
    







        
    
    
    