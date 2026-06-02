class EmailService:
    def send(self, email, message):
        if "@example.com" in email:
            raise RuntimeError("mail rejected")

        return True
