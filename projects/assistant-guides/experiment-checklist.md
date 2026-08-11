# Experiment Checklist (Entwurf)

Kurz: Eine kompakte, leicht zu nutzende Checkliste, damit kleine Experimente in der Team‑Sandbox sicher, reproduzierbar und verantwortbar abgelegt werden. Lies sie in 1–2 Minuten vor dem ersten Commit.

## 1) Kurz vor dem Start (so geht's schnell)
- Branch anlegen: `feature/<kurzname>` oder `experiment/<kurzname>`.
- Lege `projects/<kurzname>/README.md` an mit:
  - 1–2 Sätzen Zweck
  - Quickstart: 1–3 Befehle zum Install/Run
- Notiere die erwartete Lebensdauer (z. B. kurzlebig / weiterverwendbar).

## 2) Sicherheit — unverhandelbar, kurz
- Keine Secrets in das Repo committen (API‑Keys, Passwörter, Zertifikate).
- Stattdessen: `.env.example` mit Platzhaltern committen; echte Werte lokal via `.env` setzen und gitignore‑en.
- Wenn ein Secret versehentlich committed wurde: Credential sofort rotieren/ungültig machen und Repo‑Owner informieren.
- Praktischer Check vor Push: ein kurzes grep (z. B. `git grep -n "API_KEY\|SECRET\|PASSWORD"`) oder ein einfacher pre‑commit‑Hook.

Hinweis zu Tools:
- Empfohlen & ausreichend für kleine Experimente: einfache lokale Prüfung + GitHub Secret Scanning (sofern im Repo aktiviert).
- Optional: git-secrets als pre‑commit Hook, wenn du öfter mit Secrets arbeitest.
- In der Sandbox meist nicht nötig: schwere Scans wie truffleHog — nur bei hohem Risiko einsetzen.

## 3) Reproduzierbarkeit — praktisch und knapp
- Dokumentiere Install + Run + ein Smoke‑Test (1–3 Befehle) in der Projekt‑README.
- Abhängigkeiten: `requirements.txt` / `package.json` / `Dockerfile` wenn sinnvoll. Lockfiles sind hilfreich, aber nicht zwingend für Ein‑Datei‑Protos.
- Test‑Schnellcheck: mindestens ein manueller Smoke‑Schritt in der README (z. B. `python main.py --smoke`).

## 4) Lizenz & Quellen — konservativ handeln
- Wenn du Code übernimmst: immer Quelle (Link) und Lizenz angeben.
- Bei eigener Arbeit: gib eine Lizenz an (empfehlung: MIT für kleine Snippets), oder verweise auf die Repo‑Lizenz.
- Bei Unsicherheit über Lizenz oder Herkunft: nicht einfach übernehmen — öffne ein Issue und markiere es zur Klärung (oder kontaktiere Repo‑Owner/Legal).
- Hinweis: Das hier ist keine Rechtsberatung; bei rechtlichen Zweifeln Legal/Repo‑Owner konsultieren.

## 5) Datenschutz / vertrauliche Daten — kurz & klar
- Keine echten personenbezogenen oder vertraulichen Produktionsdaten verwenden.
- Nutze synthetische oder anonymisierte Datensätze. Wenn reale Daten nötig sind, vorher Data‑Protection/Legal kontaktieren und dokumentieren, wie die Daten geschützt werden.

## 6) PR & Review — minimal sinnvoll
- PR‑Titel: `[experiment] <kurze Beschreibung>`
- PR‑Beschreibung: Zweck, Quickstart (1–3 Befehle), bekannte Risiken (z. B. Daten/Secrets), gewünschte Reviewer.
- Halte PRs klein — konzentrierte Änderungen werden schneller reviewt.

## 7) CI / Workflows — nur bei Bedarf
- Secrets für Actions immer über GitHub Secrets verwalten.
- Wenn du CI hinzufügst: minimal halten und vor dem Merge prüfen.

## 8) Aufräumen / Archiv
- Wenn ein Experiment > 6 Monate inaktiv ist: archivieren oder mit `archived` kennzeichnen (Repo‑Owner/Team entscheidet).
- Kurze Abschlussnotiz: wichtigste Erkenntnis + Weiterverwendungs‑Hinweis.

## 9) Kontakt / Hilfe
- Trage im Projekt‑README eine Kontaktperson/Handle ein (z. B. `@Ca1llech`) oder verweise auf das Team‑Channel.
- Bei Unsicherheiten: Issue öffnen und passende Tags (`security`, `legal`) hinzufügen.

---

Kurzformat (zum Kopieren in PR-Template)
- Purpose (1–2 Sätze)  
- Quickstart (Install + Run)  
- [ ] Keine Secrets committed  
- [ ] Reproduzierbar (Install + Smoke‑Test)  
- [ ] Lizenz/Quellen geprüft oder Issue offen  
- Reviewer: @
