from moon_phase import MoonPhase


class BaseAdvisor:

    def get_advice(self):
        raise NotImplementedError


class LunarAdvisor(BaseAdvisor):

    def get_advice(self):

        moon = MoonPhase()
        phase = moon.get_phase_name()

        if "New Moon" in phase:
            return "🌑 New Moon Energy\n\n• Start new habits\n• Set goals\n• Plan"

        elif "Waxing Crescent" in phase:
            return "🌒 Waxing Energy\n\n• Build motivation\n• Learn\n• Start actions"

        elif "First Quarter" in phase:
            return "🌓 First Quarter Energy\n\n• Take action\n• Solve problems"

        elif "Waxing Gibbous" in phase:
            return "🌔 Waxing Gibbous Energy\n\n• Improve work\n• Refine skills"

        elif "Full Moon" in phase:
            return "🌕 Full Moon Energy\n\n• Creativity\n• Emotions\n• Release"

        elif "Waning Gibbous" in phase:
            return "🌖 Waning Gibbous Energy\n\n• Gratitude\n• Reflection"

        elif "Last Quarter" in phase:
            return "🌗 Last Quarter Energy\n\n• Let go\n• Clean up"

        else:
            return "🌘 Waning Crescent Energy\n\n• Rest\n• Recover"

    def get_best_activities(self):

        moon = MoonPhase()
        phase = moon.get_phase_name()

        if "New Moon" in phase:
            return "🌑 New Moon: \n\n• Waiting\n• Journaling\n• Meditating\n• Reading\n• Listening"

        elif "Waxing Crescent" in phase:
            return "🌒 Waxing: \n\n• Setting intentions\n• Reaching out\n• Taking risks\n• Experimenting"

        elif "First Quarter" in phase:
            return "🌓 First Quarter: \n\n• Making decisions\n• Organizing\n• Making a to-do list"

        elif "Waxing Gibbous" in phase:
            return "🌔 Waxing Gibbous: \n\n• Working out\n• Editing\n• Preparing party snacks\n• Refining a pitch"

        elif "Full Moon" in phase:
            return "🌕 Full Moon: \n\n• Presenting\n• Partying\n• Expressing yourself"

        elif "Waning Gibbous" in phase:
            return "🌖 Waning Gibbous: \n\n• Networking\n• Socializing\n• Collecting feedback"

        elif "Last Quarter" in phase:
            return "🌗 Last Quarter: \n\n• Pivoting\n• Regrouping\n• Reflective journaling"

        else:
            return "🌘 Waning Crescent: \n\n• Cleaning\n• Resting\n• Leaving\n• Quitting"