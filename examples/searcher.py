import reader as r
start = 'C:\\Users'
target = 'searcher.py'
found = False
loop = False

def search(path, target):
    global found
    global loop
    #print (path) 
    filt = r.reader.filter(path)
    files = filt.file_filter()
    files = r.create_list(files, 'bin', r.end)
    #files = r.create_list(files, 'ini', r.end)
    #files = r.create_list(files, 'xml', r.end)
    if target in files:
        found=True
        #print ('found in '+' '.join(files))
        return path
    folders = filt.invert(files)
    #print (folders)
    if target in folders:
        found=True
        #print ('found in '+' '.join(folders))
        return path
    if found==True:
        return path
    #print (files)
    #print (folders)
    for a in folders:
        print ('traveling to '+path+'\\'+a)
        p=search(path+'\\'+a, target)
        if type(p)!=type(None):
            return path

p=search(start, target)
#print (found)
if found:
    print ('found '+target+' at '+p)
else:
    print ('could not find '+target)
