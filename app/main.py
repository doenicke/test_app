import fire
from . import __version__


def main(name):
    print(f"Hallo {name}!")
    print(f"Version: {__version__}")


if __name__ == '__main__':
    fire.Fire(main)
