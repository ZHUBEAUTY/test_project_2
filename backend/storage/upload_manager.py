import os

BASE_DIR = "/tmp/uploads/"

class UploadManager:
    def save(self, filename, content):
        path = BASE_DIR + filename

        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)

        with open(path, "w") as f:
            f.write(content)

        return path
