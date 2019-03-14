import typing
import sqlalchemy
import typesystem
from attr import attrs


class ModelField:
    def __init__(
        self,
        primary_key: bool = False,
        index: bool = False,
        unique: bool = False,
        **kwargs: typing.Any
    ) -> None:
        super().__init__(**kwargs)
        self.primary_key = primary_key
        self.index = index
        self.unique = unique

    def get_column(self, name: str) -> sqlalchemy.Column:
        column_type = self.get_column_type()
        return sqlalchemy.Column(
            name,
            column_type,
            primary_key=self.primary_key,
            nullable=self.allow_null,
            index=self.index,
            unique=self.unique,
        )

    def get_column_type(self) -> sqlalchemy.types.TypeEngine:
        raise NotImplementedError()


class String(ModelField, typesystem.String):
    def get_column_type(self):
        return sqlalchemy.String(length=self.max_length)


class Text(ModelField, typesystem.Text):
    def get_column_type(self):
        return sqlalchemy.Text()


class Integer(ModelField, typesystem.Integer):
    def get_column_type(self):
        return sqlalchemy.Integer()


class Float(ModelField, typesystem.Float):
    def get_column_type(self):
        return sqlalchemy.Float()


class Boolean(ModelField, typesystem.Boolean):
    def get_column_type(self):
        return sqlalchemy.Integer()
