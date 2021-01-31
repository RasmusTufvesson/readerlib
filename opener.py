from .filters import *
from .reader import *
from .errors import *
import os
import logging
import sys
log = logging.getLogger(__name__)
class opener:
    def open_file(path):
        if file(path)!=False:
            try:
                return open(path, 'w+')
            except FileNotFoundError:
                raise FileNotFoundError('Could not find '+str(path))
            except:
                raise
                raise CouldNotOpen('Could not open '+str(path))
        else:
            raise NotAFile(str(path)+' in not a file')
    def open_all(files, opty):
        h={}
        for a in files:
            if file(a)!=False:
                try:
                    h[a]=open(a, opty)
                except FileNotFoundError:
                    raise FileNotFoundError('Could not find '+str(a))
                except:
                    raise
                    raise CouldNotOpen('Could not open '+str(a))
            else:
                raise NotAFile(str(a)+' is not a file')
        return h
    def make_import_all(fil, path):
        try:
            if file(fil)!=False:
                f=open(fil, 'w+')
            else:
                raise NotAFile(str(fil)+' is not a file')
        except FileNotFoundError:
            raise FileNotFoundError('Could not find file '+str(fil))
        except:
            err=sys.exc_info()
            raise
            raise CouldNotOpen(err[0].__name__+': '+str(err[1]))
        w=''
        r=reader(path)
        for a in r.read_all():
            if a == f or a[-3:] != '.py':
                continue
            w+='\nfrom .'+a[:-3]+' import *'
        try:
            f.write(w)
            log.info('Made import file')
        except:
            raise CouldNotWrite('Could not write to file')
        f.close()
    def __eq__(self, other):
        return (self.__class__ == other.__class__)
    def __ne__(self, other):
        return not self.__eq__(other)
    class file:
        def __init__(self, fp=os.getcwd()):
            self.path=fp
            self.pos=0
            try:
                if file(fp):
                    self.file=open(fp, 'w+')
                else:
                    raise NotAFile(str(fp)+' is not a file')
            except FileNotFoundError:
                raise FileNotFoundError('Could not find '+str(fp))
            except:
                err=sys.exc_info()
                raise
                raise CouldNotOpen(err[0].__name__+': '+str(err[1]))
            #except:
            #    raise
            #    raise CouldNotOpen('Could not open '+str(new))
        def __int__(self):
            return self.pos
        def __str__(self):
            return ' '.join(read(self.path))
        def __hash__(self):
            return hash(self.path)
        def __eq__(self, other):
            return (self.__class__ == other.__class__ and self.path == other.path)
        def __ne__(self, other):
            return not self.__eq__(other)
        def open(self):
            try:
                return self.file
            except AttributeError:
                raise FileNotFoundError('Could not find "file" parameter in "self"')
            except:
                err=sys.exc_info()
                raise
                raise ReaderError(err[0].__name__+': '+str(err[1]))
        def line(self, l):
            try:
                f=self.file
            except AttributeError:
                raise FileNotFoundError('Could not find "file" parameter in "self"')
            except:
                err=sys.exc_info()
                raise
                raise ReaderError(err[0].__name__+': '+str(err[1]))
            try:
                f.seek(l, 0)
            except:
                raise NotValidFilePosition('Could not set line position to '+str(l))
            #raise CouldNotRead('Failed to read line '+str(self.pos)+' in '+str(self.path))
            try:
                return f.readline()
            except:
                raise CouldNotRead('Failed to read line '+str(self.pos)+' in '+str(self.path))
        def len(self):
            try:
                return len(self.file.readlines())
            except AttributeError:
                raise FileNotFoundError('Could not find "file" parameter in "self"')
            except:
                raise CouldNotRead('Failed to read all lines in '+str(self.path))
        def characters(self):
            try:
                return len(list(self.file.read()))
            except AttributeError:
                raise FileNotFoundError('Could not find "file" parameter in "self"')
            except:
                err=sys.exc_info()
                raise
                raise CouldNotRead(err[0].__name__+': '+str(err[1]))
        def set_line(self, l):
            try:
                self.file.seek(l, 0)
                self.pos=l
            except:
                NotValidFilePosition('Could not set line position to '+str(l))
        def line_list(self):
            try:
                return self.file.readlines()
            except AttributeError:
                raise FileNotFoundError('Could not find "file" parameter in "self"')
            except:
                err=sys.exc_info()
                raise
                raise CouldNotRead(err[0].__name__+': '+str(err[1]))
        def pos(self):
            return self.pos
        class writer:
            def __init__(self, f=os.getcwd()):
                self.path=f
            def ready(self):
                try:
                    if file(self.path)!=False:
                        self.file=open(self.path, 'w+')
                    else:
                        raise NotAFile(str(self.path)+' is not a file')
                except FileNotFoundError:
                    raise FileNotFoundError('Could not find '+str(self.path))
                except:
                    err=sys.exc_info()
                    raise
                    raise CouldNotOpen(err[0].__name__+': '+str(err[1]))
            def __str__(self):
                return ' '.join(read(self.path))
            def __hash__(self):
                return hash(self.path)
            def __eq__(self, other):
                try:
                    return (self.__class__ == other.__class__ and self.path == other.path and self.file == other.file)
                except AttributeError:
                    err=sys.exc_info()
                    raise FileNotFoundError(err[0].__name__+': '+str(err[1]))
            def __ne__(self, other):
                return not self.__eq__(other)
            def replace(self, fro, to, new):
                try:
                    f=self.file.readlines()
                except AttributeError:
                    raise FileNotFoundError('Could not find "file" parameter in "self"')
                except:
                    raise CouldNotRead('Failed to read all lines in '+str(self.path))
                d=[]
                num=0
                for a in range(fro, to):
                    if num in new:
                        f[a]=new[num]
                    else:
                        d.append(f[a])
                    num+=1
                for b in range(len(d)-1, -1, -1):
                    del f[d[b]]
                try:
                    self.file.write(''.join(f))
                except AttributeError:
                    raise FileNotFoundError('Could not find "file" parameter in "self"')
                except:
                    err=sys.exc_info()
                    raise
                    raise CouldNotWrite(err[0].__name__+': '+str(err[1]))
            def write_list(self, l):
                try:
                    self.file.write(''.join(l))
                except AttributeError:
                    raise FileNotFoundError('Could not find "file" parameter in "self"')
                except:
                    err=sys.exc_info()
                    raise
                    raise CouldNotWrite(err[0].__name__+': '+str(err[1]))
            def duplicate(self, new):
                try:
                    if file(new)!=False:
                        f=open(new, 'w+')
                    else:
                        raise NotAFile(str(fp)+' is not a file')
                except FileNotFoundError:
                    raise FileNotFoundError('Could not find '+str(new))
                except:
                    err=sys.exc_info()
                    raise
                    raise CouldNotOpen(err[0].__name__+': '+str(err[1]))
                try:
                    f.write(self.file.read())
                except AttributeError:
                    raise FileNotFoundError('Could not find "file" parameter in "self"')
                except:
                    raise CouldNotWrite('Could not write to '+str(new))
                f.close()
