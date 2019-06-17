"""
This code was made by https://github.com/TheMasterMech
You may use any part of this code, but please link my github, cheers!:)
"""
#HELLO! 
#PLEASE GET AN API KEY FROM YOUR PROFILE ON DANBOORU! (danbooru.donmai.us)
#enter them below

#--USER          --
#--     VARIABLES--

DanbooruUsername = "USERNAME HERE"
DanbooruAPIKey = "API KEY HERE"

tagList = "astolfo_(fate) rating:s" #put up to a maximum of two tags!
#-Tag tutorial-
#-Ratings-
#To get SFW images, put "rating:s" (safe) as a tag
#To get suggestive images, put "rating:q" (questionable) as a tag
#To get NSFW images, put "rating:e" (explicit) as a tag.
#-Character names-
#Characters go surname_firstname_(seriesname), (e.g: "astolfo_(fate)")
#The seriesname isn't always needed (e.g: "kanzaki_hideri")
#-Series-
#just put the series name in, lol

saveLocation = "Path to location. Please read the text below, DM me if it's confusing :)"
#put your path to where the folder
#is located, but wherever you would put a '\' or '/', put two! (e.g "E:\Folder\Images\\" -> "E:\\Folder\\Images\\")
#!!REMEMBER TO PUT "\\" AT THE END (e.g -> E:\\Folder\\Images\\"), or all hell breaks loose im not joking!!

amountOfImages = int(50)
#Change this number to however many images you want
#Don't set it too high or it explodes into a shower of code

#--END                  --
#--    OF               --
#--       USER          --
#--            VARIABLES--
#DO NOT TOUCH ANYTHING BELOW THIS LINE

from random import randint #random numbers
import urllib.request #needed to get link contents
import os

try:
    from pybooru import Danbooru #the library that makes it work
except:
    print("Missing module (pybooru), installing now.") #use pip module to install modules
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'pybooru']) # install pybooru
    from pybooru import Danbooru
try:
    import requests #simple web requesting
except:
    print("Missing module (requests), installing now.")
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'requests']) # install requests
    import requests

client = Danbooru('danbooru', username=DanbooruUsername, api_key=DanbooruAPIKey)
links = [] #create link list
fileNumber = int(000000000) #i doubt you'll need more space than this

showMoreInfo = False #change to true if you need to find errors

bannedExtensions = ["zip","swf","ebm"] #put problematic extensions here

posts = client.post_list(tags=tagList, limit=amountOfImages) #get list of posts
ending = saveLocation[-1]
if ending == "\\":
    pass #good file path
else:
    print("Please add two slashes to the end of your save location!")
    os._exit(0)
    
for post in posts:
    try:
        links.append(post["file_url"]) #get tally of links
        if showMoreInfo == True: #debug info
            print("Image path: {0}".format(post['file_url'])) 
    except:
        continue

for link in links:
    if showMoreInfo == True:
        print(link) #debug info
    fileNumber += 1 #add one to tally
    extension = link[-3:] #get the extension
    if extension in bannedExtensions: #skip files with bad extensions
        pass #we don't want that it's bad
    else:
        try:
            with open(saveLocation+str(fileNumber)+"."+extension, "wb") as f:
                #make an empty file with extension, then fill it with data
                f.write(requests.get(link).content)
        except FileNotFoundError: #user didn't give a valid folder
            print(saveLocation)
            print("This folder does not exist! Please create it!")
            break

if links == []:
    print("No results were found, try changing the tags.")
else:
    print("Done!")
    print("Files are located in {0}.".format(saveLocation))