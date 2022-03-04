import re


def add_counter_to_file_name(file_name):
    file_name_base, file_extension = seperate_file_name_base_and_file_extension(file_name)
    counted_name_base = add_count_to_string(file_name_base)
    return "{}.{}".format(counted_name_base, file_extension)


def add_count_to_string(input_string):
    base_string = get_string_without_counter_extension(input_string)
    count = get_current_counter(input_string) + 1
    return "{}-{}".format(base_string, count)


def get_current_counter(input_string):
    tmp = re.search(r"-([0-9]+)\Z", input_string)
    if tmp is not None:
        return int(tmp.group(1))
    else:
        return 0


def get_string_without_counter_extension(input_string):
    return re.sub(r"-[0-9]+\Z", "", input_string)


def seperate_file_name_base_and_file_extension(file_path):
    name_components = file_path.split(".")
    if len(name_components) > 1:
        ending = name_components[-1]
        name = ".".join(name_components[0:-1])
        return name, ending
    else:
        return file_path, ""
