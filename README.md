# GenAI POC

This repository contains my learnings about ChatGPT, LangChain, RAGs and AI Agents.

## Project Structure

The project is organized into modules, where each module represents a lesson or topic:

```
module1/
  src/
    main.py       # Main entry point for the module
    readme.md     # Learnings and notes for the chapter

README.md         # This file - repository instructions
pyproject.toml    # Poetry project configuration
poetry.lock       # Locked dependencies
.gitignore        # Git ignore rules
```

## Prerequisites

- Python 3.9 or higher
- Poetry (Python package manager)

## Installation

1. Install Poetry if you haven't already:

   ```bash
   pip install poetry
   ```

2. Install project dependencies:

   ```bash
   poetry install
   ```

3. To add a new dependency, use:
   ```bash
   poetry add <package-name>
   ```

## Running Modules

Each module can be executed using Poetry. Navigate to the repository root and run:

### Module 1

```bash
poetry run python module_1/src/main.py
```

## Adding New Modules

To add a new module:

1. Create a new folder with the module name (e.g., `module2/`)
2. Create a `src/` subfolder inside it
3. Add `main.py` for the entry point
4. Add `readme.md` for documenting learnings

## License

This project is for educational purposes.
