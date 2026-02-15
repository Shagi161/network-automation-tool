import csv
from pathlib import Path
from typing import List, Dict

def save_csv_report(path: Path, rows: List[Dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "ip", "status"])
        writer.writeheader()
        writer.writerows(rows)

def save_summary(path: Path, rows: List[Dict[str, str]]) -> None:
    up = sum(1 for r in rows if r["status"] == "UP")
    down = sum(1 for r in rows if r["status"] == "DOWN")

    lines = [
        "Network Automation Tool - Summary",
        "--------------------------------",
        f"Total devices: {len(rows)}",
        f"UP: {up}",
        f"DOWN: {down}",
        "",
        "Devices DOWN:",
    ]
    for r in rows:
        if r["status"] == "DOWN":
            lines.append(f"- {r['name']} ({r['ip']})")

    path.write_text("\n".join(lines), encoding="utf-8")

