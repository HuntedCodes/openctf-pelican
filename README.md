
# OpenCTF info site, made with Pelican.

At it's heart, this is a Python project, using `pipenv`.


## Installation

```
# Install Python deps.
sudo apt install -y python3 python3-pip
sudo -H pip3 install pipenv

# Install Project deps.
pipenv install
# If no Pipfile
# pipenv install -r requirements.txt

# Start the virtualenv.
pipenv shell
```

## Modifying the Site

Content is located in `/content/`, in GFM (GitHub flavored markdown).
Most of the content are individual pages.

The configuration is `pelicanconf.py`.

## Building the Site

From the project root:

```
pelican content
```

The generated static site will be in `/output/`.
Copy it to the web root you want the site served from.
