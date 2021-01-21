Probleme
========

- Speicher: Ursprünglich für jedes Feld ein Objekt der Klasse
    Actor. Zeichne einfach bitmap für jeden an der entsprechenden
    stelle. 130% ram belegt, ohne überhaupt logik implementiert
    zu haben. Neue Ansatz: Wände werden seperat in einer Bitmap
    gehandhabt, Actor speichern ihre Position selber