# Quickstart Demo: experiment/quickstart-demo

Kurz: Kleines Beispiel‑Projekt, das zeigt, wie ein Experiment strukturiert sein kann. Nur Demo‑Inhalte — keine echten Daten oder Secrets.

Struktur (Beispiel)

```
projects/experiment-quickstart-demo/
├─ README.md
├─ .env.example
├─ main.py          # kleines Demo‑Script (optional)
├─ requirements.txt # falls nötig
```

Kurzer Quickstart (lokal):

1) Falls vorhanden: Abhängigkeiten installieren

```bash
# python
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

2) Smoke‑Test (Beispiel)

```bash
python main.py --smoke
```

Hinweise
- Keine Secrets committen — nutze `.env.example` als Vorlage.
- Kontakt: `@Ca1llech` (oder Team‑Channel) bei Fragen.
- Dieses Demo ist bewusst minimal — passe es nach Bedarf an.
