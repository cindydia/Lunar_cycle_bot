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
            return "🌑 Journaling, planning"

        elif "Waxing Crescent" in phase:
            return "🌒 Learning, habits"

        elif "First Quarter" in phase:
            return "🌓 Work, tasks"

        elif "Waxing Gibbous" in phase:
            return "🌔 Improving, practice"

        elif "Full Moon" in phase:
            return "🌕 Creativity, social"

        elif "Waning Gibbous" in phase:
            return "🌖 Reflection"

        elif "Last Quarter" in phase:
            return "🌗 Organizing"

        else:
            return "🌘 Rest"