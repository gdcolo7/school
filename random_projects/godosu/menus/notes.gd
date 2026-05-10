extends Sprite2D

var hit_time = 5.0 # Note should hit the line exactly 5 seconds into the song
var speed = 4

# We need a reference to the audio player to get the time!
@onready var audio = get_node("../AudioStreamPlayer2D")

func _process(delta):
	var current_time = audio.get_playback_position()
	
	# Assuming your hit line is at Y = 600
	position.y = 600 - ((hit_time - current_time) * speed)
	print("position is", position.y)
