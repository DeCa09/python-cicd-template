import pytest
from addition_package.add import add


# this decorator allows that all assert statements in a test are executed,
# even if the first one were to fail
@pytest.mark.parametrize(
    "summand_1, summand_2, expected_answer",
    [(3, 5, 8), (-1, 1, 0), (-1, -1, -2), (5, 0, 5)],
)     
def test_add(summand_1, summand_2, expected_answer):
    assert add(summand_1, summand_2) == expected_answer
