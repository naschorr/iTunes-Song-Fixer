import click
import os
from re import sub
from mutagen.easyid3 import EasyID3
from mutagen.id3._util import ID3NoHeaderError, error

## Returns true if the supplied file is an MP3
def isMP3(fileName):
	name, extension = os.path.splitext(fileName)
	if(".mp3" in extension.lower()):
		return True
	return False

## Get MP3s in current directory
def getMP3s():
	return [fileName for fileName in os.listdir() if os.path.isfile(fileName) and isMP3(fileName)]

## Removes special characters from the string
def sanitizeString(string):
	return sub(r'[?|$|.|!|/|\\]',r'', string)

def deleteSong(song):
	print("Deleting " + song)
	os.remove(song)

@click.command()
@click.option('--delete/--no-delete', default=False, help='Deletes MP3s with malformed tag sets. (eg. No title)')
@click.option('--title-artist/--artist-title', default=False, help='Choose whether to put the artist or title first in the new name.')
@click.option('--title-only/--both', default=False, help='Choose whether to keep only the song title or both the artist and title.')
def main(delete, title_artist, title_only):
	songs = getMP3s()
	for song in songs:
		try:
			loaded = EasyID3(song)
			if("title" in loaded and "artist" in loaded):
				title = sanitizeString(str(loaded["title"][0]))
				renamed = ['','', '', '.mp3']	## Since we're only dealing with mp3s at the moment.

				if(not title_only):		## Thus, we'll have the title and the artist somewhere.
					renamed[1] = ' - '

				if(not title_artist): 	## Thus, the artist string comes first
					renamed[0] = sanitizeString(str(loaded["artist"][0])) * (not title_only)
					renamed[2] = title
				else:					## Thus, the title string comes first
					renamed[0] = title
					renamed[2] = sanitizeString(str(loaded["artist"][0])) * (not title_only)

				renamed = ''.join(renamed)

				os.rename(song, renamed)
				print(song + " ==> " + renamed)

		except ID3NoHeaderError:
			print("ID3NoHeaderError exception for song: " + song)
			if(delete):
				deleteSong(song)
		except error:
			print("Mutagen Error exepction for song: " + song)
			if(delete):
				deleteSong(song)
		except FileExistsError:
			print("FileExistsError exception for song: " + song)

main()