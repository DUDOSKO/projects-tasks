"""Модуль с классами для описания различных материалов"""
from typing import Union
class Wood:
    """Класс представляющий древесину"""
    def __init__(self, name: str, radius: Union[int, float], height: Union[int, float]) -> None:
        """
        Инициализация объекта древесины.

        Args:
            name: Название древесины
            radius: Радиус бревна
            height: Высота бревна

        Raises:
            TypeError: Если передан неверный тип данных
            ValueError: Если значение не положительное
        """
        self.radius = self.init_radius(radius)
        self.name = self.init_name(name)
        self.height = self.init_height(height)
    def init_radius(self, radius: Union[int, float]) -> float:
        """Проверка и инициализация радиуса."""
        if not isinstance(radius, (int, float)):
            raise TypeError
        if not radius > 0:
            raise ValueError
        return float(radius)
    def init_name(self, name: str) -> str:
        """Проверка и инициализация названия."""
        if not isinstance(name, str):
            raise TypeError
        return name
    def init_height(self, height: Union[int, float]) -> float:
        """Проверка и инициализация высоты."""
        if not isinstance(height, (int, float)):
            raise TypeError
        if not height > 0:
            raise ValueError
        return float(height)
class Glass:
    """Класс, представляющий стекло."""
    def __init__(self, name: str, endurance: str) -> None:
        """
        Инициализация объекта стекла.

            Args:
                name: Название стекла
                endurance: Прочность стекла

            Raises:
                TypeError: Если передан неверный тип данных
        """
        self.name = self.init_glass(name)
        self.endurance = self.init_endurance(endurance)
    def init_glass(self, name: str) -> str:
        if not isinstance(name, str):
            raise TypeError
        return name
    def init_endurance(self, endurance: str) -> str:
        if not isinstance(endurance, str):
            raise TypeError
        return endurance
class Steel:
    """Класс представляющий сталь"""
    def __init__(self, name, price):
        """
        Инициализация объекта стали.

            Args:
                name: Название стали
                price: Цена стали

            Raises:
                TypeError: Если передан неверный тип данных
                ValueError: Если цена не положительная
        """
        self.price = self.init_price(price)
        self.name = self.init_name(name)
    def init_price(self, price: Union[int, float]) -> float:
        """Проверка и инициализация цены."""
        if not isinstance(price, (int, float)):
            raise TypeError
        if not price > 0:
            raise ValueError
        return float(price)
    def init_name(self, name: str) -> str:
        """Проверка и инициализация названия."""
        if not isinstance(name, str):
            raise TypeError
        return name
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    # Вывод документации классов
    help(Glass)
    help(Steel)
    help(Wood)

    import doctest

    doctest.testmod()

