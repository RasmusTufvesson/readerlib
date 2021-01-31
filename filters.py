import os
def start(st, filt):
    n=list(st)
    if n[0]==filt:
        return False
    else:
        return st
def end(st, filt):
    n=st.split('.')
    if len(n)>1:
        if n[1]!=filt:
            return st
        else:
            return False
    else:
        return False
def name(st, filt):
    if st!=filt:
        return st
    else:
        return False
def search(st, filt):
    if filt in st:
        return False
    else:
        return st
def dot(st, *useless):
    n=st.split('.')
    if len(n)>1:
        return st
    else:
        return False
def file(st, *useless):
    if os.path.isdir(st):
        return False
    #elif os.path.isfile(st):
    else:
        return st
    #else:
    #    return True
