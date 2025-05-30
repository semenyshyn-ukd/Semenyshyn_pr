txt = input("Input text: ")
n = int(input("Input size of text: "))

if len(txt) > n:
    print("Text is longer than size")

positions = []

for i in range(len(txt)):
    if txt[i] == " ":
        positions.append(i)

if not positions:
    print("Space is not in text")
else:
    print(f"Space positions: {positions}")
    print(f"Count of spaces: {len(positions)}")
    no_spaces = txt.replace(" ", "")
    print(f"Text without spaces: {no_spaces}")