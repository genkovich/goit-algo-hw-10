import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


def main():
    a, b = 2, 3
    num_samples = 1000
    monte_carlo(a, b, num_samples)

def visualize_results(x_random, y_random):
    a = 2  # Нижня межа
    b = 3  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(1.75, 3.25, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)
    ax.scatter(x_random, y_random, color = "red")

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = 3^x від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo(a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Кількість точок під кривою
    under_curve = np.sum(y_random < f(x_random))

    # Площа під кривою
    area_under_curve = (b - a) * f(b) * under_curve / num_samples

    # Обчислення інтеграла за допомогою функції quad
    result, error = spi.quad(f, a, b)

    print('Площа обчислена методом Монте-Карло', area_under_curve, 'Площа обчислена функцією quad', result)
    visualize_results(x_random, y_random)


# Визначення функції та межі інтегрування
def f(x):
    return 3 ** x


if __name__ == "__main__":
    main()


