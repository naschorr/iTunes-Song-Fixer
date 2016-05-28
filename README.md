# iTunes-Song-Fixer
Unobfuscates MP3 file names that've been renamed by iTunes

![Example output](https://raw.githubusercontent.com/naschorr/iTunes-Song-Fixer/master/images/example_output.png)

> Some example output taken from songs recovered from an ancient iPod.


Basically, it'll turn that wall of MP3s with four-letter names into a wall of MP3s with names that make sense. It does this via the handy [Mutagen](https://mutagen.readthedocs.io/en/latest/#) module, and gives you a few options for formatting the output. It's important to note that this program only *reads* the tag data, so nothing is permanant.

The `--delete` flag will automatically delete MP3s with broken or nonexistent tags. This usually happens when Mutagen can't load in the ID3 data. Defaults to '--no-delete'.<br />
The `--title-artist` flag changes the renamed files to have the title of the song before the artist. Defaults to `--artist-title`. <br />
The `--title-only` flag sets the renamed files to only have a title. Defaults to '--both'. <br />
The `--min-bitrate` or `-b` option lets you select a required minimum bitrate (in Kbps) for songs. It will delete songs that don't fulfil this. Defaults to 0 Kbps when not specified. <br />
The `--directory` or `-d` option lets you select a different working directory for the program to execute in. Defaults to the current working directory if not specified. Requires a fully qualified pathname if used.
  
Note: This requires [Click](http://click.pocoo.org/5/), and [Mutagen](https://mutagen.readthedocs.io/en/latest/#). You can install them with `pip install -r requirements.txt`.

Another Note: The songs were pulled from a jailbroken iPod running an early version of iOS 3, so no guarantees that this will work on anything else.
