from abc import ABC, abstractmethod
from pydantic import BaseModel

class BaseTool(ABC):
    name: str
    description: str
    input_schema: type[BaseModel]

    @abstractmethod
    def execute(self, **kwargs):
        pass