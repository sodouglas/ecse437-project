#!/usr/local/bin/python3
import os

# stash any changes to make sure working directory is clean
os.system("git stash")

# checkout the master branch
os.system("git checkout master")

# create a new branch
os.system("git checkout -b experiment-stylecheck")

# create a style error in second line of googler file
file = open("googler", "r")
lines = file.readlines()
lines[1] = "#badstyle\n"
file = open("googler", "w")
file.writelines(lines)
file.close()

# use git add and git commit to commit the changess
os.system("git add .")
os.system("git commit -m 'experiment stylecheck'")

# push the changes
os.system("git push --set-upstream origin experiment-stylecheck")

# open PR link
os.system("open https://github.com/emmaeagles/ecse437-project/compare/experiment-stylecheck?expand=1")

exit(0)
