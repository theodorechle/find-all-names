from time import monotonic
def find_all_names(n):
    t=monotonic()
    _,names=iterate(n-1,[""]*n,[])
    print(names)
    print(monotonic()-t)

def iterate(n,word,names):
    for i in iterate_on_all_characters():
        if n>0:
            word,names=iterate(n-1,word,names)
        word[n-1]=i
        name=try_name(word)
        if name!=None:
            names.append(name)

    return word,names

def try_name(name):
    try:
        name="".join(name)
        exec(name)
        return name
    except Exception:
        pass
def iterate_on_all_characters():
    for i in range(26):
        yield chr(i+65)
    for i in range(26):
        yield chr(i+97)

find_all_names(3)