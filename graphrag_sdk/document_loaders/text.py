from typing import Iterator
from graphrag_sdk.document import Document

class TextLoader():
    """
    Load Text
    """

    def __init__(self, path: str) -> None:
        """
        Initialize loader

        Parameters:
            path (str): path to Text.
        """

        self.path = path

    def load(self) -> Iterator[Document]:
        """
        Load Text

        Returns:
            Iterator[Document]: document iterator
        """

        with open(self.path, 'r', encoding='utf-8') as f:
            yield Document(
                f.read()
            )
