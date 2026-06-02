import secrets
from .session_store import SessionStore

store = SessionStore()

class JWTManager:
    def generate(self, user_id):
        token = secrets.token_hex(16)
        store.save(user_id, token)
        return token

    def refresh(self, user_id):
        old = store.get(user_id)
        token = secrets.token_hex(16)
        store.save(user_id, token)
        return {
            "old": old,
            "new": token
        }
