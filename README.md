# tee
Linux tee functionality for Windows

## What's this
This is my port of Linux tee functionality to handle verbose long-running commands (for example hybris software). Additionally it adds a timestamp to each line.
See: https://en.wikipedia.org/wiki/Tee_(command)

## Installation

```
pip install pyinstaller
```

```
cd c:\...\tee
```

```
pyinstaller --onefile tee.py
```

Then move generated dist/tee.exe to your PATH.

## Usage

```
long_command | tee outfile.txt
```

## Configuration

Not available.