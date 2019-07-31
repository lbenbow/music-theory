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
mode = {'ionian'    :[('w','w','h','w','w','w','h'), 0],
        'dorian'    :[('w','h','w','w','w','h','w'), 1],
        'phrygian'  :[('h','w','w','w','h','w','w'), 2],
        'lydian'    :[('w','w','w','h','w','w','h'), 3],
        'mixolydian':[('w','w','h','w','w','h','w'), 4],
        'aeolian'   :[('w','h','w','w','h','w','w'), 5],
        'locrian'   :[('h','w','w','h','w','w','w'), 6],
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
keyofCSharp = pd.Series(['C#','D#','E#','F#','G#','A#','B#','C#'], (1,2,3,4,5,6,7,8))
keyofGb = pd.Series(('Gb','Ab','Bb','Cb','Db','Eb','F','Gb'), (1,2,3,4,5,6,7,8))
keyofDb = pd.Series(('Db','Eb','F','Gb','Ab','Bb','C','Db'), (1,2,3,4,5,6,7,8))
keyofAb = pd.Series(('Ab','Bb','C','Db','Eb','Fb','Gb','Ab'), (1,2,3,4,5,6,7,8))
keyofEb = pd.Series(('Eb','F','G','Ab','Bb','C','D','Eb'), (1,2,3,4,5,6,7,8))
keyofBb = pd.Series(('Bb','C','D','Eb','F','G','A','Bb'), (1,2,3,4,5,6,7,8))
keyofCb = pd.Series(['Cb','Db','Eb','Fb','Gb','Ab','Bb','Cb'], (1,2,3,4,5,6,7,8))

# Define key signatures dictionary based on 1-indexed series
keySigSeries = {'f': keyofF,'c': keyofC,'g': keyofG,'d': keyofD,'a': keyofA,
                'e': keyofE,'b': keyofB,'c#': keyofCSharp,'gb': keyofGb,'db': keyofDb,
                'ab': keyofAb,'eb': keyofEb,'bb': keyofBb,'cb': keyofCb}

# Define the most common chords for each scape tone
majorChords = pd.Series(('Maj7','min7', 'min7', 'Maj7', '7', 'min7', 'min7b5'), (1,2,3,4,5,6,7))
minorChords = pd.Series(('min7', 'min7b5', 'Maj7','min7', 'min7', 'Maj7', '7'), (1,2,3,4,5,6,7))

def buildProgression(prog_key, prog_tone, prog_array):
# Take key, tonality and numerical sequence to build
# a progression
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
    return kSigSeries[key]

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
#class Key:

