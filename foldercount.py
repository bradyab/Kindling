import os

def numfold():
	# path='/home/' + os.getlogin() + '/Code/Kindle/images/'
	path='/home/' + os.getlogin() + '/Code/Kindling/images/'
	files = folders = 0
	for _, dirnames, filenames in os.walk(path):
	  # ^ this idiom means "we won't be using this value"
	    folders += len(dirnames)

	return folders
def numfile():
	path='/home/' + os.getlogin() + '/Code/Kindling/images/'
	files = folders = 0
	for _, dirnames, filenames in os.walk(path):
	  # ^ this idiom means "we won't be using this value"
	    files += len(filenames)

	return folders

if __name__ == '__main__':
    print(str(numfile()))
    print(str(numfold()))
