li = []
def spansub(stri, substri):
    x = len(substri)
    for i in range(len(stri)):
        subs = x+i
        if substri == stri[i:subs]:
            li.append((i,subs))

    print(len(li), li)

if __name__ == "__main__":
    strio = input("enter the string")
    substrio = input("enter the sub_string")
    spansub(strio, substrio)