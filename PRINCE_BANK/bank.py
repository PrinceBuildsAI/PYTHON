import json
import random
import string
from pathlib import Path
from datetime import datetime
import hashlib


class Bank:
    """Core banking logic for PRINCE BANK."""

    database = Path(__file__).parent / "data.json"

    @classmethod
    def _load_data(cls):
        if not cls.database.exists():
            return []

        try:
            with open(cls.database, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

    @classmethod
    def _save_data(cls, data):
        with open(cls.database, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def _hash_pin(pin):
        return hashlib.sha256(str(pin).encode()).hexdigest()

    @staticmethod
    def _generate_account_number():
        while True:
            chars = (
                random.choices(string.ascii_uppercase, k=3)
                + random.choices(string.digits, k=6)
            )
            random.shuffle(chars)
            account = "".join(chars)

            data = Bank._load_data()
            if not any(user["accountNo"] == account for user in data):
                return account

    @classmethod
    def create_account(cls, name, age, email, pin):
        name = name.strip()
        email = email.strip()

        if not name:
            return False, "Name cannot be empty.", None

        if age < 18 or age > 100:
            return False, "Age must be between 18 and 100.", None

        if not (pin.isdigit() and len(pin) == 4):
            return False, "PIN must contain exactly 4 digits.", None

        data = cls._load_data()

        if any(user["email"].lower() == email.lower() for user in data):
            return False, "An account with this email already exists.", None

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": cls._hash_pin(pin),
            "accountNo": cls._generate_account_number(),
            "balance": 0,
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        data.append(account)
        cls._save_data(data)

        public_account = account.copy()
        public_account.pop("pin")
        return True, "Account created successfully.", public_account

    @classmethod
    def authenticate(cls, account_no, pin):
        data = cls._load_data()
        hashed_pin = cls._hash_pin(pin)

        for user in data:
            if user["accountNo"] == account_no and user["pin"] == hashed_pin:
                return user

        return None

    @classmethod
    def deposit(cls, account_no, pin, amount):
        if amount <= 0 or amount > 10000:
            return False, "Deposit amount must be between ₹1 and ₹10,000."

        data = cls._load_data()
        user = cls.authenticate(account_no, pin)

        if not user:
            return False, "Invalid account number or PIN."

        for item in data:
            if item["accountNo"] == account_no:
                item["balance"] += amount
                break

        cls._save_data(data)
        return True, f"₹{amount:,.2f} deposited successfully."

    @classmethod
    def withdraw(cls, account_no, pin, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than ₹0."

        data = cls._load_data()
        user = cls.authenticate(account_no, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if user["balance"] < amount:
            return False, "Insufficient balance."

        for item in data:
            if item["accountNo"] == account_no:
                item["balance"] -= amount
                break

        cls._save_data(data)
        return True, f"₹{amount:,.2f} withdrawn successfully."

    @classmethod
    def get_details(cls, account_no, pin):
        user = cls.authenticate(account_no, pin)

        if not user:
            return None

        details = user.copy()
        details.pop("pin", None)
        return details

    @classmethod
    def update_details(cls, account_no, pin, name=None, email=None, new_pin=None):
        data = cls._load_data()
        user = cls.authenticate(account_no, pin)

        if not user:
            return False, "Invalid account number or PIN."

        for item in data:
            if item["accountNo"] == account_no:
                if name and name.strip():
                    item["name"] = name.strip()

                if email and email.strip():
                    if any(
                        x["email"].lower() == email.strip().lower()
                        and x["accountNo"] != account_no
                        for x in data
                    ):
                        return False, "This email is already linked to another account."
                    item["email"] = email.strip()

                if new_pin:
                    if not (new_pin.isdigit() and len(new_pin) == 4):
                        return False, "New PIN must contain exactly 4 digits."
                    item["pin"] = cls._hash_pin(new_pin)

                break

        cls._save_data(data)
        return True, "Account details updated successfully."

    @classmethod
    def delete_account(cls, account_no, pin):
        data = cls._load_data()
        user = cls.authenticate(account_no, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if user["balance"] != 0:
            return False, "Account must have ₹0 balance before deletion."

        data = [item for item in data if item["accountNo"] != account_no]
        cls._save_data(data)

        return True, "Account deleted successfully."
