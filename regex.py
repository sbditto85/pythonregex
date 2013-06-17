import re
from Tkinter import *

def command(f,*args,**kwargs):
    return lambda: f(*args,**kwargs)

root = Tk()
root.title("Regex Playin' Around")

top = Frame(master=root)
filtertext = Text(master=top,width=120,height=20)
filtertext.pack(side=LEFT)

middle = Frame(master=root)
regextext = Text(master=middle,width=123,height=1)
regextext.pack(side=LEFT,fill=X)

bottom = Frame(master=root)
resulttext = Text(master=bottom,width=120,height=20)
resulttext.pack(side=LEFT,fill=X)
#txtarea.config(state=DISABLED)

#functions
def findall():
    s = filtertext.get(1.0,END)[:-1]
    rs = regextext.get(1.0,END)[:-1]
    if s and rs:
        r = re.compile(rs)
        resulttext.delete(1.0,END)
        resulttext.insert(INSERT,r.findall(s))
        
def search():
    s = filtertext.get(1.0,END)[:-1]
    rs = regextext.get(1.0,END)[:-1]
    if s and rs:
        r = re.compile(rs)
        resulttext.delete(1.0,END)
        found = r.search(s)
        if found:
            start, end = found.start(), found.end()
            resulttext.insert(INSERT," ".join(["start:",str(start),"\n"]))
            resulttext.insert(INSERT," ".join(["stop:",str(end),"\n"]))
            resulttext.insert(INSERT," ".join(["subtring:",s[start:end],"\n"]))
            resulttext.insert(INSERT," ".join(["groups:",str(found.groups()),"\n"]))
        
def match():
    s = filtertext.get(1.0,END)[:-1]
    rs = regextext.get(1.0,END)[:-1]
    if s and rs:
        r = re.compile(rs)
        resulttext.delete(1.0,END)
        found = r.match(s)
        if found:
            start, end = found.start(), found.end()
            resulttext.insert(INSERT," ".join(["start:",str(start),"\n"]))
            resulttext.insert(INSERT," ".join(["stop:",str(end),"\n"]))
            resulttext.insert(INSERT," ".join(["subtring:",s[start:end],"\n"]))
            resulttext.insert(INSERT," ".join(["groups:",str(found.groups()),"\n"]))
            
def sub():
    s = filtertext.get(1.0,END)[:-1]
    rs = regextext.get(1.0,END)[:-1]
    st = subtext.get(1.0,END)[:-1]
    if not st: st = ""
    if s and rs:
        r = re.compile(rs)
        resulttext.delete(1.0,END)
        try:
            resulttext.insert(INSERT,r.sub(st,s))
        except:
            resulttext.insert(INSERT,"DOH! had an error")
            
def split():
    s = filtertext.get(1.0,END)[:-1]
    rs = regextext.get(1.0,END)[:-1]
    if s and rs:
        r = re.compile(rs)
        resulttext.delete(1.0,END)
        resulttext.insert(INSERT,r.split(s))

# Add buttons to toolbar
toolbar = Frame(master=root)
findallbutton = Button(master=toolbar, text="Findall", command=findall)
findallbutton.pack(side=LEFT)
searchbutton = Button(master=toolbar, text="Search", command=search)
searchbutton.pack(side=LEFT)
matchbutton = Button(master=toolbar, text="Match", command=match)
matchbutton.pack(side=LEFT)
splitbutton = Button(master=toolbar, text="Split", command=split)
splitbutton.pack(side=LEFT)
label = Label(master=toolbar, text="Sub String:")
label.pack(side=LEFT)
subtext = Text(master=toolbar,width=50,height=1)
subtext.pack(side=LEFT)
subbutton = Button(master=toolbar, text="Sub", command=sub)
subbutton.pack(side=LEFT)
quitbutton = Button(master=toolbar, text="Quit", command=root.quit)
quitbutton.pack(side=LEFT)

filterheader = Frame(master=root)
label = Label(master=filterheader, text="Original String:")
label.pack(side=LEFT)
filterheader.pack(fill=X)
top.pack()

regexheader = Frame(master=root)
label = Label(master=regexheader, text="Regex String:")
label.pack(side=LEFT)
regexheader.pack(fill=X)
middle.pack()

toolbar.pack(fill=X)

resultheader = Frame(master=root)
label = Label(master=resultheader, text="Result String:")
label.pack(side=LEFT)
resultheader.pack(fill=X)
bottom.pack() 

# Make the Text area scrollable (scrollable widget (Listbox, Text, Canvas, Entry) and its scrollbar must have same parent)

xrscrollbar = Scrollbar(master=bottom)
xrscrollbar.pack(side=RIGHT,fill=Y)
resulttext.config(yscrollcommand=xrscrollbar.set)
xrscrollbar.config(command=resulttext.yview)

xfscrollbar = Scrollbar(master=top)
xfscrollbar.pack(side=RIGHT, fill=Y)
filtertext.config(yscrollcommand=xfscrollbar.set)
xfscrollbar.config(command=filtertext.yview)

if __name__ == "__main__":
    root.mainloop()