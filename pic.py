from PIL import Image
#returns a list with the starting pixel values of the staff, where the
#staff ends, and a list of the transition values for the stave (pixels
#lines and between staves)
def findStave(vals):
	impw = []
	length = 0
	lend = 0
	lookblack = True
	count = 0
	for l in range(len(vals)):
		for w in range(len(vals[0])):
			col = (vals[l][w][0] + vals[l][w][1] + vals[l][w][2])/3.0
			if col < 150 and lookblack:
				length = l
				impw.append(w)
				lookblack = False
			elif col < 150:
				if l != length:
					if len(impw) < 10:
						length = l
						impw = [w]
					elif impw[len(impw)-1] - impw[len(impw)-2] < 7:
						length = l
						impw = [w]
					else:
						break
				else:
					impw.append(w)
	deltas = []
	for i in range(len(impw)-1):
		v = impw[i+1] - impw[i]
		if v not in deltas and v < 55:
			app = True
			for d in deltas:
				if abs(d-v) < 3:
					app = False
					'''saved = d
					deltas.remove(d)
					deltas.append((saved+v)/2.0)'''
			if app:
				deltas.append(v)
	for l in range(length, len(vals)):
		col = (vals[l][impw[0]][0] + vals[l][impw[0]][1] + vals[l][impw[0]][2])/3.0
		if col > 150:
			lend = l
			break
	return [[length, impw[0]], lend, deltas]

def notesOnLine((loc, end, widths)):
	(r,c) = loc
	lw = min(widths)
	stave = max(widths)+5*lw
	notesall = []
	numlines = int((len(vals[0])-c)/stave)
	notes = []
	for n in range(numlines):
		extra = 50
		if n == 0:
			extra = 100
		lines = [int(c+lw*i+n*stave) for i in range(-2, 7)]
		spaces = [int(c+lw/2+lw*i+n*stave) for i in range(-2, 5)]
		check = lines + spaces
		for i in range(len(check)):
			w = check[i]
			for l in range(r+extra, end):
				if isNote((l,w)):
					note = ""
					if i == 0:
						note = "C6"
					if i == 1:
						note = "A5"
					if i == 2:
						note = "F5"
					if i == 3:
						note = "D5"
					if i == 4:
						note = "B4"
					if i == 5:
						note = "G4"
					if i == 6:
						note = "E4"
					if i == 7:
						note = "C4"
					if i == 8:
						note = "A3"
					if i == 9:
						note = "D5"
					if i == 10:
						note = "G5"
					if i == 11:
						note = "E5"
					if i == 12:
						note = "C5"
					if i == 13:
						note = "A4"
					if i == 14:
						note = "F4"
					if i == 15:
						note = "D4"
					if i == 16:
						note = "B3"	
					if len(notes) > 0 and notes[len(notes)-1][0] == note and abs(notes[len(notes)-1][1]- l) < 10:
						pass
					else:
						notes.append([note, l])
		notes = sorted(notes, key=lambda x: x[1])
		notes = [n[0] for n in notes]
		notesall += notes
		notes = []
	return notesall				


#definitely can be improved in the future
def isNote(loc, vals, lw):
	(r,c) = loc
	#for (l,w) in [[r+5,c-5],[r+6,c-2],[r-7,c+1],[r-6,c+4]]:
	for (l,w) in [[int(r+5/12.19*lw),int(c-5/12.19*lw)],[int(r+6/12.19*lw),int(c-2/12.19*lw)],[int(r-7/12.19*lw),int(c+1/12.19*lw)],[int(r-6/12.19*lw),int(c+4/12.19*lw)]]:
		col = (vals[l][w][0] + vals[l][w][1] + vals[l][w][2])/3.0
		if col > 100:
			return False
	return True

