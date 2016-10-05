import sys
from pydub import AudioSegment
import random 

class Mashup_Maker():
	def __init__(self):
		self.min_seg_len = 2
		self.max_seg_len = 8
		self.second = 1000
		#TODO MAKE CONSTATS^

		self.songs = []
		for i in range(1, len(sys.argv)):
			song_title  = sys.argv[i]
			self.songs.append(self.open_song(song_title))

		self.get_min_len()



	def open_song(self, file_name):
		s_type = file_name.split(".")[1]
		s = AudioSegment.from_file(file_name, s_type)
		return s

	def get_min_len(self):
		self.min_len = len(self.songs[0])
		self.short_song_index = 0 
		for i in range(len(self.songs)):
			if len(self.songs[i]) < self.min_len:
				self.min_len = len(self.songs[i])
				self.short_song_index = i
		
	def make(self):
		self.pos = 0
		self.mashup = self.get_song_seg(0)
		self.seg_count = 1
		while self.pos < self.min_len:
			print self.seg_count
			curr_song_index = self.seg_count % len(self.songs)
			seg = self.get_song_seg(curr_song_index)
			self.seg_count +=1
			self.mashup = self.mashup.append(seg, crossfade=100) 
		self.mashup.export("mashup.mp3", format="mp3")

	def get_song_seg(self, song_index):
		
		seg_len = random.randint(self.min_seg_len,self.max_seg_len)*self.second
		if self.pos + seg_len > self.min_len:
				seg = self.songs[self.short_song_index][self.pos:]
		else:
			seg = self.songs[song_index][self.pos:self.pos + seg_len]
		self.pos += seg_len
		return seg

if __name__ == '__main__':
	if len(sys.argv) > 1:
		mm = Mashup_Maker()
		mm.make()
