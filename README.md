# C Ifndef Headers

This project is a Python script that checks and updates C/C++ header files with proper `#ifndef` guards.

## Features

- Recursively searches for `.h`, `.cpp`, `.c`, `.hpp` files in a specified directory (default is the current directory).
- Checks if each file contains the `#ifndef`, `#define`, and `#endif` preprocessor guards.
- If missing, automatically adds the necessary guards to the file.
- Supports dry-run mode where files are only checked, not modified.
- Custom guard name format based on the relative path of the file, ensuring uniqueness.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BaseMax/c-ifndef-headers.git
   cd c-ifndef-headers
   ```

2. Install dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to check and update header files:

```bash
python check_and_update.py /path/to/directory
```

To run in dry-run mode (only check files without modifying them):

```bash
python check_and_update.py /path/to/directory --dry-run
```

By default, the script will scan the current directory.

## License

MIT License

Copyright (c) 2025 Max Base
