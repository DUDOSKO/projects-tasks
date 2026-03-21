from __future__ import annotations


class SocialNetwork:
    """
    Базовый класс для описания социальной сети.

    Атрибуты:
        name: Название социальной сети.
        audience_mln: Размер аудитории в миллионах пользователей.
        has_messaging: Поддерживает ли социальная сеть личные сообщения.
        _region: Основной регион распространения.

    Инкапсуляция:
        Атрибут _region сделан непубличным, так как предполагается,
        что регион — это внутренняя характеристика объекта, которую
        не следует изменять напрямую извне без контроля.
    """

    def __init__(
            self,
            name: str,
            audience_mln: float,
            has_messaging: bool,
            region: str
    ) -> None:
        """
        Создаёт объект социальной сети.

        Args:
            name: Название социальной сети.
            audience_mln: Размер аудитории в миллионах пользователей.
            has_messaging: Наличие личных сообщений.
            region: Основной регион распространения.
        """
        self.name: str = name
        self.audience_mln: float = audience_mln
        self.has_messaging: bool = has_messaging
        self._region: str = region

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.

        Returns:
            Удобочитаемая строка с основной информацией о социальной сети.
        """
        return (
            f"Социальная сеть '{self.name}': аудитория — {self.audience_mln} млн, "
            f"личные сообщения — {'есть' if self.has_messaging else 'нет'}."
        )

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        Returns:
            Строка, пригодная для отладки.
        """
        return (
            f"SocialNetwork(name={self.name!r}, audience_mln={self.audience_mln!r}, "
            f"has_messaging={self.has_messaging!r}, region={self._region!r})"
        )

    def publish_post(self, text: str) -> str:
        """
        Публикует пост в социальной сети.

        Args:
            text: Текст публикации.

        Returns:
            Сообщение о публикации поста.
        """
        return f"Пост опубликован в социальной сети '{self.name}': {text}"

    def get_region(self) -> str:
        """
        Возвращает основной регион распространения социальной сети.

        Returns:
            Название региона.
        """
        return self._region

    def calculate_ads_cost(self, views: int) -> float:
        """
        Рассчитывает условную стоимость рекламы по числу просмотров.

        Args:
            views: Количество просмотров рекламы.

        Returns:
            Условная стоимость рекламы.
        """
        return views * 0.02


class VK(SocialNetwork):
    """
    Дочерний класс, описывающий социальную сеть VK.

    Дополнительные атрибуты:
        supports_mini_apps: Поддерживаются ли мини-приложения.
    """

    def __init__(
            self,
            name: str,
            audience_mln: float,
            has_messaging: bool,
            region: str,
            supports_mini_apps: bool
    ) -> None:
        """
        Создаёт объект социальной сети VK.

        Расширяет конструктор базового класса добавлением признака
        поддержки мини-приложений.

        Args:
            name: Название социальной сети.
            audience_mln: Размер аудитории в миллионах пользователей.
            has_messaging: Наличие личных сообщений.
            region: Основной регион распространения.
            supports_mini_apps: Наличие поддержки мини-приложений.
        """
        super().__init__(name, audience_mln, has_messaging, region)
        self.supports_mini_apps: bool = supports_mini_apps

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта VK для пользователя.

        Returns:
            Удобочитаемая строка с основной информацией о VK.
        """
        return (
            f"VK '{self.name}': аудитория — {self.audience_mln} млн, "
            f"сообщения — {'есть' if self.has_messaging else 'нет'}, "
            f"мини-приложения — {'поддерживаются' if self.supports_mini_apps else 'не поддерживаются'}."
        )

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта VK.

        Returns:
            Строка, пригодная для отладки.
        """
        return (
            f"VK(name={self.name!r}, audience_mln={self.audience_mln!r}, "
            f"has_messaging={self.has_messaging!r}, region={self._region!r}, "
            f"supports_mini_apps={self.supports_mini_apps!r})"
        )

    def publish_post(self, text: str) -> str:
        """
        Публикует пост в VK с учётом особенностей платформы.

        Причина перегрузки:
            Метод базового класса был перегружен, потому что VK поддерживает
            дополнительные механики публикации, например ленты сообществ,
            рекомендации и расширенные форматы записей. Поэтому логика
            публикации в VK может отличаться от абстрактной социальной сети.

        Args:
            text: Текст публикации.

        Returns:
            Сообщение о публикации поста в VK.
        """
        return f"Запись опубликована во VK '{self.name}' и показана в ленте: {text}"

    def launch_mini_app(self, app_name: str) -> str:
        """
        Запускает мини-приложение внутри VK.

        Args:
            app_name: Название мини-приложения.

        Returns:
            Результат запуска мини-приложения.
        """
        if not self.supports_mini_apps:
            return f"Мини-приложения в '{self.name}' не поддерживаются."
        return f"Мини-приложение '{app_name}' успешно запущено в '{self.name}'."


if __name__ == "__main__":
    social_network: SocialNetwork = SocialNetwork(
        name="GenericNet",
        audience_mln=120.5,
        has_messaging=True,
        region="Международный"
    )

    vk_network: VK = VK(
        name="ВКонтакте",
        audience_mln=76.0,
        has_messaging=True,
        region="Россия и СНГ",
        supports_mini_apps=True
    )

    print(social_network)
    print(repr(social_network))
    print(social_network.publish_post("Добро пожаловать!"))
    print(social_network.get_region())
    print(social_network.calculate_ads_cost(5000))

    print()

    print(vk_network)
    print(repr(vk_network))
    print(vk_network.publish_post("Новый пост во ВКонтакте"))
    print(vk_network.get_region())  # унаследованный метод
    print(vk_network.calculate_ads_cost(5000))  # унаследованный метод
    print(vk_network.launch_mini_app("Музыка"))
