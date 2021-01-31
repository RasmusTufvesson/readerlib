import os
import sys
from .filters import *
from .errors import *
import logging
log = logging.getLogger(__name__)
def create_list(li, re, filt, ignore_errors = False):
    h=[]
    for filename in li:
        try:
            try:
                filt
            except NameError:
                if not ignore_errors:
                    raise NotAFilter(str(filt)+' is not a function')
            if filt(filename, re)!=False:
                h.append(filename) #.split('.')[0]
        except:
            if not ignore_errors:
                err=sys.exc_info()
                raise CouldNotRead(err[0].__name__+': '+str(err[1]))
    return h
def read(path):
    h=[]
    try:
        for filename in os.listdir(path): # . is cwd
            #if filterout(filename)!=False:
            #h.append(filename.split('.')[0])
            h.append(filename)
    except NotADirectoryError as err:
        raise CouldNotOpen('NotADirectoryError: '+str(err))
    except:
        err=sys.exc_info()
        raise CouldNotRead(err[0].__name__+': '+str(err[1]))
        #raise CouldNotOpen('Could not open '+str(path))
    return h
class reader:
    def __init__(self, path='C:\\'):
        self.path=path
    def read_all(self):
        return read(self.path)
    def open_path(self, path):
        return self.path+'\\'+path
    def update_path(self, path):
        self.path=path
    def real_path(self, files):
        re=[]
        for a in files:
            re.append(self.path+'\\'+a)
        return re
    def path_back(self):
        f=self.path.split('\\')
        l=len(f)-1
        an=[]
        if l>0:
            for a in range(0,l):
                an.append(f[a])
            log.info('removed directory name from path')
        else:
            raise ListToShort('Could not remove last directory name')
        return '\\'.join(an)
    def __str__(self):
        return ' '.join(read(self.path))
    def __hash__(self):
        return hash(self.path)
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.path == other.path)
    def __ne__(self, other):
        return not self.__eq__(other)
    class filter:
        def __init__(self, s='C:\\'):
            self.path=s
        def start_filter(self, filt):
            return create_list(read(self.path), filt, start)
        def end_filter(self, filt):
            return create_list(read(self.path), filt, end)
        def name_filter(self, filt):
            return create_list(read(self.path), filt, name)
        def search_filter(self, filt):
            return create_list(read(self.path), filt, search)
        def file_filter(self):
            filt=None
            return create_list(read(self.path), filt, file)
        def dot_filter(self):
            filt=None
            return create_list(read(self.path), filt, dot)
        def invert(self, re):
            re2=read(self.path)
            an=[]
            for a in re2:
                if a not in re:
                    an.append(a)
            log.info('inverted file')
            return an
        def remove_filetype(self, re):
            an=[]
            for a in re:
                an.append(a.split('.')[0])
            log.info('removed filetype')
            return an
        def __str__(self):
            return ' '.join(read(self.path))
        def __hash__(self):
            return hash(self.path)
        def __eq__(self, other):
            return (self.__class__ == other.__class__ and self.path == other.path)
        def __ne__(self, other):
            return not self.__eq__(other)
