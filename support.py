import numpy as np
import pandas as pd

# Dictionary of Key Singatures
keySig = {'f':['F','G','A','Bb','C','D','E','F'],
          'c':['C','D','E','F','G','A','B','C'],
          'g':('G','A','B','C','D','E','F#','G'),
          'd':('D','E','F#','G','A','B','C#','D'),
          'a':('A','B','C#','D','E','F#','G#','A'),
          'e':('E','F#','G#','A','B','C#','D#','E'),
          'b':('B','C#','D#','E','F#','G#','A#','B'),
          'f#':['F#','G#','A#','B','C#','D#','E#','F#'],
          'c#':['C#','D#','E#','F#','G#','A#','B#','C#'],
          'gb':('Gb','Ab','Bb','Cb','Db','Eb','F','Gb'),
          'db':('Db','Eb','F','Gb','Ab','Bb','C','Db'),
          'ab':('Ab','Bb','C','Db','Eb','Fb','Gb','Ab'),
          'eb':('Eb','F','G','Ab','Bb','C','D','Eb'),
          'bb':('Bb','C','D','Eb','F','G','A','Bb'),
          'cb':['Cb','Db','Eb','Fb','Gb','Ab','Bb','Cb'],
          }

# Dictionary of Mode intervals
mode = {'ionian'    :[('w','w','h','w','w','w','h'), 1],
        'dorian'    :[('w','h','w','w','w','h','w'), 2],
        'phrygian'  :[('h','w','w','w','h','w','w'), 3],
        'lydian'    :[('w','w','w','h','w','w','h'), 4],
        'mixolydian':[('w','w','h','w','w','h','w'), 5],
        'aeolian'   :[('w','h','w','w','h','w','w'), 6],
        'locrian'   :[('h','w','w','h','w','w','w'), 7],
        }


# Create Pandas Series from dictionary
kSigSeries = pd.Series(keySig).sort_index()
modeSeries = pd.Series(mode)

# Define Keys using Pandas Series to provide 1-indexed Scale to match
# music nomenclature
keyofF = pd.Series(('F','G','A','Bb','C','D','E','F'), (1,2,3,4,5,6,7,8))
keyofC = pd.Series(('C','D','E','F','G','A','B','C'), (1,2,3,4,5,6,7,8))
keyofG = pd.Series(('G','A','B','C','D','E','F#','G'), (1,2,3,4,5,6,7,8))
keyofD = pd.Series(('D','E','F#','G','A','B','C#','D'), (1,2,3,4,5,6,7,8))
keyofA = pd.Series(('A','B','C#','D','E','F#','G#','A'), (1,2,3,4,5,6,7,8))
keyofE = pd.Series(('E','F#','G#','A','B','C#','D#','E'), (1,2,3,4,5,6,7,8))
keyofB = pd.Series(('B','C#','D#','E','F#','G#','A#','B'), (1,2,3,4,5,6,7,8))
keyofGb = pd.Series(('Gb','Ab','Bb','Cb','Db','Eb','F','Gb'), (1,2,3,4,5,6,7,8))
keyofDb = pd.Series(('Db','Eb','F','Gb','Ab','Bb','C','Db'), (1,2,3,4,5,6,7,8))
keyofAb = pd.Series(('Ab','Bb','C','Db','Eb','Fb','Gb','Ab'), (1,2,3,4,5,6,7,8))
keyofEb = pd.Series(('Eb','F','G','Ab','Bb','C','D','Eb'), (1,2,3,4,5,6,7,8))
keyofBb = pd.Series(('Bb','C','D','Eb','F','G','A','Bb'), (1,2,3,4,5,6,7,8))

