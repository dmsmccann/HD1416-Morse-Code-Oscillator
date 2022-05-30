from pcbnew import *

class SimplePlugin(ActionPlugin):
	def defaults(self):
		self.name = "Thick VCC Tracks"
		self.category = "Track adjustments"
		self.description = "Script to change all tracks in a net"

	def Run(self):

board = GetBoard()

for track in board.GetTracks():
	if track.GetNetname() == "VCC":
		track.SetWidth(FromMM(1))

SiplePlugin().register()