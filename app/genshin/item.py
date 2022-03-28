from dataclasses import dataclass


@dataclass
class Item:
    id: int
    rarity: int
    location: str
    name: dict[str, str]
    description: dict[str, str]

    def __post_init__(self):
        self.stars = "★" * self.rarity
        
    def get_name(self, locale: str, rarity: bool = False) -> str:
        '''Get localized item name

        :param str locale: name locale
        :param bool rarity: add rarity stars or not, defaults to False
        :return str: localized item name, or 'en' name.
        '''
        name = self.name.get(locale, self.name['en'])
        if rarity:
            name += ' ' + "★" * self.rarity
        return name
    
    def get_desc(self, locale: str) -> str:
        """Get localized item description

        Args:
            locale (str): description locale.

        Returns:
            str: localized item description, or 'en' description.
        """
        return self.description.get(locale, self.description['en'])