major_diatonic_chords = pd.DataFrame(
    [['FMaj7', 'Gmin7',  'Amin7', 'BbMaj7', 'C7', 'Dmin7', 'Emin7b5'],
    ['CMaj7', 'Dmin7',  'Emin7', 'FMaj7', 'G7', 'Amin7', 'Bmin7b5'],
    ['GMaj7', 'Amin7',  'Bmin7', 'CMaj7', 'D7', 'Emin7', 'Fmin7b5'],
    ['DMaj7', 'Emin7',  'F#min7', 'GMaj7', 'A7', 'Bmin7', 'C#min7b5'],
    ['AMaj7', 'Bmin7',  'C#min7', 'DMaj7', 'E7', 'F#min7', 'F#min7b5'],
    ['EMaj7', 'F#min7',  'G#min7', 'AMaj7', 'B7', 'C#min7', 'D#min7b5'],
    ['BMaj7', 'C#min7',  'D#min7', 'EMaj7', 'F#7', 'G#min7', 'A#min7b5'],
    ['GbMaj7', 'Abmin7',  'Bbmin7', 'CbMaj7', 'Db7', 'Ebmin7', 'Fmin7b5'],
    ['DbMaj7', 'Ebmin7',  'Fmin7', 'GbMaj7', 'Ab7', 'Bbmin7', 'Cmin7b5'],
    ['AbMaj7', 'Bbmin7',  'Cmin7', 'DbMaj7', 'Eb7', 'Fmin7', 'Gmin7b5'],
    ['EbMaj7', 'Fmin7',  'Gmin7', 'AbMaj7', 'Bb7', 'Cmin7', 'Dmin7b5'],
    ['BbMaj7', 'Cmin7',  'Dmin7', 'EbMaj7', 'F7', 'Gmin7', 'Amin7b5'],],
    index=['F','C','G','D', 'A','E', 'B', 'Gb', 'Db', 'Ab', 'Eb','Bb' ],
    columns = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii'])

# Define key signatures dictionary based on 1-indexed series
keySigSeries = {'f': keyofF,'c': keyofC,'g': keyofG,'d': keyofD,'a': keyofA,
                'e': keyofE,'b': keyofB,
                #'c#': keyofCSharp,
                'gb': keyofGb,'db': keyofDb,
                'ab': keyofAb,'eb': keyofEb,'bb': keyofBb}
                #'cb': keyofCb}

# Define the most common chords for each scape tone
majorChords = pd.Series(('Maj7','min7', 'min7', 'Maj7', '7', 'min7', 'min7b5'), (1,2,3,4,5,6,7))
minorChords = pd.Series(('min7', 'min7b5', 'Maj7','min7', 'min7', 'Maj7', '7'), (1,2,3,4,5,6,7))

def buildProgression(prog_key, prog_tone, prog_array):
# Take key, tonality and numerical sequence to build
# a progression
    try:
        _key = prog_key.lower()
        _prog = list(map(int, prog_array))

        _progstr = ''
        for _chord in _prog:
            if prog_tone =='M':
                _progstr += keySigSeries[_key][_chord] + majorChords[_chord] + " "
            else:
                _progstr += keySigSeries[_key][_chord] + minorChords[_chord] + " "
        #print(_progstr)
        return _progstr
    except ValueError:
        print('Please carefully check entries!')
        pass
############# End func buildProgression()

# note1 = str(keySigSeries['c'][1])
# chord1 = str(majorChords[1])

# my_str = note1 + chord1 + " "
# my_str += f"{keySigSeries['c'][4]}{majorChords[4]} "
# my_str += f"{keySigSeries['c'][5]}{majorChords[5]}"
#
# print(my_str)



# Debug
# print(kSigSeries)
#print(kSigSeries[['B','G']])
#print(keySig[('A','C')])

# print(modeSeries[['Ionian','Dorian']])

def getmodefromkey(key, mode):
    _mode = mode
    lower(_mode)
    print(f'Lowered: {_mode}')
    arr = kSigSeries[key]
    pos = modeSeries[mode][1]
    print(arr[:])
    #print(arr[pos:])
    newarr = arr[pos:] + arr[1:pos+1]
    print(newarr)

def getmodefromnote(note,mode):
    _note = note.lower()
    _mode = mode.lower()
    pos = modeSeries[_mode][1]
    print(modeSeries[_mode][1])
    for key in keySig:
        #print(keySig[key][pos])
        if keySig[key][pos] == _note:
            newarr = keySig[key][pos: ] + keySig[key][1:pos+1]
            print(f'Key = {key}: {keySig[key]}')
            print(f'{_note} {_mode} = {newarr}')




#getmodefromnote('G', 'Mixolydian')

# getmodefromkey('C', 'Dorian')
# print()
# getmodefromkey('C', 'Phrygian')
# print()
# getmodefromkey('C', 'Aeolian')
# print()




def getkeysigs():
    return kSigSeries[:]


# sentKeys = []
# keys = []
# sentKeys = input('Enter Key Signature(s): ')
# #sentKeys.
# keys = getkeysigs(sentKeys)
# print(f'Returned key(s) {sentKeys} = ', keys)
# print()

#keysarr = ['A', 'B', 'C']
#getkeysigs(keysarr)

def getkeysig(key):
# Function to retrieve notes for desired Key
#    print('Key = ' + key)
#    for _note in keySig[key]:
#        print(_note + ', ', end='')
#    print('\n')
    key = key.lower()
    return keySig[key]

def getmode(mode):
    _mode = mode.lower()
    return modeSeries[_mode]


def printallkeysig():
    for sig in keySig:
        print('Key = ' + sig)
        for note in keySig[sig]:
            print(note + ', ', end='')
        print('')
    #print(keySig)


class Key:
    """
    Test Doc
    """
    def __init__(self, key):
        self.key = key.lower()   # for calling helper functions we need lower case
        self.name = key
        self.scale = keySigSeries[key.lower()][:].values.tolist()
        self.signature = set([s for s in keySigSeries[key.lower()][:] if '#' in s or 'b' in s])
        self.major_seventh_chords = keySigSeries[key.lower()][:7].values + majorChords.values.tolist()
        self.minor_seventh_chords = keySigSeries[key.lower()][:7].values + minorChords.values.tolist()



    def print_info(self):
        print(f'Key = {self.name}')
        print(f'Signature = {self.signature}')
        print(f'Scale = {self.scale}')
        print(f'Major key seventh chords = {self.major_seventh_chords}')
        print(f'Minor key seventh chords = {self.minor_seventh_chords}')
        # for item in keySigSeries.keys():
        #     print(f"['{keySigSeries[item][1]}{majorChords[1]}', "
        #           f"'{keySigSeries[item][1]}{majorChords[2]}',  "
        #           f"'{keySigSeries[item][1]}{majorChords[3]}', "
        #           f"'{keySigSeries[item][4]}{majorChords[4]}', "
        #           f"'{keySigSeries[item][5]}{majorChords[5]}', "
        #           f"'{keySigSeries[item][1]}{majorChords[6]}', "
        #           f"'{keySigSeries[item][1]}{majorChords[7]}'],")


    def print_scale(self):
        print(self.scale)

    def print_signature(self):
        print(self.signature)

    def build_progression(self, prog=None, tone=None):
        if prog is None:
            prog = [1, 4, 5]
        if tone is None:
            tone = 'M'
        #self.prog = prog
        #
        # progression = majorChords.values[[prog]].tolist() #keySigSeries['a'][prog].values + majorChords.values[prog].tolist()
        # print(f'Progression = {progression}')
        try:
            #_key = prog_key.lower() self.key
            _prog = list(map(int, prog))

            _progstr = ''
            for _chord in _prog:
                if tone == 'M':
                    _progstr += keySigSeries[self.key][_chord] + majorChords[_chord] + " "
                else:
                    _progstr += keySigSeries[self.key][_chord] + minorChords[_chord] + " "
            print(_progstr)
            #return _progstr
        except ValueError:
            print('Please carefully check entries!')
            pass

def print_diatonic_chords(prog, key):
    if prog is None:
        progression = [0,3,4]
    else:
        progression = prog
    if key is None:
        key = 'C'
    else:
        my_key = key
    my_string = ''

    for pos in progression:
        #my_string = "major_diatonic_chords[" + str(pos) + "]"
        #major_diatonic_chords.columns.get_values()[pos]

        my_chord = ''
        if pos == 0:
            my_chord = major_diatonic_chords.I[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 1:
            my_chord = major_diatonic_chords.ii[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 2:
            my_chord = major_diatonic_chords.iii[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 3:
            my_chord = major_diatonic_chords.IV[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 4:
            my_chord = major_diatonic_chords.V[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 5:
            my_chord = major_diatonic_chords.vii[my_key]
            print(f"{my_chord} ", end='')
        elif pos == 6:
            my_chord = major_diatonic_chords.viii[my_key]
            print(f"{my_chord} ", end='')

    print()


    #prog_frame = pd.DataFrame([my_string])
    #print(f'{major_diatonic_chords[{my_string}]}')
    #print(major_diatonic_chords[{my_string}])
    #print(major_diatonic_chords[:2].to_string())

    #def print_key_signature(self):


