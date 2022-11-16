aes1 = int(input("What is your score in term 1 AES? "))
aes2 = int(input("What is your score in term 2 AES? "))
aes3 = int(input("What is your score in term 3 AES? "))
math1 = int(input("What is your score in term 1 maths? "))
math2 = int(input("What is your score in term 2 maths? "))
math3 = int(input("What is your score in term 3 maths? "))
phy1 = int(input("What is your score in term 1 physics? "))
phy2 = int(input("What is your score in term 2 physics? "))
phy3 = int(input("What is your score in term 3 physics? "))
CP = int(input("What is your score in computer programming? "))
chem = int(input("What is your score in chem? "))
CD = int(input("What is your score in term 1 AES? "))

avgmath2and3 = (math2 + math3)/2
avgall = (aes1+aes2+aes3+math1+math2+math3+phy1+phy2+phy3+CP+chem+CD)/12

if aes1 >= 40 and aes2 >= 40 and aes3 >= 40 and math1 >= 40 and math2 >= 40 and  math3 >= 40 and  phy1 >= 40 and  phy2 >= 40 and phy3 >= 40 and CP >= 40 and CD >= 40 and chem >= 40:
   if avgall >= 60:
       if avgmath2and3 >= 65:
           if aes3 >= 60:
               print("You have passed, congratulations!")
           else:
               print("Sorry you did not progress because you need above a 60% in AES 3")
       else:
           print("Sorry you did not progress because you need atleast an average of 65% over math 2 and math 3")
   else:
       print("Sorry you did not progress because you need atleast an average of 60% over all subjects")
else:
    print("Sorry you did not progress because you need atleast 40% in each subject to pass")

    quit()