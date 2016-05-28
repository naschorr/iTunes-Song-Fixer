import click
import os
import sys

from re import sub
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3._util import ID3NoHeaderError, error

## Returns true if the supplied file is an MP3
def isMP3(fileName):
	name, extension = os.path.splitext(fileName)
	if(".mp3" in extension.lower()):
		return True
	return False

## Get MP3s in given directory
def getMP3s(directory):
	return [os.path.join(directory, fileName) for fileName in os.listdir(directory) if os.path.isfile(os.path.join(directory, fileName)) and isMP3(fileName)]

## Removes special characters from the string
def sanitizeString(string):
	return sub(r'[?|$|.|!|/|\\]',r'', string)

<<<<<<< HEAD
## Alerts the user that a song is being removed, and then deletes it.
def deleteSong(song, explanation=None):
	output = "Deleting " + song + ". "
	if(explanation is not None):
		output += "(" + explanation + ")"
	print(output)
=======
## Deletes a given song
def deleteSong(song):
	print("Deleting " + song)
>>>>>>> origin/master
	os.remove(song)

## Gets the last part of a path (eg. /dir1/dir2/test returns test)
def getPathEnd(path):
	return os.path.basename(os.path.normpath(path))

@click.command()
@click.option('--delete/--no-delete', default=False, help='Deletes MP3s with malformed tag sets. (eg. No title)')
@click.option('--title-artist/--artist-title', default=False, help='Choose whether to put the artist or title first in the new name.')
@click.option('--title-only/--both', default=False, help='Choose whether to keep only the song title or both the artist and title.')
@click.option('--min-bitrate', '-b', default=0, help='Specifies a minimum bitrate that all songs must have, else they get deleted.')
@click.option('--directory', '-d', default=os.getcwd(), type=click.Path(exists=True), help='Specifies a directory for the program to execute in. Requires a fully qualified pathname.')
def main(delete, title_artist, title_only, min_bitrate, directory):
	songs = getMP3s(directory)
	for song in songs:
		try:
			loaded = EasyID3(song)
			if("title" in loaded and "artist" in loaded):
				bitrate = MP3(song).info.bitrate / 1000
				if(min_bitrate >= bitrate):		## Ensure minimum bitrate is reached
					deleteSong(song, "Bitrate below: " + str(min_bitrate))
					continue

				title = sanitizeString(str(loaded["title"][0]))
				renamed = ['','', '', '.mp3']	## Since we're only dealing with mp3s at the moment.

				if(not title_only):				## Thus, we'll have the title and the artist somewhere.
					renamed[1] = ' - '

<<<<<<< HEAD
				if(not title_artist): 			## Thus, the artist string comes first
					renamed[0] = sanitizeString(str(loaded["artist"][0])) * (not title_only)
					renamed[2] = title
				else:							## Thus, the title string comes first
=======
				if(not title_artist): 		## Thus, the artist string comes first
					renamed[0] = sanitizeString(str(loaded["artist"][0])) * (not title_only)
					renamed[2] = title
				else:				## Thus, the title string comes first
>>>>>>> origin/master
					renamed[0] = title
					renamed[2] = sanitizeString(str(loaded["artist"][0])) * (not title_only)

				renamed = os.path.join(directory, ''.join(renamed))

				os.rename(song, renamed)
				print(getPathEnd(song) + " ==> " + getPathEnd(renamed))

		except ID3NoHeaderError:
			if(delete):
				deleteSong(song, "ID3NoHeaderError exception")
			continue
		except error:
			if(delete):
				deleteSong(song, "MutagenError exception")
			continue
		except:
			exception = sys.exc_info()[0].__name__
			print(exception + " exception for song: " + song)

main()
