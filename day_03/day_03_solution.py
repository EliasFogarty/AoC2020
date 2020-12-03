filename = "day_03_input.txt"

x_pos = 0
y_pos = 0

with open(filename) as f:
    tree_map = [list(line.strip()) for line in f]

height = len(tree_map)
width = len(tree_map[0])

hit_tree = 0

while y_pos < height:
    
    get_tree = tree_map[y_pos][x_pos]
    
    print(x_pos,',',y_pos,'=',get_tree)
    
    if get_tree == ".":
        print("PASS")
    
    if get_tree == "#":
        print("HIT")
        hit_tree = hit_tree + 1
    
    x_pos = x_pos + 3
    
    if x_pos >= width:
        print("X LOOP")
        x_pos = x_pos - width
    
    y_pos = y_pos + 1
    
print('TOTAL TREES HIT =',hit_tree)