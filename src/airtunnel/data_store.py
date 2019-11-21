import logging
import os
import shutil
from abc import ABC, abstractmethod
from typing import TextIO

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseDataStoreAdapter(ABC):
    @staticmethod
    @abstractmethod
    def move(source: str, destination: str, recursive: bool = False) -> None:
        pass

    @staticmethod
    @abstractmethod
    def copy(source: str, destination: str, recursive: bool = False) -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete(path: str, recursive: bool = False) -> None:
        pass

    @staticmethod
    @abstractmethod
    def makedirs(path: str, exist_ok: bool = False, **kwargs) -> None:
        pass

    @staticmethod
    @abstractmethod
    def open(file: str, mode: str, **kwargs) -> TextIO:
        pass


class LocalDataStoreAdapter(BaseDataStoreAdapter):
    @staticmethod
    def move(source: str, destination: str, recursive: bool = False) -> None:
        shutil.move(src=source, dst=destination)

    @staticmethod
    def copy(source: str, destination: str, recursive: bool = False) -> None:
        if recursive:
            shutil.copytree(src=source, dst=destination)
        else:
            shutil.copy(src=source, dst=destination)

    @staticmethod
    def delete(path: str, recursive: bool = False) -> None:
        if recursive:
            shutil.rmtree(path=path)
        else:
            os.remove(path)

    @staticmethod
    def makedirs(path: str, exist_ok: bool = False, **kwargs) -> None:
        os.makedirs(path=path, exist_ok=exist_ok, **kwargs)

    @staticmethod
    def open(file: str, mode: str, **kwargs) -> TextIO:
        return open(file=file, mode=mode, **kwargs)