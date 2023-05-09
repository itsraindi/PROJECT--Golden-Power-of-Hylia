def displayScreen(graph, poly, clean=False):
    if(clean):
        graph = graph.replace("·", " ")

    for i in range(20):
        print(" ".join(graph[i*20:(i+1)*20]),end="\t\t")
        if(i%2==1 and i//2<len(poly)):
            print(poly[i//2], end="")
        print()


g = "···············|···················|··········#········|···················|···················|···················|···········#·······|···················|···················|············#······|·@@@··············@@@··············@@@·|···········@@#@····|···#····@@@········|····@@@@······#····|··#·---------------+----···········#···|·#··············#··|#················###···················|····"
p = ["@: 0.3x + 5","#: 0.25x² + 0.25x - 3","&: ", "$: ","%: "]

displayScreen(g,p)
print()
displayScreen(g,p,True) #clean version so as to provide a different look

def checkAndConvert(value):
    if(not(isinstance(value,str))):
        return None
    value = value.strip()
    
    if(len(value)==0):
        return None

    neg = 1
    if(value[0] == "-"):
        neg = -1
        value = value[1:]

    out = 0
    t = -1
    for v in value:
        if(t>=0):
            t += 1
        if(v==" "):
            return None
        if(v=="."):
            if(t==-1):
                t=0
                continue
            else:
                return None
        if("0"<=v and v<="9"):
            out = out*10 + int(v)
        else:
            return None
    
    if(t==-1):
        return neg*out
    return neg*out/(10**t)

        
    
while(True):
    user = input("Enter a number: ")
    num = checkAndConvert(user)

    if(num==None):
        print("...enter only integer or decimal point numbers\n\n")
    else:
        print("\nThe value entered was: "+str(num))
        print("\n\n")





