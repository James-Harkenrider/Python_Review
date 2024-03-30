
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

fancy_knife = 'no'
key = 'no'
end_game = 0

forked_trail = input("You come to a fork in the road. Do you go left or right?").lower()

if forked_trail == "left":

  print(
    '''
      ad8888888888ba
     dP'         `"8b,
     8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
     8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
     8  8   8              """        """      ""    8b
     8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
     8  `"""'       ,d8""
     Yb,         ,ad8"   
      "Y8888888888P"
    '''
  )
  
  key  = input("you've found a plain looking key on the ground, do you pick it up, yes or no?")
else:
  fancy_knife = input("you've found a fancy knife on the ground, do you pick it up, yes or no?")

print(
  '''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
  '''
)
print("Both paths converged back together upon a great lake with an island in the center.")
cross_water = input("Do you swim or wait for a boat? (Type swim or wait)")

if cross_water == "swim":
  print('''
                  _,.---.---.---.--.._ 
              _.-' `--.`---.`---'-. _,`--.._
             /`--._ .'.     `.     `,`-.`-._\
            ||   \  `.`---.__`__..-`. ,'`-._/
       _  ,`\ `-._\   \    `.    `_.-`-._,``-.
    ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
   (_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
    `---'    `._ `---._/__,----`           `-. `-\
              /_, ,  _..-'                    `-._\
              \_, \/ ._(
               \_, \/ ._\
                `._,\/ ._\
                  `._// ./`-._
                    `-._-_-_.-'

  ''')
  print("A giant ancient under water turtle surfaces beneath you partway through and carries you to the island.")
else:
  print("A boat arrives, but it has been taken over by pirates.")
  if fancy_knife == 'yes':
    print("The knife you picked up earlier was stolen from one of the priates. They surround you and take you to the brig. Game Over")
    end_game = 1
  else:
    print("The pirates are also going to the island and allow you passage on their boat. You make it to the island safely.")
if end_game == 0:
  print("On the island you come to a large building with three doors. One red, one yellow, and one blue.")
if key == 'yes':
  print("The key you picked up earlier fits into the blue door. You open it and find a treasure chest full of gold. You win!")
elif not end_game:
  door = input("Which door do you choose? (red, yellow, or blue)")
  if door == "blue":
    print("You open the blue door and find a treasure chest full of gold. You win!")
  else:
    print("The door was trapped and you are eaten by a giant that was slumbering within. Game Over.")