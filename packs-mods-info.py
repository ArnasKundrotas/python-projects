# Prevent your module's user from running your code as an ordinary script.

import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()

# Code ensuring that the directory is traversed by Python in order to find all requested modules.
# example some additional and necessary packages are stored inside the D:\Python\Project\Modules directory.

import sys

sys.path.append("D:\\Python\\Project\\Modules")

# abc
# |__ def
#      |__ mymodule.py

import abc.def.mymodule