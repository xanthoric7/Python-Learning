 # need to import the current working directory DONE os.getcwd
 # count number of directories beneath current working directory Done i =
 # create a square array(dictionary?) based on number of directories
 # add an extra column to make row/cols be odd if not alrealdy odd
 # start player on 'bottom' row in the middle
 # rooms have treaseure, trap, monster
 #
 #  os.path.isdir(PATH)
 #
 #
import os
cwd = os.getcwd()
print "Current location: ", cwd

i = 0

for root, dirs, files in os.walk(".", topdown=False) :
    for name in dirs :
        print "Current Location: ", (os.path.join(root, name))
        i += 1
        print "Seed:", i

seed = i

# best to start a list here and map to it with a function for randomizing
# the room contents for each room
rooms = [range(0,i)]
#farts 
