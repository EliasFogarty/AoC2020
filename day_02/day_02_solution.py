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
        counter = int(split[2].count(charx))
        #print(counter)
        if counter >= lower and counter <= upper:
            print("TRUE")
            passx = passx + 1
        else:
            print("FALSE") 

print("TOTAL PASS = ",passx)