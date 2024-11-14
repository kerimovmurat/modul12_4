#-*- coding: utf-8 -*-
from unittest import TestCase
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s | %(funcName)s")
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(TestCase):

    def test_walk(self):
        try:
            r1 = Runner('Вася', speed=-10) # создаем объект класса Runner с произвольным именем
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10): # вызываем метод walk 10 раз
                r1.walk()
            self.assertEqual(r1.distance, 50) # сравниваем distance этого объекта со значением 50
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)



    def test_run(self):
        try:
            r2 = Runner(12345)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100) # сравниваем distance этого объекта со значением 100
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)





