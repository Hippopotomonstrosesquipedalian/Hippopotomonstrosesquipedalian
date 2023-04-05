c=""
p=input("What is the file path of the Hippopotomonstrosesquipedalian programme you want to run (including disk name)?\n")
f=open(p,"r")
r=f.readlines()
for x in range(0,len(r)):
    if r[x]=="pneumonoultramicroscopicsilicovolcanoconiosis" or r[x]=="pneumonoultramicroscopicsilicovolcanoconiosis\n":
        c=c+"1"
    elif r[x]=="hippopotomonstrosesquipedalian" or r[x]=="hippopotomonstrosesquipedalian\n":
        c=c+"0"
    else:
        raise SyntaxError("You cannot use a word other than 'hippopotomonstrosesquipedalian' or 'pneumonoultramicroscopicsilicovolcanoconiosis'. Is each word on its own line?")
d=int(c, 2)
l=(d.bit_length() + 7)//8
n=d.to_bytes(l,"big")
t=n.decode()
f.close()
g=open("programme_made_by_compiler_do_not_touch.py","w")
g.write(t)
g.close()
exec(open("programme_made_by_compiler_do_not_touch.py").read())
open("programme_made_by_compiler_do_not_touch.py").close()