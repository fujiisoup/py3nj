#!/usr/bin/env python3

import re
from pathlib import Path

root = Path(__file__).parents[1]

version_py = root / 'src' / '_version.py'
version_str = version_py.read_text()
version_pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"

match = re.search(version_pattern, version_str, re.M)
if match:
    print(match.group(1))
else:
    raise RuntimeError(f"Unable to find version string in: {version_py}")
