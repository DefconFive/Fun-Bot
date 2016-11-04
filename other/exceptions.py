import shutil
import textwrap

# Base class for control signals
class Signal(Exception):
    pass

# signal to restart the bot
class RestartSignal(Signal):
    pass

# signal to end the bot "gracefully"
class TerminateSignal(Signal):
    pass
