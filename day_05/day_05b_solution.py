filename = 'day_05_input.txt'

max_id = 0

all_id = []

with open(filename) as f:
    
    for line in f:
        
        row_string = line[0:7]
        
        row_value = 0
        
        for char in range(0,7):
            if row_string[6-char] == 'B':
                row_value += 2**char
                

        column_string = line[7:10]
       
        column_value = 0
        
        for char in range(0,3):
            if column_string[2-char] == 'R':
                column_value += 2**char
        
        print(row_string,'=',row_value)
        print(column_string,'=',column_value)
        
        seat_id = (row_value * 8) + column_value
        all_id.append(seat_id)
                
        print(seat_id)
        

for i in range(0,len(all_id)):
    if i in all_id:
        pass
    else:
        if i-1 in all_id and i+1 in all_id:
            print('My ID =',i)