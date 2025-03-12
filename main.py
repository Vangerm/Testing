<<<<<<< HEAD
class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request):
        return self.get(self.__fn, request)

    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == 'GET':
            pass
        else:
            return None
        return f'GET: {func(None)}'


@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
=======
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
>>>>>>> 6e541e3775f9d662008d729578974a56b5029446
