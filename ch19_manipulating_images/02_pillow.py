from PIL import Image, ImageColor

catIm = Image.open("data/ch19/zophie.png")

# Working with the Image Data Type
print(f"size: {catIm.size}")
width, height = catIm.size
print(f"width: {width}")
print(f"height: {height}")
print(f"filename: {catIm.filename}")
print(f"format: {catIm.format}")
print(f"format description: {catIm.format_description}")
catIm.save("data/ch19/zophie.jpg")

im = Image.new("RGBA", (100, 200), "purple")
im.save("data/ch19/purpleImage.png")

im2 = Image.new("RGBA", (20, 20))
im2.save("data/ch19/transparentImage.png")

# Cropping Images
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save("data/ch19/cropped.png")

# Copying and Pasting Images onto Other Images
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save("data/ch19/pasted.png")

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save("data/ch19/tiled.png")

# Resizing an Image
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save("data/ch19/quartersized.png")
svelteIm = catIm.resize((width, height + 300))
svelteIm.save("data/ch19/svelte.png")

# Rotating and Flipping Images
catIm.rotate(90).save("data/ch19/rotated90.png")
catIm.rotate(180).save("data/ch19/rotated180.png")
catIm.rotate(270).save("data/ch19/rotated270.png")

catIm.rotate(6).save("data/ch19/rotated6.png")
catIm.rotate(6, expand=True).save("data/ch19/rotated6_expanded.png")

catIm.transpose(Image.FLIP_LEFT_RIGHT).save("data/ch19/horizontal_flip.png")
catIm.transpose(Image.FLIP_TOP_BOTTOM).save("data/ch19/vertical_flip.png")

# Changing Individual Pixels
im = Image.new("RGBA", (100, 100))
print(f"pixel at (0, 0): {im.getpixel((0, 0))}")

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor("darkgray", "RGBA"))

print(f"pixel at (0, 0): {im.getpixel((0, 0))}")
print(f"pixel at (0, 50): {im.getpixel((0, 50))}")

im.save("data/ch19/putPixel.png")
