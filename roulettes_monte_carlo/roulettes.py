# roulette.py
import random

class FairRoulette:
    """Models a fair roulette with 36 pockets, containing no house edge."""
    def __init__(self):
        # Pockets numbered 1 through 36
        self.pockets = list(range(1, 37))
        self.ball = None
        # Standard casino payout for a single number bet is 35 to 1
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        """Simulates spinning the roulette wheel and landing on a random pocket."""
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        """Calculates the payout or loss when betting on a specific pocket number."""
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return "Fair Roulette"


class EuRoulette(FairRoulette):
    """Models a European Roulette wheel, adding a single '0' pocket."""
    def __init__(self):
        super().__init__()
        self.pockets.append("0")

    def __str__(self):
        return "European Roulette"


class AmRoulette(EuRoulette):
    """Models an American Roulette wheel, adding an extra '00' pocket."""
    def __init__(self):
        super().__init__()
        self.pockets.append("00")

    def __str__(self):
        return "American Roulette"