filename = "day_03_input.txt"

multiply = 1

x_vel = [1,3,5,7,1]
y_vel = [1,1,1,1,2]

with open(filename) as f:
    tree_map = [list(line.strip()) for line in f]

height = len(tree_map)
width = len(tree_map[0])

slope_hits = []

for i in range(0,len(x_vel)):

    x_pos = 0
    y_pos = 0
    
    print(x_vel[i])
    print(y_vel[i])

    hit_tree = 0

    while y_pos < height:
        
        get_tree = tree_map[y_pos][x_pos]
        
        print(x_pos,',',y_pos,'=',get_tree)
        
        if get_tree == ".":
            print("PASS")
            pass
        
        if get_tree == "#":
            print("HIT")
            hit_tree = hit_tree + 1
        
        x_pos = x_pos + x_vel[i]
        
        if x_pos >= width:
            print("X LOOP")
            x_pos = x_pos - width
        
        y_pos = y_pos + y_vel[i]
        
    print('TOTAL TREES HIT =',hit_tree)
    slope_hits.append(hit_tree)
    multiply = multiply * hit_tree

print(slope_hits)
print(multiply)