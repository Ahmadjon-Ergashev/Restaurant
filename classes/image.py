def saveImage(src, path):
    print(src, path)
    with open(src, "rb") as file:
        img = file.read()

    with open(path, "wb") as file:
        file.write(img)
