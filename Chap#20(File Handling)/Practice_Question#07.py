# Read full file named "story.txt" and prints the full content
with open("Chap#20(File Handling)/Story.txt","r",encoding="utf-8") as f:
    content=f.read()
    print(content)