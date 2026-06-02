class SessionStore:
    def __init__(self):
        self.sessions = {}

    def save(self, user_id, token):
        self.sessions[user_id] = token

    def get(self, user_id):
        return self.sessions.get(user_id)

    def delete(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]
