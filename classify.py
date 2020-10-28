#class 1 = Keppra
#class 2 = Dilantin
#class 3 = No medication

from operator import contains
import os
import shutil

def searchMedication(file):
    with open(file) as openfile:
        for line in openfile:
            if contains(line,'Keppra') or contains(line,'levetiracetam') or contains(line,'keppra') or contains(line,'Levetiracetam') or contains(line,'KEPPRA') or contains(line,'LEVETIRACETUM'):
                return 1
            if contains(line,'DILANTIN') or contains(line,'phenytoin') or contains(line,'Dilantin') or contains(line,'Phenytoin') or contains(line,'dilantin') or contains(line,'phenytoin'):
                return 2
        return 3

class_1 = 'class_1/'
c1 = 0
class_2 = 'class_2/'
c2 = 0
class_3 = 'class_3/'
c3 = 0

total = 1838
for dirname, dirnames, filenames in os.walk('TUH_EEG/edf'):
    edfs = []
    names = []
    report = None

    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if filename[-3:] == 'edf':
            edfs.append(filepath)
            names.append(filename)
        elif filename[-3:] == 'txt':
            report = filepath

    if report:
        if searchMedication(report) == 1:
            
            for i in range(len(edfs)):
                # print(edfs[i],names[i],1)
                # c1 += 1
                dest = shutil.copyfile(edfs[i],class_1+names[i])
                total -= 1
                print(total)
                
        if searchMedication(report) == 2:
            
            for i in range(len(edfs)):
                # print(edfs[i],names[i],2)
                # # c2 += 1
                dest = shutil.copyfile(edfs[i],class_2+names[i])
                total -= 1
                print(total)

        if searchMedication(report) == 3:
            
            for i in range(len(edfs)):
                # print(edfs[i],names[i],3)
                # # c3 += 1
                dest = shutil.copyfile(edfs[i],class_3+names[i])
                total -= 1
                print(total)
# print(c1,c2,c3)