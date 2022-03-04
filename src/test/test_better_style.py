from better_style import seperate_file_name_base_and_file_extension, add_count_to_string


def test_seperate_file_name_base_and_file_name_ending():
    name_base, name_ending = seperate_file_name_base_and_file_extension("test.high.txt")
    assert name_base == "test.high", "name base not correct"
    assert name_ending == "txt", "name ending not correct"
    base, ending = seperate_file_name_base_and_file_extension("test")
    assert base == "test", "name base not correct if no dot present"
    assert ending == "", "ending should be empty string if no dot present"

def test_add_count_to_string():
    assert add_count_to_string("test") == "test-1"
    assert add_count_to_string("test-1") == "test-2"
