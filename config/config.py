from pathlib import Path

# -----------------------------
# PROJECT ROOT
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# PATHS
# -----------------------------
DATA_PATH = BASE_DIR / "data" / "sales.txt"

OUTPUT_DIR = BASE_DIR / "output"

DATABASE_PATH = (
    BASE_DIR
    / "database"
    / "sales.db"
)