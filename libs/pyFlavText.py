import random

# 63 verbs so far
verbRoots = ["Build", "Calibrat", "Sett", "Link",
						"Read", "Configur", "Link", "Hack",
						"Load", "Assembl", "Wrangl", "Align",
						"Compil", "Engag", "Fabricat", "Decrypt",
						"Encrypt", "Insert", "Cod", "Send",
						"Disconnect", "Salvag", "Delet", "Encrypt",
						"Connect", "Plugg", "Boot", "Start",
						"Comput", "Send", "Receiv", "Transmitt",
						"Wir", "3D Print", "Scann", "Remov",
						"Add", "Warp", "Construct", "Zapp",
						"Fus", "Initialis", "Initiat", "Re-initiat",
						"Explod", "Form", "Detonat", "Solder",
						"Suspend", "Packag", "Simulat", "Plann",
						"Tun", "Eat", "Steer", "Writ", "Download",
						"Hid", "Multiply", "Polish", "Revv",
						"Over-Clock", "Hijack", "Randomis", "[REDACTED]-"
						]

# 53 nouns so far
nouns = ["data", "signal", "Teensy", "Arduino",
				"circuits", "packets", "protocol", "bits",
				"sensors", "bugs", "wires", "registers",
				"cores", "resistors", "capacitors", "[REDACTED]",
				"the Matrix", "vectors", "AI", "Raspberry Pi",
				"electrons", "photons", "waveforms", "algorithms",
				"numbers", "variables", "settings", "nothing.",
				"things", "stuff", "everything", "disks",
				"drives", "kilobytes", "megabytes", "gigabytes",
				"motors", "servos", "robots", "automatons",
				"androids", "DVDs", "PCBs", "frequencies",
				"notes", "RAM", "cameras", "lenses",
				"controllers", "LEDs", "connectors", "interfaces",
				"cables", "dependencies", "lies", ""
				]

def testingLOL():
		selectVerb = random.choice(verbRoots) + "ing"
		selectNoun = random.choice(nouns)
		output = selectVerb+" "+selectNoun
		print(output)
		return output