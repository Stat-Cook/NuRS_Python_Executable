"""
A progress bar UI element.
"""
import sys
import logging


class ProgressBar:
    """
    A UI element for visualizing how complete a routine is.
    Parameters
    ----------
    bar_width: int
        width of UI bar to print
    max_steps: int
        maximum number of iterations that will occur.
    """

    def __init__(self, bar_width, max_steps):
        self.bar_width = bar_width
        self.max_steps = max_steps
        self.current_step = 1

    def update(self, blocks_done, percentage_done):
        """
        Update the UI element.
        Parameters
        ----------
        blocks_done: int
            number of items to mark complete
        percentage_done: float
            percentage completion
        """
        blocks_done = int(blocks_done)
        progress_bar = "".join(["|", blocks_done * "X", (self.bar_width - blocks_done) * ".", "|"])
        progress_percent = " [{:.1f}%]".format(percentage_done)
        sys.stdout.write("\r" + progress_bar + progress_percent)

    def step(self):
        """
        Increase progress count by one and update UI.
        """
        self.current_step = self.current_step + 1
        percentage = self.current_step / (self.max_steps + 1)
        blocks_done = percentage * self.bar_width
        self.update(blocks_done, percentage*100)


def progress_bar_iter(groups, func, size_check, bar_size=20):
    """
    For a group DataFrame, iterate through and apply 'func' at each step.

    Parameters
    ----------
    groups: pandas.GroupedDataFrame
    func: function
    size_check:bool
        boolean flag
    bar_size: int
        width of the UI bar.
    """
    progress = ProgressBar(bar_size, len(groups.groups))
    print(progress.max_steps)

    logging.info("Shuffle in progress:")
    for i, j in groups:
        progress.step()
        # logging.debug("Shuffling data for: {}".format(i))
        yield func(j, size_check, i)
