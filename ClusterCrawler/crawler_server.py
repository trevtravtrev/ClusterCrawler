from piClusterNetworking import server, messages


class CrawlerServer(server.Server):
    def __init__(self, host_ip, host_port):
        super().__init__(host_ip, host_port)

    def message_handler(self, message):
        pass


def main():
    s = CrawlerServer("192.168.86.100", 8001)
    
    # add crawler code to send 1 website to each client


if __name__ == '__main__':
    main()
