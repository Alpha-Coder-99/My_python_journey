#Print how many lines are present in notes .txt
with open ("Chap#20(File Handling)/notes.txt","r") as f:
    lines=f.readlines()
    print("Number of lienes",len(lines))