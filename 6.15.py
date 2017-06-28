seqFile = open("./6.15Seq/α-lactalbumin.txt", "r")
seq = []
lines = seqFile.readlines()[1:]
for line in lines:
    for letter in line:
        seq.append(letter)
seqFile.close()

seq = ['A','B','B']
canWin = []
winningRemoval = []
canWin.append(False)
for i in range(1,len(seq)+1):
    if not(canWin[i-1]):
        canWin.append(True)
        winningRemoval.append(1)
    elif not(canWin[i-2]):
        canWin.append(True)
        winningRemoval.append(2)
    else:
        canWin.append(False)
        winningRemoval.append(1)
if (canWin[-1]):
    print("Player A won.")
else:
    print("Player A lost.")
print("Removing sequence was, starting with Player A:")
i = len(winningRemoval)-1
while(i>=0):
    print(winningRemoval[i])
    i -= winningRemoval[i]