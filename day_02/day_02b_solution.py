filename = "day_02_input.txt"

passx = 0

with open(filename) as f:
    lines = []
    for line in f:
        split = line.split()
        #print(split)
        bounds = split[0].split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        #print(lower)
        #print(upper)
        charx = split[1].split(':')[0]
        #print(charx)
        counter = 0
        #print(split[2][lower-1:lower])
        #print(split[2][upper-1:upper])
        if split[2][lower-1:lower] == charx:
            counter = counter + 1
        if split[2][upper-1:upper] == charx:
            counter = counter + 1
        #print(counter)
        if counter == 1:
            print("TRUE")
            passx = passx + 1
        else:
            print("FALSE") 

print("TOTAL PASS = ",passx)