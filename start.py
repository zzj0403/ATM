import os, sys

print(os.path.dirname(__file__))

from core import src

path = os.path.dirname(__file__)
sys.path.append(path)
if __name__ == "__main__":
    src.run()
