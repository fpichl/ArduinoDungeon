Installation und Vorbereiten benötigter Software
================================================

Bevor mit der Entwicklung des Projektes begonnen werden kann, müssen einige
Programme installiert werden. In dieser Anleitung wird dabei davon ausgegangen,
dass Ubuntu 18.04 oder Windows 10 als Betriebssystem verwendet werden. Das
Nachbilden unter Verwendung anderer Betriebssysteme ist möglich, wird hier aber
nicht berücksichtigt.


Installation und Einrichtung der Arduino Entwicklungsumgebung
-------------------------------------------------------------
Unter https://www.arduino.cc/en/software kann die Arduino IDE heruntergeladen
werden. Dabei ist darauf zu achten, das korrekte Betriebssystem und die
korrekte Architektur zu wählen.

Nach der Installation der Entwicklungsumgebung muss die Bibliothek u8g2
heruntergeladen werden. Dazu wird die Entwicklungsumgebung gestartet. Nun wählt
man unter "Werkzeuge" den Bibliotheksverwalter aus und sucht dort nach "U8g2".
Es werden mehrere Bibliotheken vorgeschlagen, von denen ausschließlich die mit
dem Titel "U8g2" heruntergeladen wird. Zum Zeitpunkt des Schreibens ist die
aktuellste Version 2.27.6.


Verwenden einer Bildbearbeitungs- und Konvertierungssoftware
------------------------------------------------------------
Um Akteure, Gegenstände oder Ähnliches darstellen zu können, werden Bitmaps
verwendet. Sie enthalten die benötigten Informationen in Form eines Arrays,
bestehend aus Hexadezimalwerten.

Da das händische Erstellen aufwändig ist, wird an dieser Stelle empfohlen, ein
Programmen zum Erstellen von sogenannter "Pixel-Art" zu verwenden. Das
hier verwendete Programm ist Aseprite (https://www.aseprite.org/).
Eine kostenlose aber ebenso geeignete Variante stellt die Webanwendung Piskel
(https://www.piskelapp.com) dar. Hier in schwarz und weiß erstellte Bilder
(schwarz als Hintergrund, weiß als das darzustellende Objekt) können als .png
Dateien exportiert werden. Diese können wiederherum von einem
Konvertierungstool in ein c++ Array umgewandelt werden. In diesem Projekt wurde
dafür ein selbstgeschriebenes Python-Skript verwendet (siehe Anhang 1).
