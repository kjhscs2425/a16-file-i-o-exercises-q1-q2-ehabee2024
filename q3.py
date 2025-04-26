# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
f = ""
with open("romeo_and_juliet.txt", "r") as f:
    book = f.read()


# Count how many times the word "Juliet" appears

juliet_count = 0
for word in book.split(" "):
    if word == "Juliet":
        juliet_count = juliet_count + 1
print(f"juliet appears {juliet_count} times")