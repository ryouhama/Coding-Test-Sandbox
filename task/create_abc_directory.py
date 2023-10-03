"""
ディレクトリ作成(Atcoder ABC)

- atcoder
	- ABC
		- {name}
			- A
				- execute.py
				- input.txt
			- B
				- execute.py
				- input.txt
			- C
				- execute.py
				- input.txt
			- D
				- execute.py
				- input.txt
			- E
				- execute.py
				- input.txt
			- F
				- execute.py
				- input.txt
			- G
				- execute.py
				- input.txt
"""
import argparse
from base.create_file import CreateFileFactory

parser = argparse.ArgumentParser(
    prog="Create Atcoder ABC Directory",
    usage="create_abc_directory.py -n='999'",
    epilog="end",
)
parser.add_argument("-n", "--name", type=str, help="ディレクトリに作成する問題の番号")

ABC_DIRECTORY = ["A", "B", "C", "D", "E", "F", "G"]


def main(name: str) -> None:
    for it in ABC_DIRECTORY:
        directory_path = f"atcoder/ABC/{name}/{it}"
        factory = CreateFileFactory()
        factory.create_directory(directory_path)
        factory.create_source(directory_path)
        factory.create_input(directory_path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(name=args.name)
