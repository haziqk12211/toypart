def add(x, y):
    return x + y

def test_add():
    # INTENTIONAL FAILURE FOR RED RUN:
    # 2 + 2 != 5, will cause GitHub Actions to fail (Red Run)
    assert add(2, 2) == 4

