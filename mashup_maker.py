import sys
from pydub import AudioSegment
import random 

class Mashup_Maker():
	
	def __init__(self):
		self.SECOND = 1000
		self.MIN_SEG_LEN = 2
		self.MAX_SEG_LEN = 8
	
		self.mashup_title = "mashup_"	
		self.songs = []
		for i in range(1, len(sys.argv)):
			song_title  = sys.argv[i]
			self.mashup_title += (song_title.split(".")[0] + "_")
			self.songs.append(self.open_song(song_title))

		self.get_min_len()



	def open_song(self, file_name):
		# Opens the song file using pydub
		s_type = file_name.split(".")[1]
		s = AudioSegment.from_file(file_name, s_type)
		return s

	def get_min_len(self):
		# Finds the song with the minimum length
		self.min_len = len(self.songs[0])
		self.short_song_index = 0 
		for i in range(len(self.songs)):
			if len(self.songs[i]) < self.min_len:
				self.min_len = len(self.songs[i])
				self.short_song_index = i
		
	def mash(self):
		# Mashes random segments from each song
		self.pos = 0
		self.mashup = self.get_song_seg(0)
		self.seg_count = 1
		while self.pos < self.min_len:
			print self.seg_count
			curr_song_index = self.seg_count % len(self.songs)
			seg = self.get_song_seg(curr_song_index)
			self.seg_count +=1
			self.mashup = self.mashup.append(seg, crossfade=100) 
		self.mashup.export(self.mashup_title + ".mp3", format="mp3")

	def get_song_seg(self, song_index):
		# Gets a random segment of the indexed song 
		seg_len = random.randint(self.MIN_SEG_LEN, self.MAX_SEG_LEN)*self.SECOND
		if self.pos + seg_len > self.min_len:
			# If this segment would put us over the end of the shortest song, finish the mashup with that song
			seg = self.songs[self.short_song_index][self.pos:]
		else:
			# Grab a random segment from the song
			seg = self.songs[song_index][self.pos:self.pos + seg_len]
		self.pos += seg_len
		return seg

if __name__ == '__main__':
	if len(sys.argv) > 1:
		mashup_maker = Mashup_Maker()
		mashup_maker.mash()
