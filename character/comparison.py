import pandas as pd


class Compare(object):
    def __init__(self, characters):
        self.all_characters = characters

    def __get_stat(self, char, stat):
        char_data = char.get_data()
        return char_data[stat]

    def __get_capped_stat(self, char, stat, max_value):
        # Getting the HP until it hits the max value once, then we don't need to get it anymore
        s = self.__get_stat(char, stat)
        unique = []
        hit_top = False
        for i in s:
            if not hit_top:
                unique.append(i)
                if i >= max_value:
                    hit_top = True
        return unique

    def get_capped_data(self, stat, max_value):
        max_size = 0
        for c in self.all_characters:
            s = self.__get_capped_stat(c, stat, max_value)
            if len(s) > max_size:
                max_size = len(s)
        values = {}
        for c in self.all_characters:
            s = self.__get_capped_stat(c, stat, max_value)
            while len(s) < max_size:
                s.append(999)
            values[c.get_name()] = s
        return pd.DataFrame(data=values)

    def get_stat_data(self, stat):
        values = {}
        for c in self.all_characters:
            stat_values = self.__get_stat(c, stat)
            values[c.get_name()] = stat_values
        return pd.DataFrame(data=values)

    def get_stat_data_delta(self, stat):
        values = {}
        for c in self.all_characters:
            stat_values = self.__get_stat(c, stat)
            stat_values = stat_values.diff().shift(-1)
            values[c.get_name()] = stat_values
        return pd.DataFrame(data=values)

