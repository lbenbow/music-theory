import sys
import support

## Adding Text to test git

sentKey = input('Enter Key Signature: ')
print(sentKey)
#exit(0)
key = support.getkeysig(sentKey)
print(f'Returned key {sentKey} = ', key)
print()
print()
sentMode = input('Enter Mode: ')
mode = support.getmode(sentMode)
print(f'Returned mode {sentMode} = ', mode[0])
# support.printallkeysig()
#print(allKeys)[

sentKeys = []
# keys = []
# sentKeys = input('Enter Key Signature(s): ')
# keys = \

keys = support.getkeysigs()
print(f'Returned key(s) \n {keys} = ')
print()



exit()

print('Key Signatures')
for sig in keySig:
    print('Key = ' + sig)
    for note in keySig[sig]:
        print(note + ', ', end = '')
    print('')

key_list = []
for key in keySig.keys():
    key_list.append(key)

print('Seventh chords')
for i in key_list:
    cnt = 1
    print(i, ": ", end = '')
    for j in keySig[i]:
        #print(cnt, end = '')
        if cnt % 2:
            print(j + ', ', end = '' )
        cnt = cnt +1
        #    print(cnt, end = '')
    print()
    cnt = 0





