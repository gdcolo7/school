extends Button

func _ready():
	# This "plugs the wire in" via code
	self.pressed.connect(_on_button_pressed)

func _on_button_pressed():
	get_tree().change_scene_to_file("res://menus/gameplay.tscn")
	print("attempted scene change to gameplay")
