filename = 'day_04_input.txt'

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid = 0

with open(filename) as f:

    passport = {}
    
    for line in f:
    
        if line.rstrip() == '':
            
            print(passport.keys())
            
            if set(required).issubset(set(passport.keys())):
            
                print("TRUE")
                valid += 1
                
            else:
            
                print("FALSE")
            
            passport.clear()
            
        else:
        
            for fields in line.rstrip().split(' '):
            
                passport[fields.split(':')[0]] = fields.split(':')[1]

print ('Valid Passports = ',valid)
