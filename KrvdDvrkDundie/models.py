from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from KrvdDvrkDundie.utils.email import check_valid_email
from KrvdDvrkDundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @field_validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self):
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime = Field(default_factory=lambda: datetime.now().isoformat())
    actor: str
    value: Decimal

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class User(BaseModel):
    person: Person
    password: str = Field(default_factory=generate_simple_password)

    class config:
        json_encoders = {Person: lambda p: p.pk}


if __name__ == "__main__":
    p = Person(pk="bruno@g.com", name="Bruno", dept="Sales", role="NA")
    print(p)
    print(p.json())

    b = Balance(person=p, value=100)
    print(b.json(models_as_dict=False))

    m = Movement(person=p, date=datetime.now(), actor="sys", value=10)
    print(m.json(models_as_dict=False))

    u = User(person=p)
    print(u.json(models_as_dict))


# import json

# from KrvdDvrkDundie.database import connect

# db = connect()


# for pk, data in db["people"].items():
#     p = Person(pk=pk, **data)


# print(p)
# print(p.model_dump_json())


# balance = Balance(person=p, value=Decimal(100))
# print(balance)
# print(balance.model_dump_json())
