import linecache

# will check if the string has a function/variable type
# and returns true if it does
def A001(string):
    typelist = ['int','string','char','void','float']
    if any(type in string for type in typelist):
        return True

# will check if the string has brackets (is a function)
# and returns true if it has
def A011(string):
	if ("(" or ")") in string:
		return True

# gets the function name and its parameters from the string
def B000(string):
    spltstr = string[:string.find(')') + 1]
    spltstr = spltstr.split()
    #print(spltstr,'B000 1')
    t = spltstr[0]
    spltstr = spltstr[1].split('(')
    #print(spltstr,'B000 2')
    name = spltstr[0]
    for i in spltstr:
        if ")" in i:
            argstr = i.rstrip(')')
            args = argstr.split(',') # list of arguments
    #print(t,name,args,'B000 3')
    return t, name, args

# read lines from first curly bracket line to ending curly bracket (finds end point)
# gets the code in the brackets, and split the with delimiter ';'
def B001(src,line_number):
    snippet = src[line_number:]
    for i in enumerate(snippet):
        i[1].find('{')
    curly = src[line_number:]
    #print(curly,' B001 2')
    return 'pickles'

#decodes the op string
def B003(string, TNP=None):
    return string

# strips ;)
def B002(string):
    string = string.strip('\n')
    string = string.strip('\t')
    string = string.strip()
    return string

def B005(code):
    f = open('output.cpp', 'a')
    f.write(code)
    f.close()

def C002(filename,a,b):
    sl = []
    #print(a[0],b[0],'C002 1')
    count = a[1] + 1
    while count <= b[1] + 2:
        line = linecache.getline(filename,count)
        linecache.clearcache()
        line = line.replace('\n','')
        #line = line.replace('\t','')
        #line = s[s.find('{')+1:s.find('}')]
        sl.append(line)
        count+=1
    x = ''.join(sl)
    x= x[a[0]+1:-2].replace('\t','').strip()
    return x

    
#check number of { and } in file and get coordinates
def CA02(filename,pf,pb,MAIN=True):
    A_count=0
    B_count=0
    if MAIN == True:
        with open(filename) as f:
            fwd = [] #coordinates for forward parentheses
            bck =[] #coordinates for backward parentheses
            for line in enumerate(f):
                for i in enumerate(line[1]):
                    if i[1]==pf:
                        A_count+=1
                        fwd.append((i[0],line[0]))
                    if i[1]==pb:
                        B_count+=1
                        bck.append((i[0],line[0]))
        if A_count != B_count:
            exit('syntax error: number of bracket "{ or }" mismatch in file')
        else:
            return fwd,bck
    else:
        for i in filename: #filename is actually a string here
            if i==pf:
                A_count+=1
            if i==pb:
                B_count+=1
        print(A_count,B_count)
        if A_count == B_count:
            return True
        else:
            return False
 
def CA12(filename,fwd,bck):
    oplist =[]
    for a in enumerate(fwd):
        for i in range(0,len(fwd)):
            op = C002(filename,a[1],bck[i])
            if CA02(op,'{','}',False):
                oplist.append(op)
    print(oplist,fwd)
                #check of equal number of { and } between a and b
                #pair the parentheses and get substrings between them
                #print(pf,'and',pb,'equal','CA02')
    
        
with open('test.c*') as f:
    fwd,bck = CA02('test.c*','{','}')
    CA12('test.c*',fwd,bck)
    SRC = f.readlines()
    LN = 0
    while LN != len(SRC):
        for line in enumerate(SRC):
            if A001(line[1]): #if type
                if A011(line[1]): #if function
                    TNP = B000(B002(line[1]))
                    OPS = B001(SRC,line[0])
                    CDE = B003(OPS,TNP)
                    B005(CDE)
                else:
                    B005( B003(line[1]))
            else:
                pass
                #print('fash n chapss')
        LN+=1
