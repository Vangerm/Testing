class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename):
        if filename.split('.')[-1] in self.extensions:
            return filename


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]