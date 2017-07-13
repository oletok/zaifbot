from zaifbot.rules.exit import Exit
from zaifbot.closing_price import latest_closing_price


class BuyLowerExit(Exit):
    def __init__(self, exit_price):
        super().__init__()
        self.exit_price = exit_price

    def can_exit(self, trade):
        return self.exit_price < latest_closing_price(trade.currency_pair)
