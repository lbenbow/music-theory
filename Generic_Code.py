# Music Theory based application for learning Pythom
# Larry Benbow
# 20190731
########################################

import sys
import support

## Adding Text to test git

# control = 0
# while control != 1:
#
#
#     print('Choose a Musical Progression to build!\n')
#     prog_key = input("Enter Key: ")
#     prog_tone = input("Major or Minor (M or m): ")
#     prog_array = input("Enter Progression (numerals separated by commas): ").split(',')
#
#     prog = support.buildProgression(prog_key, prog_tone, prog_array)
#     print(prog)
#     print('\n')
#     control = input('Choose to stay (0) or to exit(1): ')
#     control = int(control)
#
#     if control == 1:
#         print('Bye!')
#         break

# exit(0)

sentKey = input('Enter Key Signature: ')
print(sentKey)
#exit(0)
key = support.getkeysig(sentKey)
print(f'Returned key {sentKey} = ', key)

print(f'Key = {key}')
exit(0)

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





