import json

from plex_post import Printable, Account, Server, Player, Metadata


class Response(Printable):
    def __init__(self, data, request=None) -> None:
        data = data.get("payload")
        data = json.loads(data)
        self.event = data.get("event")
        self.user = data.get("user")
        self.owner = data.get("owner")
        self.account = Account(data.get("Account"))
        self.server = Server(data.get("Server"))
        self.player = Player(data.get("Player"))
        self.metadata = Metadata(data.get("Metadata"))
        if request:
            self.request = request
