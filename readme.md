* Площа, обчислена методом Монте-Карло: **16.551**
* Площа, обчислена функцією quad: **16.38430607928307**

Метод Монте-Карло дає результат, який досить близький до результату, отриманого за допомогою функції quad з бібліотеки SciPy.
Відмінність між результатами становить приблизно 0.1667, що є допустимою похибкою для методу Монте-Карло, особливо з урахуванням випадкового характеру цього методу та відносно невеликої кількості вибірок (1000).

Отримані результати підтверджують, що метод Монте-Карло, незважаючи на свою простоту та випадковість, є дієвим інструментом для наближеного обчислення визначених інтегралів.