"""Append today's automated journal entry once, using the India calendar date."""

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main():
    today = datetime.now(ZoneInfo("Asia/Kolkata")).date().isoformat()
    journal = Path(__file__).resolve().parents[1] / "activity.log"
    entries = journal.read_text(encoding="utf-8").splitlines() if journal.exists() else []
    if any(line.split(" | ", 1)[0] == today for line in entries):
        print(f"Already recorded {today}; no update needed.")
        return
    entries.append(f"{today} | automated daily activity")
    journal.write_text("\n".join(entries) + "\n", encoding="utf-8")
    print(f"Recorded {today}.")


if __name__ == "__main__":
    main()
