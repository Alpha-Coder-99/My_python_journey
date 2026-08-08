#Read only first line of bio.txt
with open ("Chap#20(File Handling)/bio.txt","r") as f:
    line1=f.readline()
    print(f"First line of my file is{line1}")