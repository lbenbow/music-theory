import sys
import support

enter_key = 'Gb'

my_key = support.Key(enter_key)
# my_key.print_scale()
# my_key.print_signature()
# print(my_key.major_seventh_chords)
# print(my_key.minor_seventh_chords)
print()
print()

print(my_key.print_info())
my_key.build_progression()

support.print_diatonic_chords(key='A', prog=[0,2,4 ])

exit(0)
