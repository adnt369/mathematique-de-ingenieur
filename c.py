import numpy as np
import matplotlib.pyplot as plt


def fibonacci_spiral(n_terms):
    # Initialisation des termes de la séquence de Fibonacci
    a, b = 0, 1
    fibonacci_sequence = [a, b]

    for _ in range(n_terms - 2):
        a, b = b, a + b
        fibonacci_sequence.append(b)

    return fibonacci_sequence


def plot_fibonacci_spiral(n_terms):
    fibonacci_sequence = fibonacci_spiral(n_terms)

    # Création de l'espace de dessin
    fig, ax = plt.subplots()

    x, y = [0], [0]
    angle = 0
    for length in fibonacci_sequence:
        angle += np.pi / 2
        x.append(x[-1] + length * np.cos(angle))
        y.append(y[-1] + length * np.sin(angle))

        # Tracé des lignes
        ax.plot(x, y, 'b-')

    # Ajustement du graphique
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title('Spirale de Fibonacci')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


# Nombre de termes à afficher
n_terms = 10
plot_fibonacci_spiral(n_terms)
