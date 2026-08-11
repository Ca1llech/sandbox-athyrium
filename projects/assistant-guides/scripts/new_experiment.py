"""projects/assistant-guides/scripts/new_experiment.py

Ein kleines Hilfs-Skript, das eine konsistente Ordnerstruktur für ein neues Experiment erzeugt.

Nutzung:
  python new_experiment.py <kurzname>

Es erzeugt:
  projects/<kurzname>/README.md   (mit Zweck, Quickstart-Platzhalter)
  projects/<kurzname>/.env.example

Keine sensiblen Daten werden geschrieben. Dieses Skript ist für die lokale Nutzung gedacht.
"""

from pathlib import Path
import sys

TEMPLATE_README = """# {title}

Kurz: Zweck des Experiments (1–2 Sätze).

Quickstart

```bash
# 1) Abhängigkeiten installieren
# 2) Beispiel: python main.py --smoke
```

Kontakt: @Ca1llech
"""

ENV_EXAMPLE = """# Beispiel .env
# Trage hier keine echten Secrets ein — nutze lokale Umgebungsvariablen.
API_KEY=
DB_URL=
"""


def create_experiment(name: str):
    base = Path("projects") / name
    readme_path = base / "README.md"
    env_path = base / ".env.example"

    base.mkdir(parents=True, exist_ok=True)

    if readme_path.exists():
        print(f"README bereits vorhanden: {readme_path}")
    else:
        readme_path.write_text(TEMPLATE_README.format(title=name))
        print(f"Angelegt: {readme_path}")

    if env_path.exists():
        print(f".env.example bereits vorhanden: {env_path}")
    else:
        env_path.write_text(ENV_EXAMPLE)
        print(f"Angelegt: {env_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python new_experiment.py <kurzname>")
        sys.exit(1)
    name = sys.argv[1]
    create_experiment(name)
