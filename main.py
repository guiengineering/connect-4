#Connect four main body of code
#6x7
import c4_methods as c4

mesh = c4.mesh_creator()

game_over = False
while game_over == False:
    user = int(input("Which user is playing?"))
    c = int(input("What column do you wish do drop the pill?"))

    mesh = c4.drop_method(mesh, user,c)
    game_over = c4.win_check(mesh,user)

print("Congratulations to user:", str(user),"you win")
