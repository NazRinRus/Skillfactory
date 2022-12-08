
class OpenFile:
    def __init__(self, path_file, type):
        self.file = open(path_file, type)


    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('hello.txt', 'wt') as f:
    f.write('test C3_5_6')
