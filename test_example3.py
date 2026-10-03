import pytest


# Тест с меткой "user"
@pytest.mark.user
def test_create_user():
    assert "user" == "user"

# Тест с меткой "slow"
@pytest.mark.slow
def test_heavy_computation():
    result = sum(i for i in range(1000000))
    assert result > 0

# Тест с двумя метками "user" и "slow"
@pytest.mark.user
@pytest.mark.slow
def test_update_user_profile():
    assert "profile updated" == "profile updated"