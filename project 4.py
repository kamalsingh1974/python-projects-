import random
# print ('lets toss who will pay the bill ok')
# # input("let select teh enter button")
# number=["1","2","3","4","5","6"]
# # friends=["kamal","rishita","nisharg","diya","tamanna","ankita","satish"]
# print(random.choice(number))
rock=''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper='''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
c=[rock,paper,scissors]
user_choice=int(input("welcome to the rock paper scissors world . 0=rock,1=paper,2=scissors\n"))
if 0 <= user_choice <= 2:
    print(c[user_choice])
computer_choice=random.randint(0,2)
print(f"computer choice is")
print(c[computer_choice])
if user_choice>=3 or user_choice<=0:
    print("you typed a invalid no. you lose!")
elif user_choice==0 and computer_choice==2:
    print("you wins!")
elif user_choice==2 and computer_choice==0:
    print("you lose!")
elif computer_choice>user_choice:
    print("you lose!")
elif computer_choice<user_choice:
    print("you win!")
elif user_choice==computer_choice:
    print("it's a tie!")
