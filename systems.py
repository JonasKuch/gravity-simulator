"""gravity/systems.py

Provides predefined celestial body configurations (e.g., solar system, two equal masses, etc.).
"""

import numpy as np
from numpy import random

def system(systemname = 'Sonnensystem'):
    
    '''
    Sonnensystem
    '''
    if systemname == 'Sonnensystem':

        coords = [
            np.array([0, 0, 0], dtype=float),              # Sun
            np.array([0, 4.600e10, 0], dtype=float),       # Mercury
            np.array([0, 1.07477e11, 0], dtype=float),     # Venus
            np.array([0, 1.47098e11, 0], dtype=float),     # Earth
            np.array([0, 2.0662e11, 0], dtype=float),      # Mars
            np.array([0, 7.4052e11, 0], dtype=float),      # Jupiter
            np.array([0, 1.3536e12, 0], dtype=float),      # Saturn
            np.array([0, 2.7489e12, 0], dtype=float),      # Uranus
            np.array([0, 4.4529e12, 0], dtype=float)       # Neptune
        ]

        velocities = [
            np.array([0, 0, 0], dtype=float),              # Sun
            np.array([0, 0, 58980], dtype=float),          # Mercury
            np.array([0, 0, 35260], dtype=float),          # Venus
            np.array([0, 0, 30290], dtype=float),          # Earth
            np.array([0, 0, 26500], dtype=float),          # Mars
            np.array([0, 0, 13720], dtype=float),          # Jupiter
            np.array([0, 0, 10180], dtype=float),          # Saturn
            np.array([0, 0, 7110], dtype=float),           # Uranus
            np.array([0, 0, 5500], dtype=float)            # Neptune
        ]

        masses = [
            1.989e30,     # Sun
            3.3011e23,    # Mercury
            4.8675e24,    # Venus
            5.97237e24,   # Earth
            6.4171e23,    # Mars
            1.8982e27,    # Jupiter
            5.6834e26,    # Saturn
            8.6810e25,    # Uranus
            1.02413e26    # Neptune
        ]

        names = [
            "Sun",
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune"
        ]

        colors = [
            "orange",    # Sun
            "gray",      # Mercury
            "gold",      # Venus
            "blue",      # Earth
            "red",       # Mars
            "orange",    # Jupiter
            "khaki",     # Saturn
            "cyan",      # Uranus
            "darkblue"   # Neptune
        ]

        sizes = [
            120,  # Sun
            6,    # Mercury
            10,   # Venus
            11,   # Earth
            9,    # Mars
            25,   # Jupiter
            20,   # Saturn
            15,   # Uranus
            14    # Neptune
        ]

        autoscale = False
        axes_scales = [(-6e12, 6e12), (-6e12, 6e12), (-6e12, 6e12)]
        dt = 10000

    
    '''
    Drei gleiche Massen
    '''

    if systemname == 'zwei gleiche Massen':

        coords = [
            np.array([0, 0, 0], dtype=float),
            np.array([0, 1.5e11, 0], dtype=float)
            ]
        velocities = [
            np.array([10000, 0, 0], dtype=float), 
            np.array([0, 0, -30000], dtype=float)
            ]
        masses = [
            1.989e30, 
            1.989e30
            ]
        names = [
            'mass1', 
            'mass2'
            ]
        colors = [
            'red', 
            'blue'
            ]
        sizes = [
            10,
            10
        ]
        autoscale = True
        axes_scales = None
        dt = 10000


    '''
    10 zufällige Massen
    '''
    
    if systemname == 'zehn zufällige Massen':

        coords = [np.random.uniform(-3e11, 3e11, 3) for _ in range(10)]
        
        velocities = [np.random.uniform(-30000, 30000, 3) for _ in range(10)]
        
        masses = [random.uniform(1e24, 2e30) for _ in range(10)]  # zwischen Erdmasse und Sonnenmasse
        
        names = [f'mass{i+1}' for i in range(10)]
        
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'black', 'gray']
        
        sizes = [random.randint(5, 15) for _ in range(10)]  # rein visuell
        
        autoscale = True
        axes_scales = None
        dt = 5000  # etwas kleinere Zeitschritte wegen höherer Komplexität

    if systemname == 'drei gleiche Massen':

        coords = [
            np.array([1.5e11, 0, 0], dtype=float),
            np.array([0, 1.5e11, 0], dtype=float), 
            np.array([0, 0, 1.5e11], dtype=float)
            ]
        velocities = [
            np.array([0, 0, 0], dtype=float), 
            np.array([0, 0, -30000], dtype=float), 
            np.array([0, 30000, 0], dtype=float)
            ]
        masses = [
            1.989e30, 
            1.989e30, 
            1.989e30
            ]
        names = [
            'mass1', 
            'mass2', 
            'mass3'
            ]
        colors = [
            'red', 
            'blue', 
            'green'
            ]
        sizes = [
            10,
            10,
            10
        ]
        autoscale = True
        axes_scales = None
        dt = 10000

    
    '''
    Sonne, Erde, Mond
    '''
    if systemname == 'Sonne, Erde, Mond':

        coords = [
            np.array([0, 0, 0], dtype=float),                    # Sonne
            np.array([0, 1.47098e11, 0], dtype=float),            # Erde (Perihel)
            np.array([3.844e8, 1.47098e11, 0], dtype=float)        # Mond (Erde + 3.844e8 m in x-Richtung)
        ]

        velocities = [
            np.array([0, 0, 0], dtype=float),                    # Sonne
            np.array([0, 0, 30290], dtype=float),                # Erde
            np.array([0, 1022, 30290], dtype=float)              # Mond (Erde + relative Geschwindigkeit)
        ]

        # Massen in kg
        masses = [
            1.989e30,      # Sonne
            5.97237e24,    # Erde
            7.342e22       # Mond
        ]

        # Namen für Beschriftungen
        names = [
            "Sun",
            "Earth",
            "Moon"
        ]

        # Farben für Scatterplots
        colors = [
            "orange",  # Sonne
            "blue",    # Erde
            "gray"     # Mond
        ]

        # Relative Größen für Scatterplots (angepasst, damit die Sonne die Erde und den Mond nicht "verschluckt")
        sizes = [
            20,  # Sonne
            5,   # Erde
            2    # Mond
        ]

        autoscale = False
        axes_scales = [(-2e11, 2e11), (-2e11, 2e11), (-2e11, 2e11)]
        dt = 1000
        
    return coords, velocities, masses, names, colors, sizes, autoscale, axes_scales, dt