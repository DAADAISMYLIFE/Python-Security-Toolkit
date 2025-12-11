class FileWriter:
    def write(self, path, data):
        with open(path, 'w') as f:
            f.write(data)
