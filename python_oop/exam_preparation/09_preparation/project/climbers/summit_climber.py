from climbers.base_climber import BaseClimber
from peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    NEEDED_STRENGTH = 75
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= SummitClimber.NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Advanced':
            self.strength -= 30 * 1.3

        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)
