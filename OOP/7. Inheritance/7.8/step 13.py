"""
https://stepik.org/lesson/804638/step/13?unit=807762

Классы Lecture и Conference🌶️
1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

topic — тема выступления
start_time — время начала выступления в виде строки в формате HH:MM
duration — длительность выступления в виде строки в формате HH:MM
2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Conference должен иметь четыре метода экземпляра:

add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
Провести выступление в это время невозможно
total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строке в формате HH:MM
Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.

"""


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration


class Conference:

    def __init__(self):
        self.conferences = []
        self.blocked_time = []

    @staticmethod
    def time_to_int(time):
        hours, minutes = time.split(':')
        return int(hours) * 60 + int(minutes)

    @staticmethod
    def int_to_time(time):
        hours = time // 60
        minutes = time % 60
        return str(hours).zfill(2) + ':' + str(minutes).zfill(2)

    def time_to_range(self, start_time, duration):
        start = self.time_to_int(start_time)
        end = self.time_to_int(duration)
        return range(start, start+end)

    def block_time(self, timerange):
        self.blocked_time.append(timerange)

    def add(self, performance):
        check_range = self.time_to_range(performance.start_time, performance.duration)
        for time_range in self.blocked_time:
            if set(time_range).intersection(set(check_range)):
                raise ValueError('Провести выступление в это время невозможно')
        self.conferences.append(performance)
        self.block_time(check_range)

    def total(self):
        total_duration = sum(self.time_to_int(item.duration) for item in self.conferences)
        return self.int_to_time(total_duration)

    def longest_lecture(self):
        longest_lecture = max(self.time_to_int(item.duration) for item in self.conferences)
        return self.int_to_time(longest_lecture)

    def longest_break(self):
        starts = sorted([self.time_to_int(i.start_time) for i in self.conferences], reverse=True)
        ends = sorted([(self.time_to_int(i.start_time) + self.time_to_int(i.duration)) for i in self.conferences], reverse=True)
        longest_break = max([starts[i]-ends[i+1] for i in range(len(starts)-1)])
        return self.int_to_time(longest_break)
