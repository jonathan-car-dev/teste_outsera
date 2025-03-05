from .parser import Parser
from .database import Database
from .file_retriever import FileDataRetriever
from .log import print_log


database_instance = Database()

def get_database_instance():
    return database_instance

__all__ = (
    'Parser',
    'get_database_instance',
    'FileDataRetriever',
    'print_log'
)