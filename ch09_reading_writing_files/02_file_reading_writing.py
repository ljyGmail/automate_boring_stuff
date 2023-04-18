from pathlib import Path
p = Path('data/ch09/spam.txt')
print(f"p.write_text(): {p.write_text('Hello, world!')}")
print(f"p.read_text(): {p.read_text()}")

# Opening Files with the open() Function
# helloFile = open(Path.home() / 'hello.txt')
helloFile = open('data/ch09/hello.txt')

# Reading the Contents of Files
helloContent = helloFile.read()
print(f'helloContent: {helloContent}')

sonnetFile = open('data/ch09/sonnet29.txt')
print(f'sonnetFile.readlines(): {sonnetFile.readlines()}')

# Writing to Files
baconFile = open('data/ch09/bacon.txt', 'w')
baconFile.write('Django Flask\n')
baconFile.close()
baconFile = open('data/ch09/bacon.txt', 'a')
baconFile.write('BeatifulSoup')
baconFile.close()
baconFile = open('data/ch09/bacon.txt')
content = baconFile.read()
baconFile.close()
print(f'content: {content}')
