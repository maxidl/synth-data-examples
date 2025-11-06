# WeTab — Praxis-Guide für Nutzung, Anpassung und Einschätzung

Kurzüberblick
- WeTab ist ein linux-basiertes Touch-Tablet, das eher einem Netbook nahekommt (Netbook-Hardware) und ein offenes System bietet.
- Stärken: schnelle Boot-Zeiten, echtes Linux unter der Haube, viele Anschlüsse und Aufrüstmöglichkeiten.
- Schwächen: begrenzte, teils unausgereifte native Anwendungen, browserseitige Einschränkungen, virtuelle Tastatur/Touch-Unterstützung kann OS-abhängig variieren.

Hardware-Eigenschaften
- Gehäuse/Verarbeitung: liegt gut in der Hand, solide verarbeitet.
- Display: Touchscreen mit guter Ansprechbarkeit; Blickwinkelabhängig (bei flacher Betrachtung Farb-/Kontraständerungen).
- Ton/Video: Flash- und Videowiedergabe möglich; Lüfter läuft bei Last an (in der Regel leise).
- Akku: ~5 Stunden typischer Laufzeit (abhängig von Nutzung).
- Erweiterbarkeit: RAM und SSD sind aufrüstbar (vorsichtiges Vorgehen empfohlen).
- Anschlüsse: mehrere Ports vorhanden — ermöglicht Verbindung mit Peripherie und Netzwerken.

Betriebssystem und Benutzeroberfläche
- Standard-OS: eine MeeGo-Variante (WeTab-OS) mit eigenem, innovativem UI-Konzept.
  - Sehr kurze Boot-Zeiten.
  - Viele UI-Elemente für Fingereingabe und Multitouch ausgelegt.
  - Native App-Auswahl ist begrenzt; vielfach werden Adobe-Air-Anwendungen eingesetzt.
  - Browser-Eigenarten: keine integrierte Werbeblocker-Unterstützung, Lesezeichen werden auf dem Desktop abgelegt statt in einer internen Linkverwaltung.
- Freiheit: echtes Linux unter der Haube erlaubt Erweiterungen und Installation alternativer OS.

Vorzüge im Alltag
- Schnelles Hochfahren und reaktionsfreies UI sorgen für „Wow“-Effekt bei Präsentationen (z. B. Bildbetrachter auf der Couch).
- Ideal für Surfen, E‑Mail und kürzere Texte unterwegs.
- Voller Linux-Zugang: Root-Shell, Midnight-Commander, SSH- und SAMBA-Zugriffe möglich.
- Physische Peripherie: Tastatur und Maus per USB anschließbar — macht das Gerät auch als stationären Schreibtischrechner brauchbar.

Bekannte Einschränkungen und Kritikpunkte
- Vergleich mit iPad wenig sinnvoll — andere Hardware- und Software-Philosophie.
- Virtuelle Tastatur: unter alternativen Systemen (z. B. Kubuntu) kann die Bildschirmtastatur nicht automatisch einblenden und erfordert manuelles Aufrufen.
- Touchfunktionen: Scrollen per Touch und Multitouch sind unter anderen Linux-Distributionen nicht zwingend vollständig unterstützt.
- App-Ökosystem: wenige „echte“ native Anwendungen, einige mitgelieferte Apps unausgereift.

Alternative OS (Erfahrungen mit Kubuntu)
- Vorteile: vertrauter Desktop-Browser, bekannte Linux-Anwendungen.
- Nachteile beobachtet:
  - Kein Touch-Scrollen im Browser (nervig beim Surfen).
  - Multitouch kann ausfallen.
  - On-Screen-Tastatur muss ggf. manuell gestartet werden.
- Fazit: Kubuntu läuft grundsätzlich, ist für Touch-Benutzung aber nicht optimal ohne zusätzliche Anpassungen.

Praktische Schritte vor Systemwechseln
1. Backup erstellen
   - Benutzerdateien, Einstellungen und ggf. Partitionstabelle sichern.
2. Informationsbeschaffung
   - Community-Wiki/Forum konsultieren: Hardware-spezifische Hinweise und fertige Images finden.
