import ephem
from datetime import datetime, timedelta


class MoonPhase:

    def __init__(self, date=None):

        self.date = ephem.Date(date or datetime.utcnow())
        self.moon = ephem.Moon(self.date)

    def _moon_age(self):

        new_moon = ephem.previous_new_moon(self.date)
        return float(self.date - new_moon)

    def get_phase_name(self):

        age = self._moon_age()

        if age < 1.845:
            return "New Moon 🌑"
        elif age < 5.536:
            return "Waxing Crescent 🌒"
        elif age < 9.228:
            return "First Quarter 🌓"
        elif age < 12.919:
            return "Waxing Gibbous 🌔"
        elif age < 16.61:
            return "Full Moon 🌕"
        elif age < 20.302:
            return "Waning Gibbous 🌖"
        elif age < 23.993:
            return "Last Quarter 🌗"
        else:
            return "Waning Crescent 🌘"

    def get_phase_description(self):

        descriptions = {
            "New Moon 🌑": "New beginnings.",
            "Waxing Crescent 🌒": "Growth starts.",
            "First Quarter 🌓": "Action time.",
            "Waxing Gibbous 🌔": "Refine progress.",
            "Full Moon 🌕": "Peak energy.",
            "Waning Gibbous 🌖": "Gratitude.",
            "Last Quarter 🌗": "Release.",
            "Waning Crescent 🌘": "Rest."
        }

        return descriptions.get(self.get_phase_name(), "Moon energy shifting.")


def get_week_forecast():

    result = "🌙 Weekly Moon Forecast\n\n"

    for i in range(7):

        future_date = datetime.utcnow() + timedelta(days=i)
        moon = MoonPhase(future_date)

        day_name = future_date.strftime("%A")

        result += f"{day_name} — {moon.get_phase_name()}\n"

    return result