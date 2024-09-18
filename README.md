# untraify.py

Copy translation strings back into weidu dialogue files.

## Installation

- Have python installed.
- Copy untraify.py

## Usage

```bash
# In the same directory as files.d and files.tra, where
# files.d and files.tra are traified weidu dialogue files and their tra files
# Run
python untraify.py
```

## Features

- Replace "@0", "@1", etc in .d files with the corresponding text from .tra file
- Applies to all file pairs (filename.d, filename.tra) with the same filename
- Outputs the number of strings copied in each .d file


## Bugs

Please open an issue to report bugs.


## License

This project is licensed under the GNU GPLv2.0 License - see the LICENSE file for details.
