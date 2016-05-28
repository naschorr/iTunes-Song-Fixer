# iTunes-Song-Fixer
Unobfuscates MP3 file names that've been renamed by iTunes

![Example output](https://raw.githubusercontent.com/naschorr/iTunes-Song-Fixer/master/images/example_output.png)

> Some example output taken from an ancient iPod.


Basically, it'll turn that wall of MP3s with four-letter names into a wall of MP3s with names that make sense. It does this via the handy [Mutagen](https://mutagen.readthedocs.io/en/latest/#) module, and gives you a few options for formatting the output. It's important to note that this program only reads the tag data, so nothing is permanant.

The `--delete` flag will automatically delete MP3s with broken or nonexistent tags. This usually happens when Mutagen can't load in the ID3 data. <br />
The `--title-artist` flag changes the renamed files to have the title of the song before the artist, instead of the other way around (`--artist-title`) by default. <br />
The `--title-only` flag sets the renamed files to only have a title.
  
Note: This requires [Click](http://click.pocoo.org/5/), and [Mutagen](https://mutagen.readthedocs.io/en/latest/#). You can install them with `pip install -r requirements.txt`. It also *requires* that you put the SongFixer.py program into the directory that contains all of the songs to be fixed.

Another Note: The songs were pulled from a jailbroken iPod running an early version of iOS 3, so no guarantees that this will work on anything later.
