import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # fallback if python-dotenv is not installed
    def load_dotenv(*args, **kwargs):  # type: ignore[func-returns-value]
        return False

BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env in the project root if it exists
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "project_lms")

IMG_DIR = BASE_DIR / "img"

LOGO_SMALL = IMG_DIR / "logo-small.png"
MAIN_IMAGE = IMG_DIR / "img2.png"
