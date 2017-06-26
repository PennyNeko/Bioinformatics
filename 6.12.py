selectedSeq = input("Select sequence to use (brain, liver or muscle)")
seqFile = open("./6.12Seq/"+ selectedSeq+".txt", "r")
seq = []
lines = seqFile.readlines()[1:]
for line in lines:
    for letter in line:
        seq.append(letter)
seqFile.close()
