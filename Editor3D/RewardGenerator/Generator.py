# Задание 1. Закончить разработку паттерна Фабричный метод.
# a) Добавить в пример из семинара как минимум 5 наград.
# b) Награды должны генерироваться в соотношении: 10:10:10:10:10(ваши награды):3(золото GOLD):1(алмазы GEM)
# Задание 2. Познакомиться с другими типами паттернов (задание по желанию

from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Platinum(IGameItem):
    def __init__(self):
        print('PLATINUM')

    def open(self):
        pass


class Gold(IGameItem):

    def __init__(self):
        print('GOLD')

    def open(self):
        print('GOLD')


class Silver(IGameItem):
    def __init__(self):
        print("SILVER")

    def open(self):
        pass


class Copper(IGameItem):
    def __init__(self):
        print("COPPER")

    def open(self):
        pass


class Gem(IGameItem):
    def __init__(self):
        print("GEM")

    def open(self):
        pass


class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Platinum()


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()


class CopperGenerator(ItemFabric):
    def create_item(self):
        return Copper()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


if __name__ == "__main__":
    rewards = [CopperGenerator(), SilverGenerator(), GoldGenerator(), PlatinumGenerator(), GemGenerator()]

    for i in range(1, 11):
        rewards[0].create_item()
        rewards[1].create_item()
        rewards[2].create_item()
        if i % 3 == 0:
            rewards[3].create_item()
        if i / 10 >= 1 and i % 10 == 0:
            rewards[-1].create_item()
        print('')
