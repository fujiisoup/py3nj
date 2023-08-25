# Publish to Pypi

## Build a wheel
```
python -m build . --sdist
```
(requires `build` library. To install it, do `pip install build`)

## Upload to pypi
```
twine upload --repository pypi .\dist\* --verbose
```
(requires `twine` library. To install it, do `pip install twine`)

