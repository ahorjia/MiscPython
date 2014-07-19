import sys

def BinarySequenceGenerate(lst, maxCount) :
  if len(lst) >= maxCount :
    for item in lst :
      sys.stdout.write(str(item))
    print
  else :
    lst0 = lst[:]
    lst0.insert(0, 0)
    BinarySequenceGenerate(lst0, maxCount)
    lst1 = lst[:]
    lst1.insert(0, 1)
    BinarySequenceGenerate(lst1, maxCount)