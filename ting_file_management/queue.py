"""Linter"""
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    """Linter"""

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self.queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
