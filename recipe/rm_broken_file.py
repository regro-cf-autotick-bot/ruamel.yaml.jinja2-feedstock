import os
import re


ruamel_path = os.path.abspath(os.environ["SP_DIR"])
re_file = re.compile(r"^ruamel\.yaml\.jinja2-.*\.pth$", re.DOTALL)

for f in os.listdir(ruamel_path):
    if re_file.match(f):
        os.remove(os.path.join(ruamel_path, f))
        break

