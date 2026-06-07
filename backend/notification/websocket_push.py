class WebsocketPush:
    def send(self, user_id, payload):
        return {
            "user_id": user_id,
            "payload": payload
        }
