[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mrryaboev_quadratic_equation_new&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mrryaboev_quadratic_equation_new) [![codecov](https://codecov.io/gh/mrryaboev/quadratic_equation_new/graph/badge.svg?token=X8JAINLRMC)](https://codecov.io/gh/mrryaboev/quadratic_equation_new) [![Coverage Status](https://coveralls.io/repos/github/mrryaboev/quadratic_equation_new/badge.svg?branch=main)](https://coveralls.io/github/mrryaboev/quadratic_equation_new?branch=main)




Необходимо учесть различные сценарии и граничные случаи.

1.Позитивные тесты:


Два различных вещественных корня.

Два одинаковых вещественных корня.

Два комплексных корня.

Линейное уравнение (a = 0, b != 0).

2.Негативные тесты:


a = 0, b = 0 (нет решений).

Нечисловые аргументы (строки, списки и т.п.). (Можно решить, стоит ли делать проверку типов или полагаться на исключения Python).

Большие значения коэффициентов (проверка на переполнение, если необходимо).


3. Граничные случаи:


a, b, c близки к 0.

a, b, c очень большие или очень маленькие (близки к максимальным/минимальным значениям, которые может хранить float).
