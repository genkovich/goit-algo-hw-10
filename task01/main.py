import pulp


def main():
    model = pulp.LpProblem("Maximize Lemonade Count", pulp.LpMaximize)

    # Невідомі змінні
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')

    model += lemonade + juice, "Total Products"

    model += 2 * lemonade + 1 * juice <= 100, "Вода"
    model += 1 * lemonade <= 50, "Цукор"
    model += 1 * lemonade <= 30, "Лимонний сік"
    model += 2 * juice <= 40, "Фруктове пюре"

    model.solve()

    print("Лимонаду:", lemonade.varValue)
    print("Соку:", juice.varValue)


if __name__ == "__main__":
    main()
