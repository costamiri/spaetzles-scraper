# spaetzles-scraper

Tool zur automatisierten Gewinnung der abgegebenen Tipps im Spätzle(s)-Tippspiel im transfermarkt.de-Forum. 

`spaetzle-scraper.py` lädt die einzelnen Posts aus dem angegebenen Thread in eine json-Datei.<br>
`extract.py` extrahiert aus der json-Datei die einzelnen Tipps und erzeugt eine CSV-Datei.
`member_list.txt` gibt die Reihenfolge der Teilnehmenden an (Leerzeilen und mit "#" beginnende Zeilen werden nicht beachtet)

## Abhängigkeiten

- Python 3.x
- folgende Python-Module:
  - bs4
  - requests
  - parse

## Benutzung

1. `member_list.txt` vorbereiten: Alle Teilnehmenden zeilenweise eintragen. Kommentare können mit einem `#` am Zeilenanfang hinzugefügt werden. Idealerweise sind die Teilnehmenden bereits nach Liga und Alphabet sortiert, um später Übersicht zu wahren. Hinweis: Darauf achten, die Usernamen korrekt zu schreiben, abgegebene Posts werden sonst nicht erfasst :'(
2. Kommandozeile öffnen ("cmd" in Windows-Suche) und zum Speicherort navigieren ("cd")
3. `python spaetzle-scraper.py`. Nach Aufforderung die URL des Threads (Erste Seite!) eingeben. Anschließend werden die Usernamen und Zeitpunkte der eingelesenen Posts ausgegeben.
4. `python extract.py`. Am Schluss werden Nichttipper ausgegeben sowie die Teilnehmer, die einen Beitrag verfassten aber kein Tipp erkannt werden konnte. Dies bitte manuell nachprüfen!
5. CSV öffnen und übertragen.
6. Lücken nachprüfen. Einzelne Tipps wurden möglicherweise nicht erkannt und müssen manuell nachgetragen werden. Hilfreich ist es dazu in der Json-Datei `forumposts.json` nach dem Teilnehmer zu suchen.
