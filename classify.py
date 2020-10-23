#class 1 = Keppra
#class 2 = Dilantin
#class 3 = No medication

from operator import contains

def searchMedication(file):
    with open(file) as openfile:
        for line in openfile:
            if contains(line,'Keppra') or contains(line,'levetiracetam') or contains(line,'keppra') or contains(line,'Levetiracetam') or contains(line,'KEPPRA') or contains(line,'LEVETIRACETUM'):
                return 1
            if contains(line,'DILANTIN') or contains(line,'phenytoin') or contains(line,'Dilantin') or contains(line,'Phenytoin') or contains(line,'dilantin') or contains(line,'phenytoin'):
                return 2
        return 3
import os
for dirname, dirnames, filenames in os.walk('TUH_EEG/edf'):
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if filename[-3:] == 'txt':
            if searchMedication(filepath) == 1:
                print('Keppra is found')
            if searchMedication(filepath) == 2:
                print('Dilantin is found')
            if searchMedication(filepath) == 3:
                print('No medication found')