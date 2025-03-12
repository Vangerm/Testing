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