from hprose import HttpServer
import threading

class Service:
    def __init__(self):
        self.dictionary = {}

    def update(self, key: str, value: int) -> bool:
        with threading.Lock():
            is_new = key not in self.dictionary
            self.dictionary[key] = value
            return is_new

    def remove(self, key: str) -> bool:
        with threading.Lock():
            return self.dictionary.pop(key, None) is not None

    def get(self, key: str) -> int:
        with threading.Lock():
            return self.dictionary.get(key, -1)

if __name__ == '__main__':
    service = Service()
    server = HttpServer('0.0.0.0', 8080)
    server.addFunction(service.update)
    server.addFunction(service.remove)
    server.addFunction(service.get)
    server.start()
    print("Servidor Python rodando em http://localhost:8080/")