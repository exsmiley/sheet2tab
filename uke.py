notes = {"A": ["A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5"],
	"E": ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5"],
	"C": ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4","A5", "A#5", "B5", "C5"],
	"G4": ["G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5"]}

locs = {"C4": {"C": 0}, "C5": {"A": 3, "C": 12, "E": 8, "G": 5}, "C#4": {"C": 1}, "C#5": {"A": 4, "E": 9, "G": 6},
		"D4": {"C": 2}, "D5": {"A": 5, "E": 10, "G": 7}, "D#4": {"C": 3}, "D#5": {"A": 6, "E": 11, "G": 8},
		"E4": {"C": 4, "E": 0}, "E5": {"A": 7, "E": 12, "G": 9}, "F4": {"C": 5, "E": 1}, "F5": {"A": 8, "G": 10},
		"F#4": {"C": 6, "E": 2}, "F#5": {"A": 9, "G": 11}, "G4": {"C": 7, "E": 3, "G": 0}, "G5": {"A": 10, "G": 12},
		"G#4": {"C": 8, "E": 4, "G": 1}, "G#5": {"A": 11}, "A4": {"C": 9, "E": 5, "G": 2, "A": 0}, "A5": {"A": 12},
		"A#4": {"C": 10, "E": 6, "G": 3, "A": 1}, "B4": {"C": 11, "E": 7, "G": 4, "A": 2}}


gnotes = {"E": ["E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"],
 "A": ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4"], 
 "D": ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5"], 
 "G": ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5"], 
 "B": ["B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5"], 
 "e": ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6"]}

gnum = {1: "e", 2: "B", 3: "G", 4: "D", 5: "A", 6: "E"}


# returns the list of notes that the tab represents
def readTab(tabname):
	tab = open(tabname + ".txt", 'r')
	notes = []
	lines = []
	first = False #says if the e line has been found
	linecount = 1
	for line in tab:
		# adds lines if we have already found the first line
		if first:
			lines.append(line)
			linecount += 1
			# sees if we have all 6 lines
			if linecount == 6:
				# finds the notes in our 6 lines and adds it to our list of notes
				notes += readLines(lines)
				lines = []
				linecount = 1
				first = False
		# trying to find the first line
		else:
			keepatit = True # tells us if we should keep at trying to determine if this is a first line
			i = 0 # index of the character in the line we are looking at
			while keepatit:
				if i == len(line):
					keepatit = False
				elif line[i] == "e":
					lines.append(line)
					first = True
					keepatit = False
				elif line[i] == "-":
					keepatit = False
				i += 1
	tab.close()
	return notes


#reads a set of 6 lines and returns the associated notes
def readLines(lines):
	notes = []
	for i in range(len(lines[0])):
		spot = []
		for j in range(6):
			if i < len(lines[j]) and lines[j][i].isdigit():
				if i+1 < len(lines[j])-1 and lines[j][i+1].isdigit():
					spot.append(gnotes[gnum[j+1]][int(lines[j][i:i+2])])
				elif i-1 >= 0 and lines[j][i-1].isdigit():
					pass# do nothing
				else:
					spot.append(gnotes[gnum[j+1]][int(lines[j][i])])
		if len(spot) > 0:
			notes.append(spot)
	return notes

def usableNote(note):
	if note in locs:
		return note
	if note[0:len(note)-1] + "4" in locs:
		return note[0:len(note)-1] + "4"
	elif note[0:len(note)-1] + "5" in locs:
		return note[0:len(note)-1] + "5"


def noteToTab(note):
	global locs
	try:
		if note in locs:
			return locs[note]
		if note[0:len(note)-1] + "4" in locs:
			return locs[note[0:len(note)-1] + "4"]
		elif note[0:len(note)-1] + "5" in locs:
			return locs[note[0:len(note)-1] + "5"]
	except:
		print note, "That note cannot be played on a guitar"
		return

def firstNote(note, pos="mid"):
	place = ("E", 8)
	if pos == 'top':
		place = ("E", 0)
	elif pos == "bottom":
		place = ("E", 7)
	else:
		place = ("E", 7)
	return nextNote(note, place)

def nextNote(note, prev=None, prev2=None, prev3=None):
	if len(note) == 1:
		note += "4"
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
	tabs = [firstNote(usableNote(notes[0][0]))]
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
	lines = ["A: ", "E: ", "C: ", "G: "]
	for t in tab:
		if type(t) == list:
			nums = [0, 1, 2, 3]
			maxl = 0
			for n in t:
				if n[0] == "A":
					e = 0
				elif n[0] == "E":
					e = 1
				elif n[0] == "C":
					e = 2
				elif n[0] == "G":
					e = 3
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
			if t[0] == "A":
				e = 0
			elif t[0] == "E":
				e = 1
			elif t[0] == "C":
				e = 2
			elif t[0] == "G":
				e = 3
			for i in range(len(lines)):
				if i == e:
					lines[i] += str(t[1]) + "--"
				else:
					for j in range(len(str(t[1]))+2):
						lines[i] += "-"
	#make fit on one line instead of overflowing... need to fix cutoffs
	base = ["A: ", "E: ", "C: ", "G: "]
	eIndex = 0
	nline = 60
	while len(lines[eIndex]) > nline:
		nline = 60
		stop = len(lines)
		basecount = 0
		for i in range(eIndex, stop):
			if i % 4 == 0:
				for j in range(i, i+4):
					if len(lines[j]) > nline:
						while lines[j][nline] != "-":
							nline += 1
			lines.append(base[basecount] + lines[i][nline:])
			lines[i] = lines[i][:nline]
			basecount += 1
		eIndex += 4
		if eIndex + 1 >= len(lines):
			break
	count = 1
	for l in lines:
		if count % 4 == 0:
			l += "\n"
		l += "\n"
		f.write(l)
		count += 1
	f.close()
	print "Successfully made " + name + ".txt"
	return


a = readTab("maiden")

makeTab(tabRaw(a), "maidenuke")