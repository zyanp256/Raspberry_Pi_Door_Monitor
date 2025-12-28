# RPI-Door-Project
A Raspberry Pi–based door monitoring system that detects door open/close events using a magnetic reed switch and sends real-time notifications via Discord.

What it Does
	•	Detects when a door is opened or closed
	
	•	Sends Discord webhook notifications on state changes
	•	Prevents notification spam using a cooldown system
	•	Sends a warning notification if the door is left open too long
	•	Runs fully on the Raspberry Pi (no laptop required after launch)

Hardware
	•	Raspberry Pi Zero 2 W
	
	•	Magnetic reed switch
	•	GPIO wiring

Software / Tools
	•	Python 3
	
	•	gpiozero (GPIO handling)
	•	requests (Discord webhook)
	•	Threading for background checks
	•	SSH + VS Code Remote for development
