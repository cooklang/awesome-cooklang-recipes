#!/usr/bin/env python3
import yaml
import os
import sys
import jinja2

DATA_FILE = "data.yaml"
DATA_PATH = os.path.join(os.getcwd(), DATA_FILE)
TEMPLATE_FOLDER = os.path.join(os.getcwd(), "templates")
TEMPLATE_FILE = "README.md.j2"
TEMPLATE_PATH = os.path.join(TEMPLATE_FOLDER, TEMPLATE_FILE)
ROOT_NODE = "userCookbooks"

# TODO: Check if file exists, otherwise exit with error
if os.path.isfile(DATA_PATH):
  with open(DATA_PATH, "r", encoding="utf-8") as data_file:
    yaml_data = yaml.safe_load(data_file)
else:
  print(f"No data file present. Please provide {DATA_PATH}")
  sys.exit(1)

if not os.path.isfile(TEMPLATE_PATH):
  print(f"No template file present. Please provide {TEMPLATE_PATH}")
  sys.exit(1)

def massage_data():
  # Sort repositories
  yaml_data[ROOT_NODE] = sorted(yaml_data[ROOT_NODE], key=lambda d: d["website"]["name"].lower())

def render_readme_template():
  env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=TEMPLATE_FOLDER))
  template = env.get_template(TEMPLATE_FILE)
  output = template.render(
    user_cookbooks=yaml_data[ROOT_NODE],
  )
  return output
  
def main():
  massage_data()
  print(render_readme_template())
  return 0

if __name__ == "__main__":
  sys.exit(main())
