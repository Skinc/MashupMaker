# MashupMaker
Software to make only the best of audio mashups (aka randomly create mashups)

This incredibly complex algorithm uses a random number generator to create random mashups of songs. If it isn't clear, this is a joke and took 30 minutes. Don't judge. 

To run, download pydub http://pydub.com/ by running `pip install pydub`

`python mashup_maker.py song1.mp3 song2.mp3`

I have had no issues using mp3's and it should theoretically handle other file formats.  

The resulting mashup will be as long as the shortest song. It can handle any number of songs as long as the shortest song isn't shorter than approximately 4 seconds multipled by the number of songs.  