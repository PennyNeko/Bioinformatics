def fillSeq(selectedSeqName):
    seqFile = open("./6.12Seq/" + selectedSeqName + ".txt", "r")
    seq = []
    lines = seqFile.readlines()[1:]
    for line in lines:
        for letter in line:
            seq.append(letter)
    seqFile.close()

seq1 = fillSeq(input("Select first sequence to use (brain, liver or muscle)"))
seq2 = fillSeq(input("Select second sequence to use (brain, liver or muscle)"))

seq1 = ['A', 'B', 'C','D','C','D']
seq2 = ['A', 'B', 'B']

if len(seq2) > len(seq1):
    temp = seq1
    seq1 = seq2
    seq2 = temp

canWin = []
winningRemoval = []
winningSeq = []
canWin.append(False)
canWin.append(True)
for i in range(2,len(seq1)+1):
    for j in range(1,int((i/2)+1)):
        if not(canWin[j]) and not(canWin[i-j]):
            canWin.append(True)
            winningSeq.append(j)
            winningSplit = []
            winningSplit.append(j)
            winningSplit.append(i-j)
            winningRemoval.append(winningSplit)
            break
    else:
        canWin.append(False)
if (canWin[-1] or canWin[len(seq2)]):
    if canWin[len(seq2)]:
        winLen = len(seq2)
    else:
        winLen = len(seq1)
    print("Player A won.")
    print("Splitting sequence was, starting with Player A:")
    i = winLen-1
    j = len(winningRemoval) - 1
    while (j>=0):
        print("Selected sequence: " + winningSeq[j])
        print("and split into: " + winningRemoval)
        if not(winningRemoval[j][0]):
            i -= winningRemoval[[j][0]]
        else:
            i -=winningRemoval[j][1]
else:
    print("Player A lost.")