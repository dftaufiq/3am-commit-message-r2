#!/usr/bin/env python3
"""The 3 AM Commit Message (R2 resubmit) — make.fun entry.

Writes one commit message, the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM, to /output/entry.txt.

The line is a literal in this file: deterministic, no network, no secrets,
no environment reads. Two runs produce byte-identical output.

Structure (2-beat + reveal, per the winning one-liner pattern): beat 1 is
the good behaviour — revert the deploy and email all 12,731 customers an
apology; the reveal, in the final clause, is that the apology email was sent
FROM the production database, which is now also down. The fix caused a
second outage: an apology with a body count, reported as a status update
inside a commit message. Selected as champion (9-0) in a 10-variant internal
pairwise tournament; see variants-r2.md in the build folder.
"""

import os

ENTRY = "fix(prod): reverted the 3 AM deploy and emailed all 12,731 customers an apology; the email was sent from the production database, which is now also down"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
