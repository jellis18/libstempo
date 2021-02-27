__version__ = "2.3.5"

import os


# check to see if TEMPO2 environment variable is set
TEMPO2_RUNTIME = os.getenv("TEMPO2")


def _find_tempo2_runtime():
    return "/usr/local/share/T2runtime"


# if not try to find it and raise error otherwise
if not TEMPO2_RUNTIME:
    os.environ["TEMPO2"] = _find_tempo2_runtime()


from libstempo.libstempo import *  # noqa F401,F402,F403
