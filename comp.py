# compile (c) for c*, copyright Takudzwa Makoni
from collections import Counter
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

#convert file to string
def C002(filename):    
    with open(filename) as f:
        src = f.readlines() 
        filestring = ''.join(i for i in src)
        filestring = filestring.replace('\n','')
        filestring = filestring.replace('\t','')
    return filestring
    
# check number of parentheses and get coords
def CA02(filestring,pf,pb):
    A_count=0
    B_count=0
    fwd = [] #coordinates for forward parentheses
    bck =[] #coordinates for backward parentheses
    for i in enumerate(filestring):

        if i[1] == pf:
            A_count += 1
            fwd.append(i[0])
        elif i[1] == pb:
            B_count += 1
            bck.append(i[0])
    if A_count != B_count:
        exit('syntax error: number of bracket "{ or }" mismatch in file')
    return fwd,bck

def CA12(filestring,f,b):
    oplist=[]
    for i in f:
        for j in b:
            if j > i:
                substr = filestring[i+1:j]
                chk = counter_check(substr)
                if chk[0] == True:
                    oplist.append(substr)
                    break
    return oplist
                
def counter_check(string,cpf='{',cpb='}',rpf='(',rpb=')',spf='[',spb=']',dq='"',sq="'",apf='<',apb='>'):
    C = Counter(string)
    if C[cpf] != C[cpb]:
        return False, 'exit code 1'
    if C[rpf] != C[rpb]:
        return False, 'exit code 2'
    if C[spf] != C[spb]:
        return False, 'exit code 3'
    if C[apf] != C[apb]:
        return False, 'exit code 4'
    if C[dq] % 2 != 0:
        return False, 'exit code 5'
    if C[sq] % 2 != 0:
        return False, 'exit code 6'
    else:
        return True, None


def check_subroutine(string):
    C = Counter(string)
    plist = [ C['{'], C['('],C['['],C['<'] ]
    chklist = [i!=0 for i in plist]
    if any(chklist):
        return chklist
    else:
        return False
    
def subroutine_build(subroutine_test,preops):
    if subroutine_test != False:
        paramlist = [('{','}'),('(',')'),('[',']'),('<','>')]
        sublist = []
        for i in enumerate(subroutine_test):
            if i[1]:
                sublist.append( A000(preops[ i[0] ], paramlist[i[0]][0] , paramlist[i[0]][1] ))
    return sublist
            
        

def A000(filestring,pf,pb):
    chk, code = counter_check(filestring)
    if not(chk):
        exit(code)
    
    fwd,bck = CA02(filestring,pf,pb)
    preops = CA12(filestring,fwd,bck)
    return preops


preops = A000( C002('test.c*') ,'{' ,'}' ) #C002 is the filestring
subroutine_test = [ check_subroutine(i) for i in preops ]
print(subroutine_test)
print( subroutine_build( subroutine_test , preops ) )
