# Gravity Simulation (Python)

**Simple N-body gravitational model with 3D visualization**

This project simulates forces and movements of celestial bodies according to Newton's law of universal gravitation.

## 🧩 Project Structure

- `two_bodies.py`: Experimental two-body simulation (e.g., Sun + Earth) using leapfrog integration. Used for testing and validation before moving to n-body systems.
- `two_bodies.ipynb`: Jupyter notebook version of the two-body simulation for interactive exploration.
- `n_bodies.py`: Production N-body simulation (solar system, random bodies, 3+ bodies) with trajectory and force vector visualization.
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

## ▶️ Execution

Recommended: activate virtual environment and run one of the scripts:

```bash
python two_bodies.py
python n_bodies.py
```

## 🌀 Usage

`two_bodies.py` and `n_bodies.py` create a `matplotlib.animation.FuncAnimation` and display a 3D window.

- `two_bodies.py` provides experimental testing for a two-body model.
- `n_bodies.py` is the main simulation for n-body systems. It loads default values from `systems.py` using `system('Sonnensystem')` and can switch by name (e.g. `'zwei gleiche Massen'`, `'zehn zufällige Massen'`).

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
- Add collision detection and mass merging / performance improvements for large N.
- Add a proper package structure (`gravity/`) with importable API.

## 👨‍💻 Notes

- Simulations may become unstable for large `dt` in complex n-body systems.
- For real accuracy, relativistic corrections and stability checks should be added.

