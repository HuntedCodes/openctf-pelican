# OpenCTF Site

At it's heart, this is a Python project, using `pipenv`.
It makes use of the [Pelican](https://blog.getpelican.com/) static site generator (SSG).

## Installation

```
# Install Python deps.
sudo apt install -y python3 python3-pip
sudo -H pip3 install pipenv

# Install Project deps.
# If for some reason you can't use pipenv, create requirements.txt from Pipfile.
pipenv install

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

## Serving the Site in Development


