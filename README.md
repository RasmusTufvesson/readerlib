objects:
	path = the place where you want to read

	filt = what a filter should search for

	filenames = a list of file names

	filtercommand = a filter type command

	reader = an object made with: reader(path)

	filter = an object made with: reader.filter(path)

	opener = an object made with: opener()

	file = an object made with: opener.file(path)

	writer = an object made with: file.writer(path)

filter commands:
	start(string, filt): if the string starts with *filt* it will return "False" if not it will return the string
	Output: string(filters: begins with *filt*) or False

	end(string, filt): if the string cant be divided by a point or the other half of the string is *filt* it will return "False" if not it will return the string
	Output: string(filters: file type *filt*) or False

	name(string, filt): if the string equals *filt* it will return "False" if not it will return the string
	Output: string(filters: file name *filt*) or False

	search(string, filt): if *filt* is inside the string it will return "False" if not it will return the string
	Output: string(filters: *filt* in file name) or False

	file(path): if *path* is a folder it will return "False" if *path* is a file it returns *path* if *path* is a special file returns "True"
	Output: path or False

	dot(string): if the string does not contain a filetype it will return "False" if not it will return the string
	Output: string(filters: no file type in *string*) or False

basic:
	normal_read(path): reads everything in that *path* and then filters out things that start with "_" and then removes the file type
	Output: filenames(filters: begins with "_", removes: file type)

	create_list(filenames, filt, filtercommand): returns *filenames* that pass the given filter command
	Output: filenames(filters: filtercommand(filt))

reader:
	reader(path): returns reader object
	Output: reader

	reader.read_all(): returns all files in *path*
	Output: filenames

	reader.open_path(filename): returns the exact position of a file or folder
	Output: path

	reader.update_path(path): updates the readers inbuilt path variable

	reader.real_path(filenames): returns a list of *filenames* with their full names
	Output: filenames(added: full name)

	reader.path_back(): returns the parent folder of *path*
	Output: path

filter:
	reader.filter(path): returns filter object
	Output: filter

	filter.start_filter(filt): returns all files in *path* that dont start with *filt*
	Output: filenames(filters: begins with *filt*)

	filter.end_filter(filt): returns all files in *path* that dont have the *filt* file type
	Output: filenames(filters: file type *filt*)

	filter.name_filter(filt): returns all files in *path* that are not named *filt*
	Output: filenames(filters: file name *filt*)

	filter.search_filter(filt): returns all files in *path* that dont have *filt* in there name
	Output: filenames(filters: *filt* in file name)

	filter.file_filter(): returns all files that are in *path*
	Output: filenames(filters: not file)

	filter.dot_filter(): returns all things in *path* that do not contain a filename
	Output: filenames(filters: no file type)

	filter.invert(filenames): inverts the given *filenames* using *path*
	Output: filenames(filters: inverted)

	filter.remove_filetype(filenames): removes filetypes from the given *filenames*
	Output: filenames(remove: file type)

opener:
	opener.open_file(path): if *path* is a file it returns the file if not it returns "False"
	Output: file(location: *path*) or False

	opener.open_all(filenames(need: the exact location of files), open_type): returns a list of the opend files from *filenames*
	Output: dict: files

	opener.make_import_all(output_file, path): Warning! *output_file* must be inside *path*! creates or edits the file *output_file* and writes import lines for all of the diferent python files in *path*

	opener.file(path): returns a file class object
	Output: file

file:
	file.open(): returns the file
	Output: openfile

	file.line(line): returns a line in the file
	Output: line

	file.line_list(): returns a list of all lines in the file
	Output: list: lines

	file.len(): returns the length of the file by lines in it
	Output: int: length(lines in the file)

	file.characters(): returns the amount of characters in the file
	Output: int: length(characters in the file)

	file.set_line(line): sets the reader head line to *line*
	
	file.pos(): returns the reader heads current line
	Output: int: line

	file.writer(path): returns the writer object
	Output: writer

writer:
	writer.ready(): Warning! this command is needed to be able to use all writer commands! opens *path* so that it can be writen to

	writer.replace(from, to, list: newlines): replaces the lines between *from* and *to* with *newlines* if there is nothing at that line in *newlines* it deletes the line from the file

	writer.duplicate(newpath): duplicates the files contents to *newpath*

	writer.write_list(list: newlines): writes a list to the file

for examples look in "examples"