
# src/data_handling/json_api.py
"""
Data Handling & (Mock) API Examples

What this file covers
- JSON parsing & validation with helpful error messages
- File I/O using pathlib for cross-platform paths
- Mock API (fetch_posts) for offline demos
- Optional requests pattern without making a real network call
- Small utilities for real-world tasks (email normalization, filtering)

Demonstrates:
- JSON parsing/serialization with the stdlib `json`
- Reading/writing files safely using `pathlib`
- A mock API function that returns sample data (no network required)
- Optional usage of `requests` (if installed) to show typical patterns

Run: python src/data_handling/json_api.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any, Optional


# ---------- JSON PARSING EXAMPLE ----------
def parse_items_from_json(payload: str) -> List[Dict[str, Any]]:
    """
    Parse a JSON string that contains an 'items' list and return that list.
    Raises ValueError if structure is invalid.
    """
    try:
        obj = json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON payload: {e}") from e

    if not isinstance(obj, dict) or "items" not in obj or not isinstance(obj["items"], list):
        raise ValueError("Payload must be a dict with an 'items' list")

    return obj["items"]


# ---------- FILE I/O WITH PATHLIB ----------
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

ITEMS_PATH = DATA_DIR / "items.json"
ACTIVE_USERS_PATH = DATA_DIR / "active_users.json"


def write_json(path: Path, obj: Any, *, indent: int = 2) -> None:
    """Write Python object to JSON file with UTF-8 encoding."""
    path.write_text(json.dumps(obj, indent=indent), encoding="utf-8")


def read_json(path: Path) -> Any:
    """Read JSON file and return Python object."""
    return json.loads(path.read_text(encoding="utf-8"))


# ---------- MOCK API ----------
def fetch_posts() -> List[Dict[str, Any]]:
    """
    Simulate an API call: returns a list of post dicts.
    This avoids actual network use and keeps workshop runnable offline.
    """
    return [
        {"id": 1, "title": "Intro to Python", "tags": ["python", "training"]},
        {"id": 2, "title": "Using Requests", "tags": ["http", "python"]},
        {"id": 3, "title": "Data Handling Tips", "tags": ["json", "files"]},
    ]


# Optional: show typical 'requests' usage pattern (only if installed)
def optional_requests_demo(url: str) -> Optional[Dict[str, Any]]:
    """
    Demonstrates how you'd use 'requests' to fetch JSON.
    - Returns parsed JSON dict if successful
    - Returns None if requests isn't installed or call fails
    Note: In this workshop script, we do not actually make network calls.
    """
    try:
        import requests  # type: ignore
    except Exception:
        print("Requests not available in this environment.")
        return None

    try:
        # Example pattern (commented to avoid accidental network calls in workshop):
        # resp = requests.get(url, timeout=10)
        # resp.raise_for_status()
        # return resp.json()

        print(f"(Demo) Would perform GET {url} with requests here.")
        return {"demo": True, "url": url}
    except Exception as e:
        print(f"Requests demo failed: {e}")
        return None


# ---------- SMALL UTILITIES ----------
def normalize_emails(emails: List[str]) -> List[str]:
    """
    Deduplicate and normalize email strings (strip spaces, lowercase).
    Returns a sorted list of unique emails.
    """
    normalized = {e.strip().lower() for e in emails if e and isinstance(e, str)}
    return sorted(normalized)


def filter_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return only users with truthy 'active' key."""
    return [u for u in users if u.get("active")]


# ---------- DEMO MAIN ----------
def main() -> None:
    # 1) JSON parsing demo
    payload = '{"items":[{"id":1,"name":"widget"},{"id":2,"name":"gadget"}]}'
    items = parse_items_from_json(payload)
    print("Parsed items:", items)

    # 2) Write items to file, then read back
    write_json(ITEMS_PATH, items)
    loaded_items = read_json(ITEMS_PATH)
    print("Loaded items from file:", loaded_items)

    # 3) Mock API usage
    posts = fetch_posts()
    print("Mock posts:", posts)

    # 4) Users filtering & writing JSON
    users = [
        {"id": 1, "name": "Ann", "email": "ann@example.com", "active": True},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False},
        {"id": 3, "name": "Cara", "email": "  CARA@example.com  ", "active": True},
    ]
    active = filter_active_users(users)
    print("Active users:", active)

    # Normalize emails and show dedupe
    emails = [u["email"] for u in users]
    normalized_emails = normalize_emails(emails)
    print("Normalized emails:", normalized_emails)

    write_json(ACTIVE_USERS_PATH, active)
    print(f"Wrote active users to: {ACTIVE_USERS_PATH}")

    # 5) Optional requests demo (no network call performed)
    demo = optional_requests_demo("https://api.example.com/posts")
    print("Requests demo result:", demo)


if __name__ == "__main__":
    main()
