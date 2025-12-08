
# src/oop/models.py
"""
OOP Models: Classic class vs @dataclass, type hints, equality/hash, and simple utilities.

What this file demonstrates:
- A classic class with explicit methods and custom equality/hash.
- A dataclass with type hints, computed field (fingerprint), and a to_dict helper.
- Utilities to filter active users and dedupe by id.
- An optional Pydantic model (UserModel) for runtime validation and conversion to UserDC.
- A _demo() function you can run to see everything working end-to-end.

Run this file with:
    python src/oop/models.py
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any, Iterable
from hashlib import sha256


# ---------- Classic class ----------
class User:
    """
    Classic Python class:
    - Explicit constructor
    - Custom methods (__repr__, __eq__, __hash__)
    - Lightweight business logic
    """

    def __init__(self, id: int, name: str, email: str, active: bool = True) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    def domain(self) -> str:
        """Return the email domain (part after '@')."""
        return self.email.split("@")[-1]

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a plain dict (useful for JSON, logging, etc.)."""
        return {"id": self.id, "name": self.name, "email": self.email, "active": self.active}

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', active={self.active})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        # Consider users equal if they share the same unique id
        return self.id == other.id

    def __hash__(self) -> int:
        # Hash based on id to allow set/dict usage
        return hash(self.id)


# ---------- Dataclass variant ----------
@dataclass(eq=True, frozen=False)
class UserDC:
    """
    Dataclass version:
    - Automatic __init__, __repr__, __eq__ (controlled via decorator args)
    - Type hints for clarity
    - Extra computed fields or methods can be added
    """
    id: int
    name: str
    email: str
    active: bool = True
    # Example of a non-init field (computed later)
    fingerprint: Optional[str] = field(default=None, init=False, repr=False)

    def domain(self) -> str:
        return self.email.split("@")[-1]

    def compute_fingerprint(self) -> str:
        """
        Compute a stable fingerprint (not security-grade; example only).
        """
        fp = sha256(f"{self.id}:{self.email}".encode("utf-8")).hexdigest()
        self.fingerprint = fp
        return fp

    def to_dict(self) -> Dict[str, Any]:
        """
        Use dataclasses.asdict for convenience, but exclude None fields if you want:
        """
        payload = asdict(self)
        # Optionally drop None values:
        return {k: v for k, v in payload.items() if v is not None}


# ---------- Collection utilities ----------
def active_users(users: Iterable[User | UserDC]) -> list[User | UserDC]:
    """Filter only active users from a sequence of classic or dataclass user objects."""
    return [u for u in users if getattr(u, "active", False)]


def dedupe_users_by_id(users: Iterable[User | UserDC]) -> list[User | UserDC]:
    """
    Deduplicate users by id while preserving order of first occurrence.
    Works for both User and UserDC since both expose .id.
    """
    seen: set[int] = set()
    result: list[User | UserDC] = []
    for u in users:
        if u.id not in seen:
            seen.add(u.id)
            result.append(u)
    return result


# ---------- Optional: Pydantic model for runtime validation ----------
try:
    from pydantic import BaseModel, EmailStr

    class UserModel(BaseModel):
        id: int
        name: str
        email: EmailStr
        active: bool = True

        def domain(self) -> str:
            return self.email.split("@")[-1]

    def to_user_dc(model: UserModel) -> UserDC:
        """Convert validated UserModel to UserDC."""
        return UserDC(id=model.id, name=model.name, email=str(model.email), active=model.active)

except Exception:
    # Pydantic is optional; skip if not installed.
    UserModel = None  # type: ignore
    def to_user_dc(model):  # type: ignore
        raise RuntimeError("Pydantic not installed; cannot convert UserModel -> UserDC")


# ---------- Demonstration ----------
def _demo() -> None:
    print("=== Classic User ===")
    u1 = User(1, "Ann", "ann@example.com")
    u2 = User(2, "Bob", "bob@example.com", active=False)
    print(u1, "domain=", u1.domain())
    print(u2, "domain=", u2.domain())
    print("u1 == User(1, 'X', 'x@x.com')? ->", u1 == User(1, "X", "x@x.com"))

    print("\n=== Dataclass UserDC ===")
    d1 = UserDC(3, "Cara", "cara@example.com")
    d2 = UserDC(4, "Dan", "dan@example.com", active=False)
    print(d1, "domain=", d1.domain())
    print(d2, "domain=", d2.domain())
    print("Fingerprint for d1:", d1.compute_fingerprint())
    print("to_dict(d1):", d1.to_dict())

    print("\n=== Utilities ===")
    mixed = [u1, u2, d1, d2, User(1, "Ann-dup", "ann@dup.com")]
    print("Active:", active_users(mixed))
    print("Dedupe by id:", dedupe_users_by_id(mixed))

    print("\n=== Optional: Pydantic ===")
    if UserModel:
        try:
            model = UserModel(id=10, name="Eve", email="eve@example.com")
            print("Validated model:", model)
            d = to_user_dc(model)
            print("Converted to UserDC:", d, "domain=", d.domain())
        except Exception as e:
            print("Pydantic validation error:", e)
    else:
        print("Pydantic not installed; skipping model demo.")


if __name__ == "__main__":
    _demo()
