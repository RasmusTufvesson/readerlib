import reader
start='C:'
location=start
read=reader.reader(start)
while True:
    new_path=location
    print (' '.join(read.read_all())+' back')
    i=input('how do you want to move?\n')
    if i=='back':
        if location==start:
            break
        new_path=read.path_back()
    else:
        if reader.file(i)!=False:
            r=reader.opener.open_file(read.open_path(i))
            if type(r)!=type(True):
                print (r.read())
            else:
                new_path=read.open_path(i)
        else:
            new_path=read.open_path(i)
    location=new_path
    read.update_path(new_path)
