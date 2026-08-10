# sandbox-athyrium

Eine gemeinsame Sandbox für das Team — zum Ausprobieren, Prototyping und Teilen kleiner Experimente.

## Ziel
Dieses Repository dient als zentrale Spielwiese, in der Teammitglieder schnell Ideen testen, Proof-of-Concepts ablegen und wiederverwendbare Snippets sammeln können. Die Sandbox ist kein Produkt-Repository; sie soll schnelle Iteration und Wissensaustausch fördern.

## Grundsätze
- Kurzlebige Experimente sind willkommen — dokumentiere wichtige Erkenntnisse.
- Beiträge sollten so angelegt werden, dass andere Teammitglieder sie nachvollziehen können.
- Keine sensiblen Daten oder Zugangsdaten ins Repository einchecken.

## Repository-Struktur (Empfehlung)
- projects/<name> — einzelnes Experiment oder Prototype (jeweils eigenständiges Unterverzeichnis)
- docs — kurze Anleitungen, Entscheidungen, Notizen
- scripts — Hilfs-Skripte zum lokalen Testen
- examples — kleine, wiederverwendbare Codebeispiele

Beispiel:
- projects/fast-proto-1/README.md
- projects/fast-proto-1/main.py

## Wie man ein neues Experiment anlegt
1. Lege ein neues Verzeichnis unter `projects/` an, z. B. `projects/<kurzer-name>`.
2. Füge eine kurze README im Verzeichnis hinzu (Zweck, Setup, wie testen).
3. Wenn nötig: `requirements.txt` / `package.json` / `Dockerfile` für reproduzierbare Tests.
4. Öffne einen Pull Request mit einer kurzen Beschreibung der Änderung.

## Branch- und PR-Konvention (Empfehlung)
- Branchname: `feature/<kurz-beschreibung>` oder `experiment/<kurz-beschreibung>`
- Commit-Messages: kurz und prägnant (z. B. `add: erster prototype für X`)
- PR-Titel: `[experiment] <kurze beschreibung>`
- Bei experimentellen Beiträgen ist ein Review erwünscht, aber nicht zwingend — markiere im PR, wenn es rein explorativ ist.

## Laufzeit & Tests
Je nach Projekt unterschiedlich. Füge im Projekt-Ordner Hinweise hinzu:
- Python: `python -m venv .venv && .venv/bin/pip install -r requirements.txt`
- Node: `npm install` bzw. `pnpm install`
- Container: `docker build -t <name> .` und `docker run --rm -it <name>`

## Dokumentation & Wissen teilen
- Kurze Ergebnisse und Erkenntnisse in `docs/` oder in der Projekt-README dokumentieren.
- Wichtige Learnings gern als Issue oder Discussion verlinken.

## Sicherheit und sensible Daten
- Niemals Passwörter, API-Keys, Zertifikate oder andere Geheimnisse einchecken.
- Nutze `.env`-Vorlagen (`.env.example`) für lokale Konfigurationen, aber committe keine echten Werte.

## Mitmachen
1. Fork/Branch erstellen.
2. Änderungen in einem eigenen Branch commiten.
3. PR öffnen mit kurzer Beschreibung (Zweck, wie testen).
4. Reviewer zuweisen (wenn du unsicher bist, weise eine Kollegin oder einen Kollegen zu).

## Verantwortlichkeiten
- Jede(r) Beitragende ist für die Lesbarkeit und kurze Dokumentation seines Experiments verantwortlich.
- Repo-Owner kann inaktive Experimente archivieren oder in ein `archive/`-Verzeichnis verschieben.

## Lizenz
Trage hier die gewünschte Lizenz ein (z. B. MIT). Wenn keine Lizenz angegeben ist, gelten die Standardurheberrechte.

## Kontakt
Bei Fragen oder Abstimmungen: Issue öffnen oder im Team-Chat (z. B. Slack) nachfragen.
