#Necessary imports for full functionalities
from traceback import print_tb
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

#Hold the list of songs
songs=[]

#Connect to spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR-CLIENT_ID-HERE",
                                                           client_secret="YOUR-CLIENT_SECRET-HERE"))

#Open Document.txt (converted from docx)
with open("Document.txt", "r") as my_file:

  #Reads each line in Ducument.txt
  for line in my_file:

      #Checks if line is empty
      if line != "":
          
        #Removes "*" at end of line
        replaceVotes = line.replace("*", "")

        #Lets Spotify API a .5 second cooldown
        time.sleep(0.5)

        #searches the Spotify library for song containg "song-artist"
        results = sp.search(q=replaceVotes, limit=1)

        #Gets release date from song and adds it songs[] as "song-artist\t date"
        for track in results['tracks']['items']:
            song = track['name']
            songArgument = str(song)+"\t"+str(results['tracks']['items'][0]['album']['release_date'])
            print(songArgument)
            songs.append(songArgument)

# Create file "songs.txt"
cwd = os.getcwd()
file_name = os.path.join(cwd, "songs.txt")

#open the newly created songs.txt
#if it already exists, it is cleared
txt_file = open(file_name, "w")

#Attempts to write the songs list to the songs.txt file
for s in songs:
    try:
        txt_file.write(str(s)+'\n')
    except:
        print(s + "Error")