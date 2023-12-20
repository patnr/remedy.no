# Project website

## Usage

- Create & edit web pages by editing **markdown** files.
- Push to Github.
- Wait 1 minute for the website to update (check status in "Actions" tab).

## Instant/live preview

Create & activate a dedicated virtual env. then, from the project root directory, do

```bash
pip install -e .
```

*Alternatively* use `poetry install` which itself takes care of setting up the virtual environment,
and installs the dependencies from `poetry.lock` (if it exists) rather than `pyproject.toml`,
thus providing stricter reproducibility.

Now run the following, which will print a URL for you to open in a browser.
The page should automatically refresh whenever you save a source markdown file.

```bash
mkdocs serve
```


## FAQ

- Q: How did you make the home page image?  
  A: Assembled a few `png`s with transparency.
- Q: How did you make the footer logos?  
  A: Googled "<company name> svg".
     Then used regex to replace all hex colors with "white".
