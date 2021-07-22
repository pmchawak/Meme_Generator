# Meme Generator

A command-line and web application that generates random star wars and/or custom memes.

## Getting Started

The following instructions show how to get the Meme Generator running for web requests
and using the command-line program.

### Prerequisites

* Required python libraries:
```bash
pip install -r requirements.txt
```

* pdftotext 
```bash
# deb based distros
apt-get install poppler-utils
```

```bash
# yum based distros
yum install poppler-utils
```

### Command-line Application
```bash
$ python3 meme.py --help
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

MeMe Generator CLI

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to image file
  --body BODY      quote for meme
  --author AUTHOR  author of quote
```

### Web-based Application
Start the web application
```bash
python app.py
```

You can access the application at: http://localhost:5000
