# Skripte README

Dieses Verzeichnis enthält kleine Hilfs‑Skripte für die Sandbox.

Aktuelles Script: `new_experiment.py`

Kurz: Erzeugt eine minimal‑struktur für ein neues Experiment:
- `projects/<kurzname>/README.md`
- `projects/<kurzname>/.env.example`

Beispielnutzung (lokal):

```bash
python projects/assistant-guides/scripts/new_experiment.py my-cool-experiment
```

Hinweise
- Das Script schreibt keine Secrets und hat keine externen Abhängigkeiten.
- Prüfe die erzeugten Dateien, passe Inhalte an und committe erst, wenn alles geprüft wurde.
