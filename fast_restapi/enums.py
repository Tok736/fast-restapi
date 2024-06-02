from enum import Enum


class SchemaType(Enum):
    create_schema: str = "create_schema"
    read_schema:   str = "read_schema"
    update_schema: str = "update_schema"
