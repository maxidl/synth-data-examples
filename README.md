# synth-data-examples

## Input data
The input data consists of 10 test documents. 5 English from fineweb-edu, and 5 German from fineweb-2.

## Output data

Generated files are written to `examples/synthetic_data/<prompt-key>/<filename>.md`. Each file corresponds to an input document from `examples/source_documents`, transformed according to the selected prompt.

### summary
Produces a long-form summary of the source document in the same language as the input. The output avoids referencing the original document explicitly and is formatted as markdown.

### qa
Creates 10 self-contained question–answer pairs in the same language as the input text. The result is formatted in markdown for easy reading and downstream use.

### edu_material
Transforms the source text into stand-alone educational learning material in the same language. The content is designed to be directly usable for teaching or studying, with markdown formatting.

### exams
Generates five exam variants (different styles) with solutions, all in the input language. Each exam includes a mix of easy, medium, and hard tasks and is self-contained in markdown.

### active_reading
Interleaves the original text with guided active-reading prompts and reflections to support comprehension. The output simulates a reader’s thought process before, during, and after reading, formatted in markdown.

<details>
<summary>Deutsch: Ausgabedaten</summary>

Die generierten Dateien werden in `examples/synthetic_data/<prompt-key>/<filename>.md` abgelegt. Jede Datei entspricht einem Eingabedokument aus `examples/source_documents` und wurde gemäß dem ausgewählten Prompt transformiert.

### summary
Erzeugt eine ausführliche Zusammenfassung des Quelldokuments in derselben Sprache wie der Input. Die Ausgabe verweist nicht explizit auf das Original und ist als Markdown formatiert.

### qa
Erstellt 10 in sich geschlossene Frage–Antwort‑Paare in der Sprache des Eingabetextes. Das Ergebnis ist zur leichten Weiterverwendung in Markdown strukturiert.

### edu_material
Wandelt den Quelltext in eigenständiges Lehr‑ und Lernmaterial in derselben Sprache um. Der Inhalt ist direkt für Unterricht oder Selbststudium nutzbar und in Markdown formatiert.

### exams
Generiert fünf Prüfungsvarianten (unterschiedliche Stile) mit Lösungen, alle in der Sprache des Inputs. Jede Prüfung enthält eine Mischung aus leichten, mittleren und schwierigen Aufgaben und ist eigenständig in Markdown gehalten.

### active_reading
Verschränkt den Originaltext mit angeleiteten Active‑Reading‑Elementen zur besseren Verständlichkeit. Die Ausgabe simuliert die Gedankenprozesse vor, während und nach dem Lesen und ist in Markdown formatiert.

</details>


## Prompts
You can find the prompts are in `prompts.py`.