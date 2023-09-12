"""
https://stepik.org/lesson/864077/step/3?unit=923013

Класс CaesarCipher
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].
"""

from string import ascii_letters

class CaesarCipher:

    def __init__(self, shift):
        self.shift = shift
        self.mode = 1

    def convert(self, ord):
        if ord in range(97, 123):
            ord += self.shift * self.mode
            if ord > 122:
                ord -= 26
            if ord < 97:
                ord += 26
        if ord in range(65, 91):
            ord += self.shift * self.mode
            if ord > 90:
                ord -= 26
            if ord < 65:
                ord += 26
        return ord

    def encode(self, word):
        return ''.join(chr(self.convert(ord(letter))) if letter in ascii_letters else letter for letter in word)

    def decode(self, word):
        self.mode = -1
        return self.encode(word)