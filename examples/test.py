import reader as r
import os
reader = r.reader(os.getcwd()) # make the reader
filt = r.reader.filter(os.getcwd()) # make the reader filter
print (reader.read_all()) # print all things in a folder

print (r.normal_read(os.getcwd())) # print all things in a folder that pass the basic filter

print (filt.end_filter('txt')) # print all things in a folder that dont have the txt file type

#combind filters
read1 = filt.start_filter('_') # get all things in a folder that dont start with "_"

read2 = r.create_list(read1, 'hello_world.py', r.name) # combind the start filter with the name filter

print (read2) # print all things in a folder that passed boath filters

#search after all folders
read1 = filt.file_filter() # get all files in a folder

read2 = filt.invert(read1) # invert the files in read1 and get the folders instead of files

print (read2) # print all the folders in a folder
