"""
https://stepik.org/lesson/864077/step/5?unit=923013

Классы Domain и DomainException
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():

domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:

Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен.

Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.
"""

import re

class Domain:

    pattern_domain = r'^\w+\.\w+$'
    pattern_url = r'^https?:\/\/\w+\.\w+$'
    pattern_email = r'^[a-zA-Z]+@\w+\.\w+$'
    patterns = [pattern_domain, pattern_url, pattern_email]

    def __init__(self, domain):
        if not any(re.match(pattern, domain) for pattern in self.patterns):
            raise DomainException
        self.domain = domain

    @classmethod
    def from_url(cls, url):
        if not re.match(cls.pattern_url, url):
            raise DomainException
        url = url.split('//')
        return cls(url[1])

    @classmethod
    def from_email(cls, email):
        if not re.match(cls.pattern_email, email):
            raise DomainException
        email = email.split('@')
        return cls(email[1])

    def __repr__(self):
        return f'{self.domain}'

class DomainException(Exception):
    def __init__(self, *args):
        super().__init__('Недопустимый домен, url или email')

emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
        print(domain)
    except DomainException as e:
        print(e)