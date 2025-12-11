class FileReader:
    def read(self, path):
        with open(path, 'r') as f:
            return f.read()
