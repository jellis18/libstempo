import subprocess
import logging
from pathlib import Path
import os

logger = logging.getLogger(__name__)

RUNTIME_DIRS = ("atmosphere", "clock", "earth", "ephemeris", "observatory", "solarWindModel")
HOME = os.getenv("HOME")


def find_tempo2_runtime():
    """
    Attempt to find TEMPO2 runtime if TEMPO2 environment variable is not set
    """

    # first check for local install (i.e. from using install_tempo2.sh)
    local_path = Path(HOME) / ".local/share/T2runtime"
    if local_path.exists():
        return str(local_path)

    # if not, check for tempo2 binary in path
    try:
        out = subprocess.check_output("which tempo2", shell=True).decode().strip()
    except subprocess.CalledProcessError:
        raise subprocess.CalledProcessError(
            ("tempo2 does not appear to be in your path. Please make sure the executable is in your path")
        )

    # since this would be in a bin/ directory, navigate back to root and check share/
    share_dir = Path(out).parents[1] / "share"

    if share_dir.exists():
        # loop through all directories in share
        for d in share_dir.iterdir():
            if d.is_dir():
                # if this directory contains the runtime dirs then set this to be the runtime dir
                if all(rd in list(d.iterdir()) for rd in RUNTIME_DIRS):
                    return str(d)
    else:
        raise FileNotFoundError(f"Directory {str(share_dir)} does not exist. Can't find T2runtime")
