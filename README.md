# Advent of Code

My solutions for Advent of Code

See https://adventofcode.com

## Setup

First-time setup:
```
pip install poetry
poetry config virtualenvs.in-project true
poetry shell
poetry install
```

This project is designed to be run using pytest. Use the pytest command to
execute tests:
```
poetry shell
pytest
```

I'd recommend setting up VSCode with the virtual environment you created with
`poetry shell`. Then installing a Python test runner with autorun support to
re-run specific day solutions while developing the solution on file saves. This
isn't something I'll document in detail since the precise setup steps change
often due to updates etc.