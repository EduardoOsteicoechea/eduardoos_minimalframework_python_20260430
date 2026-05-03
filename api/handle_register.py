import html
import sqlite3
import bcrypt  # type: ignore
from urllib.parse import parse_qsl
from pydantic import BaseModel, EmailStr, Field, ValidationError
from database.create_user import create_user


class UserRegistration(BaseModel):
    username: str = Field(strip_whitespace=True, min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)


def handle_register(body):
    print(f"[METHOD: handle_register]:")
    print(f"    body: {body}")

    parsed_body = dict(parse_qsl(body))

    if not parsed_body.get("submit"):
        raise ValueError("The request wasn't submitted.")

    try:
        clean_data = UserRegistration(**parsed_body)
    except ValidationError as e:
        print(f"    -> [!] Validation Error: {e}")
        return "Error: Invalid data provided."

    safe_username = html.escape(clean_data.username)

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(
        clean_data.password.encode("utf-8"), salt).decode("utf-8")

    print(f"    -> Ready for DB. Username: {safe_username}, Email: {clean_data.email}")

    try:
        create_user(safe_username, clean_data.email, hashed_password)
    except sqlite3.IntegrityError as e:
        print(f"    -> [!] Database Integrity Error: {e}")
        return "Error: That email is already registered."
    except Exception as e:
        print(f"    -> [!] Database Error: {e}")
        return "Error: Could not complete registration at this time."

    print(f"    parsed_body: {parsed_body}")

    return "Registration successfully processed!"
