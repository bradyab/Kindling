import os

def numfold(path):
	# path='/home/' + os.getlogin() + '/Code/Kindling/images/'
	# path = "./images/"
	files = folders = 0
	for _, dirnames, filenames in os.walk(path):
	  # ^ this idiom means "we won't be using this value"
	    folders += len(dirnames)

	return folders
def numfile(path):
	# path='/home/' + os.getlogin() + '/Code/Kindling/images/'
	files = folders = 0
	for _, dirnames, filenames in os.walk(path):
	  # ^ this idiom means "we won't be using this value"
	    files += len(filenames)

	return files

if __name__ == '__main__':
    print("files: "+str(numfile()))
    print("folders: "+str(numfold()))
