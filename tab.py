from random import randint
import pic
from PIL import Image

locs = {"C3": {"E": 8, "A": 3}, "C4": {"E": 20, "A": 15, "D": 10, "G": 5, "B": 1}, "C5": {"G": 17, "B": 13, "e": 8}, "C6": {"e": 20}, "G2": {"E": 3},"G3": {"E": 15, "A": 10, "D": 5, "G": 0}, "G4": {"A": 22, "D": 17, "G": 12,"B": 8, "e": 3}, "G5": {"B": 20, "e": 15}, "D3":{"E": 10, "A": 5, "D": 0},"D4": {"E": 22, "A": 17, "D": 12, "G": 7, "B": 3}, "D5": {"G": 19, "B": 15, "e": 10}, "D6": {"e": 22}, "A2": {"E": 5, "A": 0}, "A3": {"E": 17, "A": 12, "D": 7, "G": 2}, "A4": {"D": 19, "G": 14, "B": 10, "e": 5},"A5": {"B": 22, "e": 17}, "E2": {"E": 0}, "E3": {"E": 12, "A": 7, "D": 2},"E4": {"A": 19, "D": 14, "G": 9, "B": 5, "e": 0}, "E5": {"G": 21, "B": 17, "e": 12},"B2": {"E": 7, "A": 2}, "B3": {"E": 19, "A": 14, "D": 9, "G": 4, "B": 0}, "B4": {"D": 21, "G": 16, "B": 12, "e": 7}, "B5": {"e": 19}, "F#2": {"E": 2}, "Gb2": {"E": 2}, "F#3": {"E": 14, "A": 9, "D": 4}, "Gb3": {"E": 14, "A": 9, "D": 4},"F#4": {"A": 21, "D": 16, "G": 11, "B": 7, "e": 2}, "Gb4": {"A": 21, "D": 16, "G": 11, "B": 7, "e": 2},"F#5": {"B": 19, "e": 14}, "Gb5": {"B": 19, "e": 14}, "C#3": {"E": 9, "A": 4}, "Db3": {"E": 9, "A": 4},"C#4": {"A": 16, "D": 11, "G": 6, "B": 2}, "Db4": {"A": 16, "D": 11, "G": 6, "B": 2},"C#5": {"G": 18, "B": 14, "e": 9}, "Db5": {"G": 18, "B": 14, "e": 9},"C#6": {"e": 21}, "Db6": {"e": 21}, "Ab2": {"E": 4}, "G#2": {"E": 4},"Ab3": {"E": 16, "A": 11, "D": 6, "G": 1}, "G#3": {"E": 16, "A": 11, "D": 6, "G": 1},"Ab4": {"D": 18, "G": 13, "B": 9, "e": 4}, "G#4": {"D": 18, "G": 13, "B": 9, "e": 4},"Ab5": {"B": 21, "e": 16}, "G#5": {"B": 21, "e": 16}, "Eb3": {"E": 11, "A": 6, "D": 1},"D#3": {"E": 11, "A": 6, "D": 1}, "Eb4": {"A": 18, "D": 13, "G": 8, "B": 4},"D#4": {"A": 18, "D": 13, "G": 8, "B": 4}, "Eb5": {"G": 20, "B": 16, "e": 11},"D#5": {"G": 20, "B": 16, "e": 11}, "Bb2": {"E": 6, "A": 1}, "A#2": {"E":6, "A":1},"Bb3": {"E": 18, "A": 13, "D": 8, "G": 3}, "A#3": {"E": 18, "A": 13, "D": 8, "G": 3},"Bb4": {"D": 20, "G": 15, "B": 11, "e": 6}, "A#4": {"D": 20, "G": 15, "B": 11, "e": 6},"Bb5": {"e": 18}, "A#5": {"e": 18}, "F2": {"E": 1}, "F3": {"E": 13, "A": 8, "D": 3},"F4": {"A": 20, "D": 15, "G": 10, "B": 6, "e": 1}, "F5": {"G": 22, "B": 17, "e": 13}}

