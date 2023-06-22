"""
https://stepik.org/lesson/933767/step/8?unit=939666

Класс ReadableTextFile
Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:

filename — имя текстового файла
Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце. Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.
"""

class ReadableTextFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8', newline='\r\n')
        #or return (line.strip() for line in self.file)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()