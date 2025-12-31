# no_you_want_check=int(input("what do you want to divide :"))
# if no_you_want_check %2==0 :
#     print("even")
# else :
#     print("odd")
# print("lets check are you fit or not")
# W=float(input("what is your weight :"))
# H=float(input("what is your lovely height :"))
# bmi=round(W /(H**2))
#
# print(f"your bmi is :{bmi}")
# #bmi category
# if bmi < 18 :
#     print('underweight')
# elif 18 <= bmi <25 :
#  print("normal")
# elif bmi<25 and bmi<30:
#      print("overweight")
# else  :
#     print("you are obese")
# print("welcome to python pizza deleviery!")
# size = input("what size pizza do you want ? S, M, or L :").upper()
# bill=0
# # to do the billing for size of pizza
# if size== "S":
#     bill+=100
# elif size=="M":
#     bill+=150
# elif size=="L":
#     bill+=200
# else:
#     print("oops you selected the wrong pizza !")
#     exit()# stop the program
#
# # to do the choice and price of pepproni
# pepperoni =input(" do you want pepperoni on your pizza ? Y or N:").upper()
# if pepperoni=="Y":
#     if size=="S":
#         bill +=10
#     elif size=="M":
#         bill+=20
#     else:
#         bill+=30
# #to do the choice and bill of cheese extra
# extra_cheese =input("do you want extra cheese on your pizza? Y or N:").upper()
# if extra_cheese=="Y":
#     bill+=10
#
# print(f"your final bill is :₹{bill}.")
print('''               [\
                  |\)                                ____
                  |                               __(_   )__
                  Y\          ___               _(          )
                 T  \       __)  )--.          (     )-----`
                J    \   ,-(         )_         `---'
               Y/T`-._\ (     (       _)                 __
               /[|   ]|  `-(__  ___)-`  |\          ,-(  __)
               | |    |      (__)       J'         (     )
   _           | |  ] |    _           /;\          `-  '
  (,,)        [| |    |    L'         /;  \
             /||.| /\ |   /\         /.,-._\        ___ _
            /_|||| || |  /  \        | |{  |       (._.'_)
  L/\       | \| | '` |_ _ {|        | | U |   /\
 /v^v\/\   `|  Y | [  '-' '--''-''-"-'`'   | ,`^v\ /\,`\
/ ,'./  \.` |[   |       [     __   L    ] |      /^v\  \
,'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_
--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y
   Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _
  Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _
 Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)
     --   ;\~~~/\|  _,.-'`_  `.\_..-'"  _ . ,_ Y_ Y_ _Y  _Y__
    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)
   (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -
    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____
      --           _    _ --   Y   (^)   _ (^)  ===   ----
          __   -  (^)  (^)      --- Y   (^) Y
      _            Y    Y                Y             ''')
print(" Welcome to treasure island")
print("your mission is to find the treasure.")
choice1=input('you\'re at the middle of the road . choose the path to go "left" or "right"\n').lower()
#now make a result of your choice
if choice1=="left":
    choice2= input('you are at the middle of the sea . select what to do "wait" for the boat or "swim"\n').lower()
    if choice2 == "wait" :
        choice3= input('you are the final stage . select the door.\n"the red"\n"the yellow "\n"the blue" \n')
        if choice3 =="the red":
            print(" oops you catch the fire . GAME LOST!")
        elif choice3 =="the yellow":
            print("hurray! you founded the treasure . you win !")
        elif choice3 =="the blue":
            print("you caughted by the lion. GAME OVER!")
        else:
            print(" you took the wrong keywords. GAME OVER!")
            exit()
    else:
        print("you were attacked by the shark . GAME OVER!")
        exit()
else:
    print("you fell down in the gutter . GAME OVER!")
    exit()







