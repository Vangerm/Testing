class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    __IP = None

    def __init__(self):
        self.buffer = list()

    def send_data(self, data: Data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer);
        """
        Router.add_data(data)

    def push_data(self, data):
        self.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        result = self.buffer
        self.buffer = list()
        return result

    def set_ip(self, ip):
        self.__IP = ip

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.__IP


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    SERVER_LIST: list = list()
    buffer: list = list()

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        self.SERVER_LIST.append(server)
        server.set_ip(len(self.SERVER_LIST))

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        self.SERVER_LIST.remove(server)

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for data in self.buffer:
            for server in self.SERVER_LIST:
                if data.ip == server.get_ip():
                    server.push_data(data)
                    break
        self.buffer = list()

    @classmethod
    def add_data(cls, data):
        cls.buffer.append(data)


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from)
print(msg_lst_to)
