filename = 'day_06_input.txt'

my_group = []

total = 0

with open(filename) as f:
   
    for line in f:
    
        clean = line.strip()
            
        if clean == '':
            
            print ('My Group (',len(my_group),') =',my_group)
            total += len(my_group)
            my_group = []
            
        else:
                    
            print(clean)
            for char in range(0,len(clean)):
                if clean[char] not in my_group:
                    my_group.append(clean[char])

#Final Group
print ('My Group = ',len(my_group),my_group)
total += len(my_group)

print ('Total = ',total)
