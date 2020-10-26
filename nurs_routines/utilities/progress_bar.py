import sys


class ProgressBar:

    def __init__(self, bar_width, N):
        self.bar_width = bar_width
        self.N = N
        self.K = 1

    def update(self, x, p):
        x = int(x)
        progress_bar = "".join(["|", x*"X", (self.bar_width - x) * ".", "|"])
        progress_percent = " [{:.1f}%]".format(p)
        sys.stdout.write("\r" + progress_bar + progress_percent)

    def step(self):
        self.K = self.K + 1
        p = self.K / self.N
        x = p * self.bar_width
        self.update(x, p*100)


