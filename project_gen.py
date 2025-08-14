import os
import argparse
from pathlib import Path

def create_module_structure(module_name: str, base_path: str = ".") -> None:
    """
    Create a standard Python module structure with template files.

    Args:
        module_name (str): Name of the module to create
        base_path (str): Base path where the module directory will be created
    """
    # Convert module name to PascalCase for class names
    ModuleName = "".join(word.capitalize() for word in module_name.split("_"))

    # Define the directory structure
    module_structure = {
        module_name: {
            "src": {
                module_name: {
                    "__init__.py": f"# __init__.py for {module_name}\n\n__version__ = '0.1.0'\n",
                    "main.py": f"""# main.py\n\nclass {ModuleName}:\n    def __init__(self):\n        pass\n\n    def example_method(self):\n        return 'Hello from {ModuleName}!'\n\nif __name__ == '__main__':\n    obj = {ModuleName}()\n    print(obj.example_method())\n""",
                },
                "__init__.py": "",
            },
            "tests": {
                "__init__.py": "",
                f"test_{module_name}.py": f"""# test_{module_name}.py\n\nimport unittest\nfrom src.{module_name}.main import {ModuleName}\n\nclass Test{ModuleName}(unittest.TestCase):\n    def setUp(self):\n        self.obj = {ModuleName}()\n\n    def test_example_method(self):\n        self.assertEqual(self.obj.example_method(), 'Hello from {ModuleName}!')\n\nif __name__ == '__main__':\n    unittest.main()\n""",
            },
            "docs": {
                "index.rst": f"{module_name} Documentation\n====================\n\nWelcome to the {module_name} documentation.\n",
                "conf.py": f"""# conf.py\n\nproject = '{module_name}'\ncopyright = '2025, Your Name'\nauthor = 'Your Name'\nrelease = '0.1.0'\n\nextensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']\ntemplates_path = ['_templates']\nexclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']\nhtml_theme = 'alabaster'\nhtml_static_path = ['_static']\n""",
            },
            "README.md": f"""# {module_name}\n\nA Python module for [describe your module here].\n\n## Installation\n\n```bash\npip install {module_name}\n```\n\n## Usage\n\n```python\nfrom {module_name} import {ModuleName}\n\nobj = {ModuleName}()\nprint(obj.example_method())\n```\n\n## Development\n\n- Clone the repository\n- Install dependencies: `pip install -r requirements.txt`\n- Run tests: `python -m unittest discover tests`\n""",
            "pyproject.toml": f"""[project]\nname = "{module_name}"\nversion = "0.1.0"\ndescription = "A Python module for [describe your module here]"\nreadme = "README.md"\nrequires-python = ">=3.8"\ndependencies = []\n\n[project.optional-dependencies]\ntest = ["pytest", "pytest-cov"]\ndev = ["black", "isort", "flake8"]\n\n[build-system]\nrequires = ["setuptools>=61.0"]\nbuild-backend = "setuptools.build_meta"\n""",
            "requirements.txt": "# requirements.txt\n\n# Add your dependencies here\n",
            ".gitignore": """# .gitignore\n\n__pycache__/\n*.pyc\n*.pyo\n*.pyd\n.Python\nenv/\nvenv/\n.env\n*.egg-info/\n*.egg\nbuild/\ndist/\n*.log\n*.cache\n.pytest_cache/\n.coverage\ncoverage.xml\n*.tox/\n*.DS_Store\n*.idea/\n.vscode/\n""",
            "LICENSE": """MIT License\n\nCopyright (c) 2025 Your Name\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n"""
        }
    }

    def create_files(structure: dict, current_path: Path) -> None:
        """
        Recursively create directories and files from the structure dictionary.

        Args:
            structure (dict): Dictionary defining the directory/file structure
            current_path (Path): Current path for creating files/directories
        """
        for name, content in structure.items():
            new_path = current_path / name
            if isinstance(content, dict):
                # Create directory
                new_path.mkdir(parents=True, exist_ok=True)
                create_files(content, new_path)
            else:
                # Create file with content
                try:
                    with open(new_path, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error creating file {new_path}: {e}")

    # Validate module name
    if not module_name.isidentifier():
        raise ValueError(f"'{module_name}' is not a valid Python identifier")

    # Create the base module directory
    base_module_path = Path(base_path) / module_name
    try:
        base_module_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Failed to create directory {base_module_path}: {e}")

    # Create the structure
    create_files(module_structure[module_name], base_module_path)
    print(f"Created Python module structure for '{module_name}' at {base_module_path}")

def main():
    parser = argparse.ArgumentParser(description="Create a Python module structure.")
    parser.add_argument("module_name", help="Name of the module to create")
    parser.add_argument("--path", default=".", help="Base path for module creation (default: current directory)")
    args = parser.parse_args()

    try:
        create_module_structure(args.module_name, args.path)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
