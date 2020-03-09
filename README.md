# SIFAS Reroll Bot

## WTF

This is a script in Python 3 that automatizes the rerolling process for Love Live! All Stars game. This is still a work in progress.

## Dependencies

This needs `pyautogui` and `opencv-python` to work. Install both with `pip`.
```
pip install pyautogui opencv-python
```

You also need Nox (Android emulator) with SIFAS installed.

## Usage

Open Nox (Android 5) and keep the window maximized. Open the `playerprefs.xml` file in File Manager, then open Browser, then open SIFAS. Finally, run `python bot.py`.

## Issues and future improvements

- Remove hardcoded values so this can be easily reused somewhere other than my computer.