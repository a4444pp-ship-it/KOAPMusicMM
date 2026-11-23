import os
from dotenv import load_dotenv

load_dotenv()


def _to_int(val: str | None, default: int = 0) -> int:
    if not val:
        return default
    try:
        return int(str(val).strip())
    except ValueError:
        return default


def _to_int_list(raw: str | None) -> list[int]:
    if not raw:
        return []
    out: list[int] = []
    for item in str(raw).replace(",", " ").split():
        try:
            out.append(int(item.strip()))
        except ValueError:
            continue
    return out


class Config:
    API_ID: int = _to_int(os.getenv("API_ID"), 0)
    API_HASH: str = os.getenv("API_HASH", "").strip()
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "").strip()
    SESSION_STRING: str = os.getenv("SESSION_STRING", "").strip()
    MONGO_URL: str = os.getenv("MONGO_URL", "").strip()
    OWNER_ID: int = _to_int(os.getenv("OWNER_ID"), 0)
    SUDO_USERS: list[int] = list(set([OWNER_ID] + _to_int_list(os.getenv("SUDO_USERS")))) if OWNER_ID else _to_int_list(os.getenv("SUDO_USERS"))
    LOG_GROUP_ID: int = _to_int(os.getenv("LOG_GROUP_ID"), 0)
    AOI_API_BASE: str = os.getenv("AOI_API_BASE", "https://host-repository.vercel.app").rstrip("/")
    AOI_API_KEY: str = os.getenv("AOI_API_KEY", "").strip()
    DEFAULT_THUMB: str = os.getenv("DEFAULT_THUMB", "cache/default_thumb.png").strip()


config = Config()
