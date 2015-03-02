import sys
import os

def findAllFiles( fileDirectory, fileExtension ):
	returnFiles = []
	if os.path.isdir(fileDirectory):
		for FILE in os.listdir( fileDirectory ):
			print FILE
			if str( FILE ).endswith( fileExtension ):
				returnFiles.append( str( FILE ).replace( '.' + fileExtension, '' ) )

		print returnFiles
		return returnFiles
		
	else:
		print "not a directory"

print findAllFiles("/", ".txt")

