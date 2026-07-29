from __future__ import annotations

import shutil
import os
from pathlib import Path

from gradio_client import Client


ROOT = Path(__file__).resolve().parents[1]
EXPORT_DIR = ROOT / "exports" / "ace-step-smoke"


def copy_audio(result) -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    candidates = result if isinstance(result, (list, tuple)) else [result]
    copied = False

    for item in candidates:
        if isinstance(item, str) and Path(item).exists():
            target = EXPORT_DIR / Path(item).name
            shutil.copy2(item, target)
            print(f"copied: {target}")
            copied = True
        else:
            print(f"result: {item!r}")

    if not copied:
        print("no local audio file was returned")


def main() -> None:
    client = Client(os.environ.get("ACE_STEP_URL", "http://127.0.0.1:7865"))
    result = client.predict(
        "wav",
        8,
        "cozy Korean cafe instrumental, soft felt piano, warm acoustic guitar, gentle lo-fi drums, soft bass, subtle gayageum texture, 78 BPM, warm, peaceful, minimal",
        "[instrumental]",
        8,
        7.0,
        "euler",
        "apg",
        6.0,
        "12345",
        0.5,
        0.0,
        3.0,
        True,
        False,
        True,
        "",
        0.0,
        0.0,
        False,
        0.5,
        None,
        "none",
        1.0,
        api_name="/__call__",
    )
    copy_audio(result)


if __name__ == "__main__":
    main()
