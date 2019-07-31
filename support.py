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

