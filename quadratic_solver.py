import cmath

def solve_quadratic_equation(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    Args:
        a: Коэффициент при x^2.
        b: Коэффициент при x.
        c: Свободный член.

    Returns:
        Кортеж с корнями уравнения. Если корней нет, возвращает None.
    """
    if a == 0:
        if b == 0:
            return None  # Нет решений, если a и b равны 0
        else:
            return (-c / b,)  # Линейное уравнение, один корень

    delta = (b**2) - 4*(a*c)

    if delta >= 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return (x1, x2)
    else:
        x1 = (-b - cmath.sqrt(delta)) / (2 * a)
        x2 = (-b + cmath.sqrt(delta)) / (2 * a)
        return (x1, x2)

if __name__ == '__main__':
    a = 1
    b = -3
    c = 2
    roots = solve_quadratic_equation(a, b, c)
    if roots:
        print("Корни уравнения:", roots)
    else:
        print("Уравнение не имеет решений.")
