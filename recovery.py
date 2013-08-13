'''
Based on http://stackoverflow.com/questions/7374069/undo-git-reset-hard
and http://stackoverflow.com/questions/1108853/recovering-added-file-after-doing-git-reset-hard-head

-Run the following command and store response in file:
$ git fsck --cached --no-reflogs --lost-found --unreachable HEAD
-Execute this script on file.
'''

import sys
import os



if __name__ == "__main__":
	infile = sys.argv[1]
	
	os.system("mkdir recovery")
	print "recovery dir created"
	
	f = open(infile, "rU")
	
	for i, line in enumerate(f):
		word1, word1, blob = line.split(' ')
		#print blob[:-1]
		com = "git show " + blob[:-1] + " > recovery/file" + str(i+1) + ".txt"
		print com
		# format is: git show <blob num> > <filename>
		os.system(com)