notes = {"E": ["E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"],
 "A": ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4"], 
 "D": ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5"], 
 "G": ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5"], 
 "B": ["B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5"], 
 "e": ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6"]}

#returns a dictionary of the possible locations on a guitar that the note is
#ie. noteToTab("C4") returns {'A': 15, 'B': 1, 'E': 20, 'D': 10, 'G': 5}
def noteToTab(note):
	global locs
	try:
		return locs[note]
	except:
		print "That note cannot be played on a guitar"
		return

def firstNote(note, pos="mid"):
	place = ("E", 8)
	if pos == 'top':
		place = ("E", 0)
	elif pos == "bottom":
		place = ("E", 15)
	else:
		place = ("E", 8)
	return nextNote(note, place)

def nextNote(note, prev=None, prev2=None, prev3=None):
	if len(note) == 1:
		note += "3"
	try:
		tab = noteToTab(note)
		(stringOld, fretOld) = prev
		if prev2:
			(sOld2, fOld2) = prev2
		if prev3:
			(sOld3, fOld3) = prev3
		possible = [] #(str, fret, cost)
		for s in tab.keys():
			possible.append([s, tab[s], 0])
		next = ("str", "fret")
		cost = 1000#cost will never be as high as 1000
		for p in possible:
			#test1: Same String
			if p[0] != stringOld:
				p[2] += 1
			#test2: Fret difference
			p[2] += abs(fretOld - p[1])
			if prev2:
				p[2] += abs(fOld2 - p[1])
			if prev3:
				p[2] += abs(fOld3 - p[1])
			if p[2] < cost:
				next = (p[0], p[1])
				cost = p[2]
		return next
	except:
		return

#notes is a list of notes
def tabRaw(notes):
	tabs = [firstNote(notes[0])]
	count = 0
	first = True
	for n in notes:
		if not first:#n != notes[0]:
			prev = tabs[count]
			prev2 = None
			prev3 = None
			if count >= 1:
				prev2 = tabs[count-1]
			if count >= 2:
				prev3 = tabs[count-2]
			if type(prev) == list:
				prev = prev[0]
			if type(prev2) == list:
				prev2 = prev2[0]
			if type(prev3) == list:
				prev3 = prev3[0]
			if type(n) == list:
				t = []
				for n2 in n:
					t.append(nextNote(n2, prev))
				tabs.append(t)
			else:
				tabs.append(nextNote(n, prev, prev2, prev3))
			count += 1
		else:
			first = False
	return tabs

#max for a line should be 130
def makeTab(tab, name="NewTab"):
	f = open(name + ".txt", 'w')
	lines = ["e: ", "B: ", "G: ", "D: ", "A: ", "E: "]
	for t in tab:
		if type(t) == list:
			nums = [0, 1, 2, 3, 4, 5]
			maxl = 0
			for n in t:
				if n[0] == "E":
					e = 5
				elif n[0] == "A":
					e = 4
				elif n[0] == "D":
					e = 3
				elif n[0] == "G":
					e = 2
				elif n[0] == "B":
					e = 1
				elif n[0] == "e":
					e = 0
				nums[e] = [e, n[1]]
				if len(str(n[1])) > maxl:
					maxl - len(str(n[1]))
			for i in nums:
				if type(i) == list:
					lines[i[0]] += str(i[1])
					for j in range(maxl-len(str(i[1]))+3):
						lines[i[0]] += "-"
				else:
					for j in range(maxl+3):
						lines[i] += "-"
		else:
			if t[0] == "E":
				e = 5
			elif t[0] == "A":
				e = 4
			elif t[0] == "D":
				e = 3
			elif t[0] == "G":
				e = 2
			elif t[0] == "B":
				e = 1
			elif t[0] == "e":
				e = 0
			for i in range(len(lines)):
				if i == e:
					lines[i] += str(t[1]) + "--"
				else:
					for j in range(len(str(t[1]))+2):
						lines[i] += "-"
	#make fit on one line instead of overflowing... need to fix cutoffs
	base = ["e: ", "B: ", "G: ", "D: ", "A: ", "E: "]
	eIndex = 0
	nline = 60
	while len(lines[eIndex]) > nline:
		nline = 60
		stop = len(lines)
		basecount = 0
		for i in range(eIndex, stop):
			if i % 6 == 0:
				for j in range(i, i+6):
					if len(lines[j]) > nline:
						while lines[j][nline] != "-":
							nline += 1
			lines.append(base[basecount] + lines[i][nline:])
			lines[i] = lines[i][:nline]
			basecount += 1
		eIndex += 6
		if eIndex + 1 >= len(lines):
			break
	count = 1
	for l in lines:
		if count % 6 == 0:
			l += "\n"
		l += "\n"
		f.write(l)
		count += 1
	f.close()
	return

cscale = ["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

def randomInC():
	cscale = ["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
	song = []
	count = 0
	current = randint(0, len(cscale)-1)
	while count < 50:
		top = current+2
		bottom = current-2
		if top >= len(cscale):
			top = len(cscale)-1
		if bottom < 0:
			bottom = 0
		current = randint(bottom, top)
		song.append(cscale[current])
		count += 1
	return makeTab(tabRaw(song), "Random in C")

def inputTab():
	try:
		global locs
		n = raw_input("What do you want to name your tab? ")
		tlist = []
		t = raw_input("Enter a note and press enter after each one\nType 'stop' to stop it: ")
		while t.lower() != 'stop':
			if t.upper() in locs.keys():
				tlist.append(t.upper())
			else:
				print "Previous note cannot be played on guitar."
			t = raw_input("Next note: ")
		makeTab(tabRaw(tlist), n)
		print "Tab made called " + n
		return True
	except:
		return False

#t = tabRaw(cscale)
#makeTab(t, "C Scale")
#randomInC()
def getVals(pic):
	image = Image.open(pic)
	pix = image.load()
	(length,width) = image.size

	vals = []

	for l in range(length):
		row = []
		for w in range(width):
			row.append(pix[l,w])
		vals.append(row)
	return vals

picName = "abc.png"
#makeTab(tabRaw(pic.notesOnLine(pic.findStave(getVals(picName)))), picName)
randomInC()
#makeTab(tabRaw(pic.findAllNotes(picName)), picName)