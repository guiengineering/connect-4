#regular size is 6x7

def mesh_creator(r=6,c=7):
    #global mesh
    mesh = [] #creates an empty list(matrix)
    for i in range(0,r):
        row = []                  #row we will populate
        for j in range(0,c):
            row.append(0)         #each row will have col # of entries
        mesh.append(row)          #adds another row to mesh
    return mesh, 0                #the zero is for testing atm

def drop_method(mesh,user,c):
    mesh = mesh[0]
    #get size of mesh:if you drop on the c'th col you need to know how many rows there are to see how far it falls
    drop_height = len(mesh)
    #next you need to see what row it lands on
    for i in range(-1,-drop_height-1,-1):         #start from bottom to top,once it hits a value other than zero it returns updated mesh
        if mesh[i][c] == 0:
            mesh[i][c] = user
            print(mesh) ####################
            return mesh, [i,c]    #returns updated mesh and position

#returns T/F based on if Game is won or not
#going to need 5 for loops(check sides and below and diagnols)
def win_check(mesh,user):
    grid = mesh[0] #mesh[0] gives whole grid
    pos = mesh[1] #pos[0]-row / pos[1]-col
#    print(len(grid[0])) #number of columns in the whole grid
#    print("row:",pos[0])
#    print("col:",pos[1])

#1 for loop (checks below for connect 4)
    in_a_row = 0
    for i in range(pos[0], pos[0] + 4, 1):
        if grid[i][pos[1]] == user:
            in_a_row += 1
        if in_a_row == 4:
            print("loop 1")
            return True

#2 for loop (checks to the left for connect 4)
    in_a_row = 0
    for i in range(pos[1], pos[1] - 4, -1):
        if grid[pos[0]][i] == user:
            in_a_row += 1
        if in_a_row == 4:
            print("loop 2")
            return True

#3 for loop (checks to the right for connect 4)
    in_a_row = 0
    for i in range(pos[1], pos[1] + 4, 1):
        if i < len(grid[0]): #keeps from checking out of bounds index
            if grid[pos[0]][i] == user:
                in_a_row += 1
            if in_a_row == 4:
                print("loop 3")
                return True

    return False

'''
mesh = mesh_creator()
mesh = drop_method(mesh,1,3) #(mesh,user,c)
print(win_check(mesh,1))
mesh = drop_method(mesh,1,2)
print(win_check(mesh,1))
mesh = drop_method(mesh,1,1)
print(win_check(mesh,1))
mesh = drop_method(mesh,1,0)
print(win_check(mesh,1))
'''

