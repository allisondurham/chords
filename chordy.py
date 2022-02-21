sounds = ["C", "C#/Db", "D","D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
place = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7]
major = [True, False, True, False, True, True, False, True, False, True, False, True]
minor = [True, False, True, True, False, True, False, True, True, False, True, False]
major_pentatonic = [True, False, True, False, True, False, False, True, False, True, False, False]
minor_pentatonic = [True, False, False, True, False, True, False, True, False, False, True, False]
mutations = ["m", 5, "5", 6, "6", 7, "7", "maj7", 9, "9", "maj9", "dim", "dim7", "aug", "+", "aug7", "+7", "aug9","+9", "sus", "sus4", "sus2", "sus9"]
# notes = []
print(len(mutations))

def key(starting_note):
    start = sounds.index(starting_note)
    shifted_notes = []
    for n in range(start,len(sounds)):
        shifted_notes.append(n)
    for n in range(len(sounds)):
        if n < start:
            shifted_notes.append(n)
    notes = []
    for i in shifted_notes:
        notes.append(sounds[i])
    # print(start, shifted_notes, notes)
    return start, shifted_notes, notes

# print(key("G"))


def find_scale(starting_note, scale):          # major 1, 2,   3, 4, 5,   6,   7
    key_info = key(starting_note)              # minor 1, 2, 2.5, 4, 5, 5.5, 6.5
    is_true = scale
    notes = key_info[2]
    requested_scale = []
    for j in range(len(is_true)):
        if is_true[j] == True:
            requested_scale.append(notes[j])
    return requested_scale

print(find_scale("G", major))

def find_relative(starting_note):
    if starting_note.find("m") > -1:
        starting_note = starting_note.strip("m")
        key_info = key(starting_note)
        notes = key_info[2]
        relative = notes[3]
        return relative
    else:
        key_info = key(starting_note)
        notes = key_info[2]
        relative = str(notes[9] + "m")
        return relative

# print(find_relative("Dm"))



def chord(starting_note, scale, mutation=""):
    key_info = key(starting_note)
    notes = key_info[2]
    scale_info = find_scale(starting_note, scale)
    # print("notes     ", notes)
    # print("scale", scale)
    # print("scale_info", scale_info)                     # scale 1, 2, 3, 4, 5, 6, 7
    chord = []
    chord.append(scale_info[0])
    chord.append(scale_info[2])
    chord.append(scale_info[4])                         # major 1, 3, 5
    if mutation != "":
        if mutation == "m":                             # minor 1, 2.5, 5
            if scale == "minor":
                pass
            else:
                chord[1] = notes[3]
        if mutation == "5" or mutation == 5:            # 1, 5
            chord.pop(1)
        elif mutation == "6" or mutation == 6:          # 1, 3, 5, 6
            chord.append(scale_info[5])
        elif mutation == "7" or mutation == 7:          # 1, 3, 5, 6.5
            chord.append(notes[10])
        elif mutation == "maj7":                        # 1, 3, 5, 7
            chord.append(notes[11])
        elif mutation == "9" or mutation == 9:          # 1, 3, 5, 6.5, 9or2
            chord.append(notes[10])
            chord.append(notes[2])
        elif mutation == "maj9":                        # 1, 3, 5, 7, 9or2
            chord.append(notes[10])
            chord.append(notes[3])
        elif mutation == "dim":                         # 1, 2.5, 4.5
            chord[1] = notes[3]
            chord[2] = notes[6]
        elif mutation == "dim7":                        # 1, 2.5, 4.5, 6.5
            chord[1] = notes[3]
            chord[2] = notes[6]
            chord.append(notes[9])
        elif mutation == "aug" or mutation == "+":      # 1, 3, 5.5
            chord[2] = notes[8]
        elif mutation == "aug7" or mutation == "+7":    # 1, 3, 5.5, 6.5
            chord[2] = notes[8]
            chord.append(notes[10])
        elif mutation == "aug9" or mutation == "+9":    # 1, 3, 5.5, 6.5, 9or2
            chord[2] = notes[8]
            chord.append(notes[10])
            chord.append(notes[2])
        elif mutation == "sus" or mutation == "sus4":   # 1, 4, 5
            chord[1] = notes[5]
        elif mutation == "sus2" or mutation == "sus9":  # 1, 2, 5
            chord[1] == notes[2]
        
    print("name      ", starting_note) 
    print("chord     ", chord)
    return chord

# chord("G", major)
# chord("C", major, "")
# chord("C", minor)
# chord("E", minor)
# chord("C", major, "6")

# print(scale("G", major))

def chords_in_key(starting_note):
    if starting_note.find("m") > 0:
        m = True
        starting_note = starting_note.strip("m")
        key_info = key(starting_note)
        notes = key_info[2]
        chords = []
        print(notes)
        if m == True:
            chords.append(notes[0] + "m")
            chords.append(notes[2] + "dim")
            chords.append(notes[3])
            chords.append(notes[5] + "m")
            chords.append(notes[7] + "m")
            chords.append(notes[8])
            chords.append(notes[10])
        else:
            chords.append(notes[0])
            chords.append(notes[2] + "m")
            chords.append(notes[4] + "m")
            chords.append(notes[5])
            chords.append(notes[7])
            chords.append(notes[9] + "m")
            chords.append(notes[11] + "dim")
        print(chords)
        return chords

# print(chords_in_key("D#/Ebm"))

def transpose(sequence, new_starting_chord):
    starting_chord = sequence[0]
    if starting_chord.find("m") > 0:
        m = True
        starting_note = starting_chord.strip("m")
        old_info = key(starting_note)
        old = old_info[2]
        new_info = key(new_starting_chord)
        new = new_info[2]
    else:
        old_info = key(starting_chord)
        old = old_info[2]
        new_info = key(new_starting_chord)
        new = new_info[2]
    print(old)
    print(new)
    print(sequence)

progression = ["G", "Em", "C", "D"]

transpose(progression, "C")



def clean_input(input):
    for j in sounds:
        if input == j:
            cleaned_input = input
            detail = []
            return cleaned_input, detail
        else:
            pass
    z = list(input)
    if z[1] == "#" and z[2] == "/" and z[4] == "b":
        if range(len(z)) == 5:
            cleaned_input = "".join(z)
        else:
            detail = []
            for g in z:
                if z.index(g) > 4:
                    detail.append(g)
                    z.remove(g)
            print("else", detail)
            print("else", z)

            
print(clean_input("G#/Abm"))