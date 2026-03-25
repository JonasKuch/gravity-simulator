# Gravity Simulation (Python)

**Simple N-body gravitational model with 3D visualization**

This project simulates forces and movements of celestial bodies according to Newton's law of universal gravitation.

## 🧩 Project Structure

- `main.py`: Two-body simulation (e.g., Sun + Earth) using leapfrog integration.
- `manybodies.py`: N-body simulation (solar system, random bodies, 3+ bodies) with trajectory and force vector visualization.
- `utils.py`: Physics engine:
  - `newton_force` (gravitational force magnitude)
  - `total_F` (n-body force sums + accelerations)
  - `leapfrog_integration` (symplectic time integrator)
- `systems.py`: Predefined scenarios (solar system, two equal masses, three equal masses, sun-earth-moon, random bodies). 

## ⚙️ Requirements

- Python 3.9+
- NumPy
- Matplotlib
- SciPy

Optional (for Jupyter notebook interaction):
- IPython

### Installation (mit `venv`)

```bash
python -m venv myenv
source myenv/bin/activate
pip install -U pip
pip install numpy matplotlib scipy
```

## ▶️ Execution

Recommended: activate virtual environment and run one of the scripts:

```bash
python main.py
python manybodies.py
```

In Jupyter:

```python
%run main.py
%run manybodies.py
```

## 🌀 Usage

`main.py` and `manybodies.py` create a `matplotlib.animation.FuncAnimation` and display a 3D window.

- `main.py` is fixed for a two-body model.
- `manybodies.py` loads default values from `systems.py` using `system('Sonnensystem')` and can switch by name (e.g. `'zwei gleiche Massen'`, `'zehn zufällige Massen'`).

## 📌 API (internal)

### `utils.newton_force(r, m1, m2)`
- Returns gravitational force magnitude given distance and two masses.

### `utils.total_F(coords, masses)`
- Input: `coords` list of 3D position vectors, `masses` list of scalars.
- Returns: force vectors for each body and acceleration vectors.

### `utils.leapfrog_integration(coords, velocities, masses, dt)`
- Input: positions, velocities, masses, time step.
- Returns: updated positions, velocities, new force vectors, old force vectors.

### `systems.system(systemname)`
- Input: scenario name.
- Returns: `coords, velocities, masses, names, colors, sizes, autoscale, axes_scales, dt`.

## 🛠️ Future improvements

- Add a CLI (ArgumentParser) for easy scenario selection and simulation duration.
- Add persistent logging of trajectory data to `.csv` or `.npz`.
- Add collision detection and mass merging / performance improvements for large N.
- Add zoom/pan and camera controls for Matplotlib.
- Add a proper package structure (`gravity/`) with importable API.

## 👨‍💻 Notes

- Simulations may become unstable for large `dt` in complex n-body systems.
- For real accuracy, relativistic corrections and stability checks should be added.

---

© 2026 Gravity Simulation
