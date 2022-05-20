
#file handle
fhand = open ('data.txt')
count = 0
fnames = list()

#for line in file handle
for line in fhand :
    line = line.rstrip()
    #append split(seperator splitting string, specifies how many splits)[index 0, aka the first item in the split of each line]
    fnames.append(line.split (None, 1)[0])

#def fx counter: takes string entries, outputs counts of word occurrences
def counter(stg):
    #ordered collection, changeable; no duplicates
    counts = {}
    words = stg

    for word in words :
        if word in counts :
            counts [word] += 1
        else :
            counts [word] = 1
#return is class dict
    return counts


#column formatter for printing items from dictionary
def columnformatter(dict):

    for index in dict:
        print (index, dict[index])
    return

columnformatter(counter(fnames))
