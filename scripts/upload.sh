#!/usr/bin/env sh
pandoc --from=markdown --to=rst --output=README README.md
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi
