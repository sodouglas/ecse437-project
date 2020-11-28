#!/usr/local/bin/python3
import os

# stash any changes to make sure working directory is clean
os.system("git stash")

# checkout the master branch 
os.system("git checkout master")

# create test file
os.system("touch test.txt")

# write to test file
os.system("echo hello > test.txt")

# use git add and git commit to commit the changess
os.system("git add .")
os.system("git commit -m 'test push'")

# push the changes
os.system("git push")

exit(0)
