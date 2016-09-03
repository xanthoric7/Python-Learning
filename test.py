# print 'hello world \n tits' ;banner = "FreeFloatFTP Server"
# print banner, type(banner)
# portList = [21,22,23,23,34]
# print portList, type(portList)
# print banner.upper()
# print banner.lower()
# portList.append(21)
# portList.append(443)
# portList.append(80)
# print portList
# portList.sort()
# print portList
# count = len(portList)
# print count
# services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
# print services.keys()
# print services.items()
# print services.has_key('ftp')
# print services['ftp']
# print "[+] Found vuln with FTP on port "+str(services['ftp'])
# import socket
# socket.setdefaulttimeout(2)
# s = socket.socket()
# try:
#     s.connect(("192.168.95.148",21))
# except Exception, e:
#     print  "[-] Error = "+str(e)
# try:
#     print "[+] 1337/0 = "+str(1337/0)
# except Exception, e:
#     print "[-] Error = "+str(e)
# import socket
# def retBanner(ip, port):
#     try:
#         socket.setdefaulttimeout(2)
#         s = socket.socket()
#         s.connect((ip, port))
#         banner = s.recv(1024)
#         return banner
#     except:
#         return
# def main():
#     ip1 = '192.168.95.148'
#     ip2 = '192.168.95.149'
#     port = 21
# banner1 = retBanner(ip1, port)
# if banner1:
#     print '[+] ' + ip1 + ': ' + banner1
# banner2 = retBanenr(ip1, port)
# if banner2:
#     print '[+] ' + ip2 + ': ' + banner2
# if __name__ == '__main__':
#     main()
# from sys import argv
#
# script, user_name = argv
# prompt = '> '
#
# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like ot ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
# print """
# Alright, so you said %s about liking me.
# You live in %s. Not sure where that is.
# And you have a %s computer. Faggot.
# """ % (likes, lives, computer)
# from sys import argv
# script, filename = argv
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()
#
# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()
# from sys import argv
# script , filename = argv
#
# print "We're going to erase %r." % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit ENTER."
#
# raw_input("?")
#
# print "Opening the file..."
# target = open(filename, 'w')
#
# print "Truncating the file. Goodbye bitch!"
# target.truncate()
#
# print "Now I'm going ot ask you for three lines."
#
# line1 = raw_input("Line 1: ")
# line2 = raw_input("Line 2: ")
# line3 = raw_input("Line 3: ")
#
# print "I'm going to write these to the file now, cunt."
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
#
# print "And finally, we close that shit nigga."
# target.close()
# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print "Copying from %s to %s" % (from_file, to_file)
#
# in_file = open(from_file)
# indata = in_file.read()
#
# print "The input file is %d byes long" % len(indata)
#
# print "Does the output file exist? %r" % exists(to_file)
# print "ready, hit ENTER to continue, CTRL-C to abort."
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "Alright, all done."
#
# out_file.close()
# in_file.close()
# for i in range(0,255):
#     print "Adding %d to the list you slut" % i
#
#
# def looping_this_slut(incoming,jumper):
#     i = 0
#     numbers = []
#     while i < incoming:
#         print "At the top i is %d" % i
#         numbers.append(i)
#
#         i += jumper
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i
#
#     print "The numbers: "
#     for num in numbers:
#         print num
#
#
# input_needed = int(raw_input("Give me a number slut>"))
# second_input = int(raw_input("How many to jump?>"))
# looping_this_slut(input_needed,second_input)
# import os
# wd = os.getcwd()
# print wd
# print os.listdir(wd)
# def answer(x):
#     # your code here
#     if x <= 0  :
#         print("No!")
#     else:
#         for y in range(6):
#             x **= y
#     return x
#
# print answer(3)
# ten_things = "Apples Oranges Crows Telephone Light Sugar"
#
# print "Wait there are not 10 things in that list. Let's fix that."
#
# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#
# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print "Adding: ", next_one
#     stuff.append(next_one)
#     print "There are %d items now." % len(stuff)
#
# print "There we go: ", stuff
#
# print "Let's do some things with stuff."
#
# print stuff[1]
# print stuff[-1] # whoa! fancy
# print stuff.pop()
# print ' '.join(stuff) # what? cool!
# print '#'.join(stuff[3:5]) # super stellar!
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"
