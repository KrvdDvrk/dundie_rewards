"""Core module of dundie"""
import os
from csv import reader

from KrvdDvrkDundie.database import add_movement, add_person, commit, connect
from KrvdDvrkDundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database.

    >>> len(load('assets/people.csv'))
    2
    >>> load('assets/people.csv') [0][0]
    'J'
    """
    try:
        csv_data = reader(open(filepath))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)

        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people


def read(**query):
    """Read data from db and filters using query

    read(email="joe@doe.com")
    """
    db = connect()
    return_data = []
    for pk, data in db["people"].items():
        # Funcionamento para versões antes do python 3.8
        # query_dept = query.get("dept")
        # if query_dept != data["dept"]:
        #     continue

        # WALRUS / Assignment Expression - Funciona a partir do python 3.8
        if (dept := query.get("dept")) and dept != data["dept"]:
            continue

        if (email := query.get("email")) and email != pk:
            continue

        return_data.append(
            {
                "email": pk,
                "balance": db["balance"][pk],
                "last_movement": db["movement"][pk][-1]["date"],
                **data,
            }
        )
    return return_data


def add(value, **query):
    """Add value to each record on query"""
    people = read(**query)
    if not people:
        raise RuntimeError("Not Found")

    db = connect()
    user = os.getenv("USER")
    for person in people:
        add_movement(db, person["email"], value, user)
    commit(db)