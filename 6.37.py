seqFile = open("./6.37Seq/nucleotide.txt", "r")
seq = []
lines = seqFile.readlines()[1:]
for line in lines:
    for letter in line:
        seq.append(letter)
seqFile.close()