def fillSeq(selectedSeqName):
    seqFile = open("./6.12-6.14Seq/" + selectedSeqName + ".txt", "r")
    seq = []
    lines = seqFile.readlines()[1:]
    for line in lines:
        for letter in line:
            seq.append(letter)
    seqFile.close()
    return seq

seq1 = fillSeq(input("Select first sequence to use (brain, liver or muscle)"))
seq2 = fillSeq(input("Select second sequence to use (brain, liver or muscle)"))

if len(seq2) > len(seq1):
    temp = seq1
    seq1 = seq2
    seq2 = temp

canWin = []
winningRemoval = []
canWin.append(False)
canWin.append(True)
for i in range(2,len(seq1)+1):
    for j in range(1,int((i/2)+1)):
        if not(canWin[j]) and not(canWin[i-j]):
            canWin.append(True)
            winningSplit = []
            winningSplit.append(j)
            winningSplit.append(i-j)
            winningRemoval.append(winningSplit)
            break
    else:
        canWin.append(False)
if (canWin[-1] or canWin[len(seq2)]):
    print("Player A won.")
else:
    print("Player A lost.")
print("Winning splits were:")
for i in winningRemoval:
    print(i)