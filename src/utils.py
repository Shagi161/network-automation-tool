from datetime import datetime
from pathlib import Path

def now_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def ensure_output_dir() -> Path:
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    return out_dir

