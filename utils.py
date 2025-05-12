import os

def generate_guard_name(file_path):
    """
    Generate the unique #ifndef guard name based on the file path.
    Example: utility/utf8/utf8_char_decode/utf8_char_decode.h
    will generate _UTILITY_UTF8_UTF8_CHAR_DECODE_UTF8_CHAR_DECODE_H_
    """
    relative_path = os.path.relpath(file_path).replace(os.sep, '_').upper()
    return f"_{relative_path.replace('.', '_').replace('-', '_').replace(' ', '_')}_"

def update_file(file_path, guard_name):
    """
    Updates the file by adding the necessary #ifndef guard at the top.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    header_content = f"#ifndef {guard_name}\n#define {guard_name}\n\n" + content + "\n#endif // {guard_name}"

    with open(file_path, 'w') as file:
        file.write(header_content)
