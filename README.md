# Gravity Simulation (Python)

**Einfaches N-Körper-Gravitationsmodell mit visueller 3D-Animation**

Dieses Projekt simuliert Kräfte und Bewegungen von Himmelskörpern gemäß dem newtonschen Gravitationsgesetz.

## 🧩 Projektstruktur

- `main.py`: Zwei-Körper-Simulation (z. B. Sonne + Erde) mittels Leapfrog-Integration.
- `manybodies.py`: Mehrkörper-Simulation (Sonnensystem, zufällige Körper, 3+ Körper), inklusive Anzeige von Trajektorien und Kraftvektoren.
- `utils.py`: Kernphysik-Engines:
  - `newton_force` (Gravitationsstärke)
  - `total_F` (N-Körper-Kraftsummen + Beschleunigungen)
  - `leapfrog_integration` (symplektische Zeitintegration)
  - `body` (Basis-Klasse, aktuell Platzhalter)
- `systems.py`: Vordefinierte Szenarien (Sonnensystem, zwei gleiche Massen, drei gleiche Massen, Sonne+Erde+Mond, zufällige Kugeln). 

## ⚙️ Voraussetzungen

- Python 3.9+
- NumPy
- Matplotlib
- SciPy

Optional (für Jupyter-Notebook-Interaktion):
- IPython

### Installation (mit `venv`)

```bash
python -m venv myenv
source myenv/bin/activate
pip install -U pip
pip install numpy matplotlib scipy
```

## ▶️ Ausführung

Empfehlung: aktivieren Sie virtuelle Umgebung und führen Sie eines der Skripte aus:

```bash
python main.py
python manybodies.py
```

In Jupyter:

```python
%run main.py
%run manybodies.py
```

## 🌀 Verwendung

`main.py` und `manybodies.py` erzeugen eine `matplotlib.animation.FuncAnimation` und zeigen ein 3D-Fenster an.

- `main.py` arbeitet fest mit einem Zweikörper-Modell.
- `manybodies.py` lädt per `system('Sonnensystem')` Standardwerte aus `systems.py` und kann per String wechseln (z.B. `'zwei gleiche Massen'`, `'zehn zufällige Massen'`).

## 📌 Funktionen / API (intern)

### `utils.newton_force(r, m1, m2)`
- Rückgabe: Gravitationskraftbetrag nach Newton.

### `utils.total_F(coords, masses)`
- Eingabe: `coords` Liste 3D-Vektoren und `masses` Liste von Massen.
- Rückgabe: Kraftvektoren für jedes Objekt und Beschleunigungen.

### `utils.leapfrog_integration(coords, velocities, masses, dt)`
- Eingabe: Positionen, Geschwindigkeit, Massen, Zeitschritt.
- Rückgabe: neue Positionen, neue Geschwindigkeiten, neue Kräfte, alte Kräfte.

### `systems.system(systemname)`
- Eingabe: Name der Konfiguration.
- Rückgabe: `coords, velocities, masses, names, colors, sizes, autoscale, axes_scales, dt`.

## 🛠️ Weiterentwicklungsideen

- Ein CLI (ArgumentParser) für einfache Szenenwahl und Simulationsdauer.
- Persistentes Logging der Bahndaten als `.csv` oder `.npz`.
- Kollisionserkennung und Massenfusion/amortisiertes Rechnen für große N.
- Zoom/Pan und Kamerasteuerung in Matplotlib.
- Ein komplettes Paket (`gravity/`) mit Import-API wäre nützlich.

## 👨‍💻 Hinweise

- Simulationen sind nicht stabil für große `dt` bei komplexen Mehrkörpersystemen.
- Für reale Genauigkeit müssten relativistische und Stabilitätsprüfungen ergänzt werden.

---

© 2026 Gravity Simulation
