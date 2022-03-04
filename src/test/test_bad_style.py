from bad_style import sample_one


def test_one():
    assert sample_one("test.txt") == "test-1.txt", "simple count not correct"
    assert sample_one("test-1.txt") == "test-2.txt", "advanced count not correct"
    assert sample_one("test-42.txt") == "test-43.txt", "count 42 not correct"