3. Recovery-Image bereithalten
   - Recovery-Image zum Zurücksetzen auf Auslieferungszustand herunterladen und testen.
4. Bootmedium erstellen
   - Bootfähigen USB-Stick oder SD-Karte mit gewünschtem Image erstellen.
5. Installation durchführen
   - Anleitung aus Community-Wiki befolgen; auf Treiber-/Touch-Unterstützung achten.
6. Nacharbeit
   - Touch- und virtuelle Tastatur-Lösungen konfigurieren; ggf. zusätzliche Treiber/Daemonen installieren.

Tipps für besseren Touch-/Tastaturkomfort
- Externe Tastatur/Maus anschließen für längere Texte.
- Wenn Kubuntu (oder andere Distros) verwendet werden: nach Touch-Treiberpaketen, On‑Screen-Keyboard-Daemons (z. B. onboard, florence) sowie xinput- oder libinput-Konfigurationen suchen.
- Für Browsing: alternative Browser installieren, Add‑On-Unterstützung prüfen (AdBlocker, Bastel-Lesezeichen-Tools).
- Bei Ausfall von Multitouch: Community-Patches und Kernel-Module prüfen.

Netzwerk & Remote-Nutzung
- SSH einrichten für Fernzugriff.
- SAMBA für Dateifreigaben im Heimnetz konfigurieren.
- Konsole wechseln: STRG+ALT+F1 (virtuelle Konsole) funktioniert wie bei üblichen Linux-Systemen.

Fehlerbehebung / Recovery
- Zurücksetzen auf Auslieferungszustand mit Recovery-Image möglich — vorher unbedingt Daten sichern.
- Bei Problemen mit Touch oder Tastatur: Logs (/var/log/*, dmesg) prüfen, Input-Geräte mit xinput auflisten.
- Community-Foren und Wiki sind oft die beste Quelle für gerätespezifische Lösungen.

Für wen ist das Gerät geeignet?
- Empfohlen für Nutzer, die:
  - mit Linux vertraut sind oder bereit sind, sich einzuarbeiten,
  - ein offenes, erweiterbares System wollen,
  - das Tablet primär zum Surfen, Mailen und Präsentieren nutzen,
  - bei Bedarf an externe Eingabegeräte anschließen können.
- Weniger geeignet für Nutzer, die:
  - ein geschlossenes App-Ökosystem oder native Apps wie beim iPad erwarten,
  - sehr viel und bequem lange Texte ohne externe Tastatur tippen möchten.

Kurzes Fazit
- WeTab ist ein interessantes, offenes Tablet mit Netbook-Charakter: solide Hardware, echtes Linux und Anpassbarkeit sprechen für das Gerät. Einschränkungen bestehen vor allem bei App-Auswahl, Browserfunktionen und bei der Touch-Unterstützung unter alternativen Distributionen. Als mobiler Begleiter für Linux-affine Anwender und für Nutzer, die Kontrolle über ihr System schätzen, stellt es eine empfehlenswerte Option dar.

Häufige Fragen (Kurz)
- Lässt sich das System zurücksetzen? Ja — Recovery-Image kann auf Auslieferungszustand zurücksetzen.
- Kann ich Android-Apps nutzen? Nicht out-of-the-box; Unterstützung für Android-Apps wäre eine zukünftig mögliche (aber nicht garantierte) Erweiterung.
- Wie lange hält der Akku? Etwa 5 Stunden im typischen Einsatz.
- Ist Multitouch voll nutzbar? Unter dem Standard-WeTab-OS: ja; unter alternativen OS kann Multitouch eingeschränkt sein.

Weiterführende Handlungsempfehlung
- Vor Kauf: Prüfen, ob die typische Nutzung (Surfen, E‑Mail, Präsentation) mit den bekannten Einschränkungen kompatibel ist.
- Bei Kauf gebrauchter Geräte: auf Vollständigkeit von Recovery-Image und Zugang zu Community-Ressourcen achten.
- Wer maximale Touch-Integration will, sollte zunächst die WeTab-OS-Funktionalität testen; wer bestimmte Desktop-Programme benötigt, kann alternative Distributionen probieren, muss aber mit Mehraufwand beim Touch-Setup rechnen.