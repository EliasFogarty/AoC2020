filename = 'day_04_input.txt'

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid = 0

with open(filename) as f:

    passport = {}

    for line in f:

        if line.rstrip() == '':

            if set(required).issubset(set(passport.keys())):

                isValid = True

                for key,value in passport.items():

                    print(key,value)

                    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                    if key == "byr":
                        if int(value) not in range(1920,2003):
                            isValid = False
                    
                    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                    if key == "iyr":
                        if int(value) not in range(2010,2021):
                            isValid = False
                    
                    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                    if key == "eyr":
                        if int(value) not in range(2020,2031):
                            isValid = False
                    
                    # hgt (Height) - a number followed by either cm or in:
                        # If cm, the number must be at least 150 and at most 193.
                        # If in, the number must be at least 59 and at most 76.
                    if key == "hgt":
                        if value[-2:] == "cm":
                            if int(value[:-2]) not in range(150,194):
                                isValid = False
                        elif value[-2:] == "in":
                            if int(value[:-2]) not in range(59,77):
                                isValid = False  
                        else:
                            isValid = False
                    
                    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                    if key == "hcl":
                        if value[:1] != '#' or len(value) != 7:
                            isValid = False
                    
                    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                    if key == "ecl":
                        if value not in ("amb","blu","brn","gry","grn","hzl","oth"):
                            isValid = False
                    
                    # pid (Passport ID) - a nine-digit number, including leading zeroes.
                    if key == "pid":
                        if len(value) != 9:
                            isValid = False
                
                print(isValid)
                
                valid += 1 if isValid else 0

            passport.clear()

        else:

            for fields in line.rstrip().split(' '):
            
                passport[fields.split(':')[0]] = fields.split(':')[1]

print ('Valid Passports = ',valid)
