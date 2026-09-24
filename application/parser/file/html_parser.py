"""HTML parser.

Contains parser for html files.

"""
from pathlib import Path

from application.parser.file.base_parser import BaseParser


class HTMLParser(BaseParser):
    """HTML parser."""

    def _init_parser(self) -> dict:
        """Init parser."""
        return {}

    def parse_file(self, file: Path, errors: str = "ignore") -> str | list[str]:
        from langchain_community.document_loaders import BSHTMLLoader

        loader = BSHTMLLoader(file)
        data = loader.load()        
        return data
