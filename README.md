# Game Title Screen

This repository contains a simple Python script that displays a title screen using the built-in `curses` module.
The title now reads **"This is an Exercise"** and shows options "Start", "Options", and "Quit" at the bottom of the screen.

## Requirements

- Python 3.x (with `curses` support)

## Usage

Run the script from your terminal:

```bash
python title_screen.py
```

Press any key to proceed from the title screen.

## Building an executable

If you want to create a standalone executable (for example on Windows), install
`pyinstaller` and run the provided build script:

```bash
pip install pyinstaller
./build_exe.sh
```

The resulting executable will be placed in the `dist` directory.
