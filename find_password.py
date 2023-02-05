from time import monotonic
def find_password(n):
    t=monotonic()
    _,name=iterate(n-1,[""]*n,None)
    print("password :",name)
    print("time to find :",monotonic()-t)

def iterate(n,word,name):
    for i in iterate_on_all_characters():
        if n>0:
            word,name=iterate(n-1,word,name)
            if name!=None:return word,name
        word[n-1]=i
        name=try_name(word)
        if name!=None:
            return word,name
    if n==len(word)-1:
      if n>0:
        word,name=iterate(n-1,word,name)
        if name!=None:return word,name
      word[n-1]=i
      name=try_name(word)
      if name!=None:
          return word,name
    return word,name

def try_name(name):
  name="".join(name)
  if name==password:
    return name
  
def iterate_on_all_characters():
    for i in range(26):
        yield chr(i+65)
    for i in range(26):
        yield chr(i+97)
    for i in range(10):
        yield str(i)

def change_password(p):
  global password
  password=p

password="99999"

find_password(5)