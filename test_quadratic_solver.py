import pytest
from quadratic_solver import solve_quadratic_equation

def test_two_distinct_real_roots():
    assert solve_quadratic_equation(1, -5, 6) == (3.0, 2.0) or solve_quadratic_equation(1, -5, 6) == (2.0, 3.0)

def test_two_identical_real_roots():
    assert solve_quadratic_equation(1, -2, 1) == (1.0, 1.0)

def test_complex_roots():
    roots = solve_quadratic_equation(1, 2, 5)
    assert isinstance(roots[0], complex)
    assert isinstance(roots[1], complex)

def test_linear_equation():
    assert solve_quadratic_equation(0, 2, -4) == (2.0,)

def test_no_solution():
    assert solve_quadratic_equation(0, 0, 5) is None

def test_near_zero():
    assert solve_quadratic_equation(0.00001, -0.00002, 0.00001) == (1.0, 1.0)

# Пример негативного теста (если хотите проверять типы)
#def test_invalid_input_type():
#    with pytest.raises(TypeError):
#        solve_quadratic_equation("a", 2, 3)
