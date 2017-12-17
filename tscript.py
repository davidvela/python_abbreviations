import re 

def cal_score(letter): 
    if letter[0] == 0: 
        return 0 
    if letter[0] == -1: 
        if letter[1] == "E":
            return 15
        else:
            return 2
    else: 
        val = valdic[letter[1]] # read values 
        return  int(val) + letter[0]


def names(input): 
    letters = []
    for word in input: 
        for i in range(len(word)):
            letters.append( [ i, word[i]] )
        letters[-1][0] = -1 #last letter in a word 
    letters[-1][0] = -1 #last letter in a word
    #print(letters)        
    lenLet = len(letters)
    if lenLet < 1: 
        return ""
    fAB = letters[0]
    if lenLet < 2: 
        return fAB[1]
    sAB = letters[1]
    if lenLet < 3: 
        return fAB[1] + sAB[1]
    tAB = letters[2]
    if lenLet < 4: 
        return fAB[1] + sAB[1] + tAB[1]
    
    # else => logic 
    ps = 1; pt = 2; #POSITION SECOND/THIRD
    lc = 10000 # last calculation
    while ps < lenLet-1:
        sAB = letters[ps]
        while pt < lenLet:
            tAB = letters[pt]
            # do calculation
            mc = cal_score(sAB) + cal_score(tAB)
            if mc < lc: 
                lc = mc
                ret = fAB[1] + sAB[1] + tAB[1]
                #print("{}--{}".format(mc, ret))
            elif mc == lc: 
                ret = ret + " , " + fAB[1] + sAB[1] + tAB[1]
            pt += 1
        ps += 1
        pt = ps+1
               
    return ret

def cleanLine(txt):
    txt = txt.replace("'", "")
    #txt = txt.replace("-", " ")
    txt = re.sub('[^a-zA-Z]+', ' ', txt)
    return txt

if __name__ == '__main__':
    print("Abreviations program! ")

    # Read names.txt 
    data = []
    # sometimes this can give a problem ... 
    # if it does try the new line with just \n
    f = open("./names.txt","r", newline='\r\n') 
    for line in f: 
        # print(line.split())
        cline = cleanLine(line)
        dat = cline.upper().split()
        # print(dat)
        data.append(dat)
    f.close()
    # print(data)

    # Store values in a dictionary 
    values = []
    f = open("./values.txt","r", newline='\r\n') 
    for line in f: 
        #print(line.split())  
        values.append(line.upper().split())
    f.close()
    # print(values[0:5])
    valdic = dict([ (v[0], v[1]) for v in values ])
    #print(values)

    # Calculate Ab. 
    f = open("./names_abbrevs.txt","w", newline='\n') 
    for name in data: 
        ab =  names(name)
        outline = str(name) + "  -  " + str(ab) + "\n"
        # print("{} - {} ".format(name,ab ))
        print(outline)
        #Store the string in a file: names_abbrevs.txt
        f.write(outline)
    f.close()
