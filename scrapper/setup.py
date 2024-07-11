import sys
import os

def path_setup() -> None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))

