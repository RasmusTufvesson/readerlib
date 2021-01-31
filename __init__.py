import os
import logging
__title__ = 'daleks'
__author__ = 'LarsTu'
__version__ = '2.2'
#logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
#path='D:\Rasmus\python\discord_bot\songs'
def normal_read(path):
    #global path
    h=[]
    for filename in os.listdir(path): # . is cwd
        if _filter_out(filename)!=False:
            h.append(filename.split('.')[0])
    return h
def _filter_out(name):
    n=list(name)
    if n[0]=='_':
        return False
    else:
        return name

from .reader import reader, create_list
from .filters import *
from .opener import opener
from .errors import *
"""
__all__=[reader, create_list, start, end, name, search, dot, file, opener]

#ex_filters={}
def imp():
    global __all__
    #global ex_filters
    #fi=__file__
    #fi=fi.split('\\')
    #del fi[len(fi)-1]
    #p='\\'.join(fi)+'\\expansions\\filters'
    #filt=reader.filter(p)
    #f=filt.end_filter('py')
    #f=filt.invert(f)
    #for a in f:
    #    ex_filters[a]=__import__('expansions.filters.'+a)
    log.fatal('does this print?')
    modules = glob.glob(os.path.join(os.path.dirname(__file__)+'\\expansions\\filters', "*.py"))
    log.info(str(modules))
    for a in [ os.path.basename(f)[:-3] for f in modules if os.path.isfile(f) and not f.endswith('__init__.py')]:
        log.info(a)
        __all__.append(os.path.dirname(__file__)+'\\expansions\\filters\\'+a)
        log.info(str(__all__))

log.fatal('DOES THIS WORK')
imp()
"""

opener.make_import_all(os.path.dirname(__file__)+'\\expansions\\filters\\importer.py', os.path.dirname(__file__)+'\\expansions\\filters')
from .expansions.filters.importer import *
log.info('imported extra exceptions')
opener.make_import_all(os.path.dirname(__file__)+'\\expansions\\exceptions\\importer.py', os.path.dirname(__file__)+'\\expansions\\exceptions')
from .expansions.exceptions.importer import *
log.info('imported extra filters')
log.info('imported expansions')

if __name__=='__main__':
    print (normal_read(os.getcwd()))
    print (os.getcwd())
del os
del logging
del log
