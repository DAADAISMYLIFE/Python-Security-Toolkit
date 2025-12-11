from filetool.reader import FileReader
from filetool.writer import FileWriter

data = input("파일에 생성할 내용을 입력하세요: ")
path = input("파일 저장 위치를 입력하세요: ")

writer = FileWriter()
reader = FileReader()

writer.write(path, data)
read_data = reader.read(path)

print(read_data)
