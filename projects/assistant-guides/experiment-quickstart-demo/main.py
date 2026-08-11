"""experiment-quickstart-demo/main.py

Kleines Demo‑Script für den Quickstart.
Verwendung:
  python main.py --smoke

Wenn --smoke übergeben wird, gibt es eine kurze Erfolgsmeldung aus.
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Quickstart demo script")
    parser.add_argument("--smoke", action="store_true", help="Run smoke test")
    args = parser.parse_args()

    if args.smoke:
        print("SMOKE OK: Demo läuft in der Sandbox")
        sys.exit(0)
    else:
        print("Nutze --smoke für einen schnellen Funktionstest")
        sys.exit(0)


if __name__ == "__main__":
    main()
