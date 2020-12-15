filename = 'day_06_input.txt'

my_group = []

total = 0

with open(filename) as f:
   
    for line in f:
    
        clean = line.strip()
        
        if clean == '':
            
            print ('My Group (',len(set.intersection(*my_group)),') =',my_group)
            total += len(set.intersection(*my_group))
            my_group = []
            print('Next Group!')
            
        else:
                    
            print(clean)
            my_group.append(set(clean))

#Final Group
print ('My Group (',len(set.intersection(*my_group)),') =',my_group)
total += len(set.intersection(*my_group))
    
print ('Total = ',total)
