"""
ディレクトリ作成
- atcoder
    - A
        - execute.py
        - input.txt
"""
import argparse
from base.create_file import CreateFileFactory

TEMPLATE = '''"""
Title:

URL:

Memo:

Run:
    >>> rye run python %s < %s
"""
'''

parser = argparse.ArgumentParser(
    prog="Create Template Directory",
    usage="create_directory.py -p='atcoder/999' -n='A'",
    epilog="end",
)
parser.add_argument("-p", "--path", type=str, help="ディレクトリを作成するパス")
parser.add_argument("-n", "--name", type=str, help="ディレクトリに作成する問題の名前")


def main(path: str, name: str) -> None:
    directory_path = f"{path}/{name}"
    factory = CreateFileFactory()
    factory.create_directory(directory_path)
    factory.create_source(directory_path)
    factory.create_input(directory_path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(path=args.path, name=args.name)
