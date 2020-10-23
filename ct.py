import os
c1 = 0
c2 = 0
for dirname, dirnames, filenames in os.walk('TUH_EEG/edf'):
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if filename[-3:] == 'edf':
            c1 += 1
        if filename[-3:] == 'txt':
            c2 += 1

print(c1,c2,c1+c2)
