"""
ディレクトリ作成
- atcoder
    - A
        - execute.py
        - input.txt
"""
import os
import argparse

TEMPLATE = '''"""
Title: 
URL: 
>>> rye run python %s < %s
"""
'''

parser = argparse.ArgumentParser(
    prog="Create Template Directory",
    usage="create_directory.py -p='atcoder/999' -n='A'",
    epilog="end"
)
parser.add_argument('-p', '--path', help="ディレクトリを作成するパス")
parser.add_argument('-n', '--name', help="ディレクトリに作成する問題の名前")


def main(path: str, name: str) -> None:
    directory_path = f"{path}/{name}"
    os.makedirs(directory_path, exist_ok=True)
    with open(f"{directory_path}/execute.py", mode="w") as file:
        file.write(TEMPLATE % (f"{directory_path}/execute.py", f"{directory_path}/input.txt"))

    with open(f"{path}/{name}/input.txt", mode="w") as file:
        file.write("")
    
if __name__ == "__main__":
    args = parser.parse_args()
    main(path=args.path, name=args.name)
