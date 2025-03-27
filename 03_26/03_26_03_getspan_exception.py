li = []
def spansub(stri, substri):
    if (stri == '' or substri == ''):
        raise Exception("please enter the input properly")
    else:
        x = len(substri)
        for i in range(len(stri)):
            subs = x+i
            if substri == stri[i:subs]:
                li.append((i,subs))

        print(len(li), li)

if __name__ == "__main__":
    
    try:
        strio = input("enter the string")
        substrio = input("enter the sub_string")
        spansub(strio, substrio)
    except Exception as e:
        print(e)