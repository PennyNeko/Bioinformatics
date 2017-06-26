seqFile = open("./6.15Seq/α-lactalbumin.txt", "r")
seq = []
lines = seqFile.readlines()[1:]
for line in lines:
    for letter in line:
        seq.append(letter)
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
if (winningRemoval):
    print("Player A won.")
    print("Removing sequence was, starting with Player A:")
    i = len(seq)-1
    while(i>0):
        print(winningRemoval[i])
        i -= winningRemoval[i]