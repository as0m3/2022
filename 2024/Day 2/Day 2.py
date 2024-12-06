

def main():
    file = open("Day 2\input.txt", 'r')

    safe_reports: int = 0

    for line in file:
        line = line.strip()
        line = line.split(" ")

        # numbers must be all asc or desc
        # and can only be a difference between 1 and 3
        #     between two numebrs

        asc: bool = True if int(line[0]) < int(line[1]) else False
        safe: bool = True
        
        for i in range(1,len(line)):
            if safe is False:
                break
            dist = abs(int(line[i-1]) - int(line[i]))
            if dist >= 1 and dist <= 3:
              asc_test: bool = True if int(line[i-1]) < int(line[i]) else False
              if asc != asc_test:
                  safe = False
            else:
                safe = False

        if safe is True:   
            safe_reports += 1
    
    print("Safe reports: ", safe_reports)



if __name__ == '__main__':
    main()
