from time import sleep


class Request:
    def get(self, index: int):
        # request data from network
        sleep(index)


def request_ten_times(request: Request):
    for i in range(10):
        request.get(i)


def call_ten_times(func: callable):
    for i in range(10):
        func(i)
