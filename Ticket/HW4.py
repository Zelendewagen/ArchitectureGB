import datetime
import decimal
from typing import Any


class Ticket:
    _id: int
    _departure_zone: int
    _arrival_zone: int
    _route_number: int
    _departure_time: datetime
    _arrival_time: datetime
    _buyer_id: int
    _is_used: bool
    _price: decimal
    _place: str

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)


class User:
    _id: int
    _name: str
    _tickets: [Ticket]
    _login: str
    _password_hash_code: int
    _account_id: int

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)


class Account:
    _user_account_id: int
    _balance: decimal

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)