#returns a list with the starting pixel values of the staff, where the
#staff ends, and a list of the transition values for the stave (pixels
#lines and between staves)
def findStave2(vals, sw = 0):
	impw = []
	isLine = False
	startL = 0
	startw = 0
	endL = 0
	lineGoing = False
	linecount = 0
	#find stave's first line first
	for w in range(sw, len(vals[0])):
		for l in range(len(vals)):
			col = (vals[l][w][0] + vals[l][w][1] + vals[l][w][2])/3.0
			if col < 130 and not lineGoing:
				startL = l
				startw = w
				lineGoing = True
				linecount += 1
			elif col < 130 and lineGoing:
				linecount += 1
			elif lineGoing and linecount > 50:
				endL = l
				lineGoing = False
				break
			elif linecount > 50:
				break
			else:
				startL = 0
				startw = 0
				linecount = 0
				lineGoing = False
	impw.append([startL, startw])
	linew = [startw]
	for w in range(startw+1, len(vals[0])):
		col = (vals[startL][w][0] + vals[startL][w][1] + vals[startL][w][2])/3.0
		if col < 130:
			linew.append(w)
		if len(linew) > 10:
			break
	deltas = []
	for i in range(len(linew)-1):
		a = linew[i+1]-linew[i]
		if a not in deltas and a>5:
			app = True
			for d in deltas:
				if abs(d-a) < 3:
					app = False
					saved = d
					deltas.remove(d)
					deltas.append((9*saved+a)/10.0)
			if app:
				deltas.append(a)
	impw.append(endL)
	impw.append(deltas)
	print deltas
	return impw

def notesOnLine2((loc, end, widths, vals)):
	(r,c) = loc
	lw = min(widths)
	notes = []
	extra = 70
	lines = [int(c+lw*i) for i in range(-2, 7)]
	spaces = [int(c+lw/2+lw*i) for i in range(-2, 5)]
	check = lines + spaces
	for i in range(len(check)):
		w = check[i]
		for l in range(r+extra, end):
			if isNote((l,w), vals, lw):
				note = ""
				if i == 0:
					note = "C6"
				if i == 1:
					note = "A5"
				if i == 2:
					note = "F5"
				if i == 3:
					note = "D5"
				if i == 4:
					note = "B4"
				if i == 5:
					note = "G4"
				if i == 6:
					note = "E4"
				if i == 7:
					note = "C4"
				if i == 8:
					note = "A3"
				if i == 9:
					note = "D5"
				if i == 10:
					note = "G5"
				if i == 11:
					note = "E5"
				if i == 12:
					note = "C5"
				if i == 13:
					note = "A4"
				if i == 14:
					note = "F4"
				if i == 15:
					note = "D4"
				if i == 16:
					note = "B3"	
				if len(notes) > 0 and notes[len(notes)-1][0] == note and abs(notes[len(notes)-1][1]- l) < 10:
					pass
				else:
					notes.append([note, l])
	notes = sorted(notes, key=lambda x: x[1])
	stuff = []
	stuffi = 0
	i = 0
	while i < len(notes)-1:
		use = notes[i]
		if type(use[0]) == list:
			use = use[len(use)-1]
		elif abs(use[1]-notes[i+1][1]) <=5:
			app = True
			for s in stuff:
				if notes[i][0] == s:
					app = False
			if app:
				stuff.append(notes[i])
			app = True
			for s in stuff:
				if notes[i+1][0] == s:
					app = False
			if app:
				stuff.append(notes[i+1])
			notes.pop(i)
			notes.pop(i)
			notes.insert(i, stuff)
		else:
			stuff = []
		i += 1

	notes = [n[0] if not type(n[0]) == list else [n2[0] for n2 in n] for n in notes]
	for i in range(len(notes)):
		if type(notes[i]) == list:
			noduplicates = []
			for n in notes[i]:
				if n not in noduplicates:
					noduplicates.append(n)
			notes.pop(i)
			notes.insert(i,noduplicates)
	return [notes, spaces[len(spaces)-1]]

def findAllNotes(pic):
	image = Image.open(pic)
	pix = image.load()
	(length,width) = image.size

	vals = []

	for l in range(length):
		row = []
		for w in range(width):
			row.append(pix[l,w])
		vals.append(row)
	allnotes = []
	next = 1
	while next != 0:
		stave = findStave2(vals, next)
		if stave[0][0] != 0:
			print "found a line at (" + str(stave[0][0]) + ", " + str(stave[0][1]) + ")"
			stave += [vals]
			(n, next) = notesOnLine2(stave)
			print len(n)
			print n
			allnotes += n
		else:
			break
	return allnotes

pic = "abc.png"
#print findAllNotes(pic)