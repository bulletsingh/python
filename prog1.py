import os
import re
 import sample
 here = os.path.abspath(os.path.dirname(__file__))
 # Get the long description from the relevant file
@@ -14,9 +12,10 @@
setup(
    name="sample",
     # There are various approaches to referencing the version. For a discussion,
    # see http://packaging.python.org/en/latest/tutorial.html#version
    version=sample.__version__,
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='1.2.0',
     description="A sample Python project",
    long_description=long_description,
