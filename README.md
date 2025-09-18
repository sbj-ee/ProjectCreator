# ProjectCreator

`ProjectCreator` is a Python script that generates a complete and standardized project structure for a new Python module. It simplifies the process of starting a new project by creating a best-practice directory layout with all the necessary boilerplate files.

## Features

Running the script for a new module (e.g., `my_new_module`) will generate the following structure:

```
my_new_module/
├── .gitignore
├── LICENSE
├── README.md
├── docs/
│   ├── conf.py
│   └── index.rst
├── pyproject.toml
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── my_new_module/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── __init__.py
    └── test_my_new_module.py
```

- **`src` layout:** Follows the modern `src` layout for better package management.
- **Testing with `unittest`:** Includes a `tests` directory with a sample test file.
- **Documentation with Sphinx:** Pre-configured `docs` directory with `conf.py` and `index.rst`.
- **Packaging with `pyproject.toml`:** A `pyproject.toml` file is included for modern packaging and dependency management.
- **`.gitignore` and `LICENSE`:** Comes with a standard `.gitignore` for Python projects and a pre-filled MIT License.

## Prerequisites

- Python 3.x

## Usage

To create a new project, run the `project_gen.py` script from your terminal:

```bash
python3 project_gen.py <your_module_name> --path /path/to/your/projects
```

### Example

```bash
python3 project_gen.py my_new_module --path /mnt/e/Python_Projects
```

This command will create a new directory named `my_new_module` inside `/mnt/e/Python_Projects` with the complete project structure.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
