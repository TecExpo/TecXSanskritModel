# Create a PyPI Account: Register at PyPI.org and generate an API token in your account settings. Store this token safely; it replaces your password for uploads.
# Install Build Tools: Ensure you have the latest versions of build and twine.

# bash

pip install --upgrade build twine


# Generate Archives: Create the source distribution and wheel files.
# bash

python -m build

# Upload to PyPI: Use twine to upload the contents of the newly created dist/ directory.
# bash

twine upload dist/*


# When prompted for a username, enter __token__. For the password, paste your PyPI API token (including the pypi- prefix). 



# Verification
# Once uploaded, anyone can install your library: 

# bash


pip install sanskrit-cleaner
