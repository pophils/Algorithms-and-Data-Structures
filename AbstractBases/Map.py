
from abc import ABCMeta, abstractmethod
from collections import MutableMapping


class Map (MutableMapping, metaclass=ABCMeta):

    class _Item():

        def __init__(self, k, value):
            self._key = k
            self._value = value

    @abstractmethod
    def clear(self):
        """
        # Could have used the one implemented in super, but it will run in theta(n) where n
        is the number of items in the map.
        :return:
        """
        pass