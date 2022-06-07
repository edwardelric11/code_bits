#File Objects

##The Basics:
#reading mode f = open("test.txt", "r")
#write f = open("test.txt", "w")
#append f = open("test.txt", "a")
#read and write f = open("test.txt", "r+")
#print(f.name)
#print(f.mode)
#f.close()

##Reading Files:
#with open("test.txt", "r") as f:
	#pass

	##Small Files:
	#f_contents = f.read()
	#print(f_contents)

	##Big Files:
	#f_contents = f.readlines()
	#print(f_contents)

	##Iterating through the file:
	for line in f:
		print(line, end = '')

	##Printing by characters:
	f_contents = f.read(100)
	print(f_contents, end = '')
	

	###Iterating through small chunks, with 10 characters::
	with open('test.txt', 'r') as f:
    
    size_to_read = 10
    
	  f_contents = f.read(size_to_read)
    
	  while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)

#print(f.mode)
#print(f.closed)
#print(f.read())



##Copying Files:
with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)

#Copying an image, without chunks:
#with open("demo.jpg", "r") as rf:
	#with open("demo_copy.jpg", "w") as wf:
		#for line in rf:
			#wf.write(line)


###Copying image with chunks:
#with open("demo.jpg", "rb") as rf:
	#with open("bdemo_copy.jpg", "wb") as wf:
		#chunk_size = 4096
        #rf_chunk = rf.read(chunk_size)
        #while len(rf_chunk) > 0:
            #wf.write(rf_chunk)
            #rf_chunk = rf.read(chunk_size)
