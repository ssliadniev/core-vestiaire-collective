import time
from math import floor


class LunarStandardTime:
    """
    Class for converting UTC to Lunar Standard Time.
    """
    def __init__(self):
        self.lunar_epoch_unix_time = 14159025
        self.lunar_second_ration_earth_second = 0.984352966667
        self.current_time = int(time.time())
        self.unix_seconds_since_lunar_epoch = (
            self.current_time + self.lunar_epoch_unix_time
        )
        self.lunar_time = int(
            self.unix_seconds_since_lunar_epoch / self.lunar_second_ration_earth_second
        )
        self.lunar_day_names = [
            "Armstrong", "Aldrin", "Conrad", "Bean", "Shepard", "Mitchell", "Scott",
            "Irwin", "Young", "Duke", "Cernan", "Schmitt"]

    def lunar_datetime(self):
        years = floor(self.lunar_time / (12 * 30 * 24 * 60 * 60)) + 1
        days = (
            floor(self.lunar_time % (12 * 30 * 24 * 60 * 60) / (30 * 24 * 60 * 60)) + 1
        )
        cycles = floor(self.lunar_time % (30 * 24 * 60 * 60) / (24 * 60 * 60)) + 1
        hours = floor(self.lunar_time % (24 * 60 * 60) / 3600)
        minutes = floor(self.lunar_time % (60 * 60) / 60)
        seconds = floor(self.lunar_time % 60)

        datetime = {
            "s": self.lunar_time,
            "y": years,
            "j": days,
            "c": cycles,
            "G": hours,
            "n": minutes,
            "?": seconds,
            "Y": "{:02d}".format(years),
            "d": "{:02d}".format(days),
            "C": "{:02d}".format(cycles),
            "H": "{:02d}".format(hours),
            "i": "{:02d}".format(minutes),
            "S": "{:02d}".format(seconds),
            "z": days * 30 + cycles,
            "g": hours % 12 + 1,
            "h": "{:02d}".format(hours % 12 + 1),
            "!": "▽",
            "T": "LST",
            "D": self.lunar_day_names[days - 1],
        }

        return f"{datetime['Y']}-{datetime['d']}-{datetime['c']} {datetime['!']} {datetime['H']}:{datetime['i']}:" \
               f"{datetime['S']} {datetime['T']}, {datetime['D']}"
