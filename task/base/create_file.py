import os
import logging
from dataclasses import dataclass

logger = logging.getLogger()


class CreateFileFactory:
    SOURCE_FILE_NAME = "execute.py"
    INPUT_FILE_NAME = "input.txt"

    TEMPLATE = '''"""
Title:

URL:

Memo:

Run:
	>>> rye run python {source_file_path} < {input_file_path}
"""
'''

    def create_directory(self, path: str) -> None:
        try:
            os.makedirs(path, exist_ok=True)
            logger.info(f"ディレクトリ作成成功 path={path}")
        except OSError as error:
            logger.exception(error)
            logger.error(f"ディレクトリ作成失敗 path={path}")
        except Exception as error:
            logger.exception(error)
            logger.error(f"ディレクトリ作成失敗 path={path}")

    def create_source(self, path: str) -> None:
        source_file_path = f"{path}/{self.SOURCE_FILE_NAME}"
        input_file_path = f"{path}/{self.INPUT_FILE_NAME}"
        with open(source_file_path, mode="w") as file:
            file.write(
                self.TEMPLATE.format(
                    source_file_path=source_file_path, input_file_path=input_file_path
                )
            )
        logger.info(f"ソースファイル作成成功 path={path}")

    def create_input(self, path: str) -> None:
        with open(f"{path}/{self.SOURCE_FILE_NAME}", mode="w") as file:
            file.write("")
        logger.info(f"インプット作成成功 path={path}")
