from piClusterNetworking import client


class CrawlerClient(client.Client):
    def __init__(self, server_host, server_port):
        super().__init__(server_host, server_port)

    def message_handler(self, message):
        pass


def main():
    c = CrawlerClient("192.168.86.100", 8001)


if __name__ == '__main__':
    main()
