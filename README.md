# Smmry

Smmry is a [multi-document summarization](https://en.wikipedia.org/wiki/Multi-document_summarization) tool for news articles. It fetches five articles from NewsAPI and attempts to summarize them into 150 words.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have installed all of the following prerequisites on your development machine.
- [Git](https://git-scm.com/downloads) (If using Windows make sure Git Bash in installed)
- [Python](https://www.python.org/downloads/) (Recommended Python 3.8)
- [NodeJS](https://nodejs.org/en/download/) (Recommended NodeJS 12.16.2 and NPM 6.14.4)



### Installing

*Note: If using Windows all commands should be run in a Git Bash terminal.*

Clone this repository and change into the cloned repository's directory:
```sh
$ git clone https://github.com/mihir3k/smmry
$ cd smmry
```

Create a python virtual enviroment and activate it:
```sh
$ python -m venv venv
$ source venv/Scripts/activate
```

Install dependencies as defined in `requirements.txt`:
```sh
$ pip install -r requirements.txt
```

This project uses a frontend built with ReactJS.  
Change into the `templates` directory and install dependencies as defined in `package.json`:
```sh
$ cd app/templates
$ npm install
```

Change back to the project's root directory:
```sh
$ cd ../../
```

## Running the Application

Edit `run.sample.sh` and paste your NewsAPI api key.  
*You can obtain a free NewsAPI api key by creating an account on https://newsapi.org*

Rename `run.sample.sh` to `run.sh`:
```sh
$ mv run.sample.sh run.sh
```

Execute `run.sh`:
```sh
$ ./run.sh
```

The application should run on port 5500 and can be accessed by going to http://localhost:5500 in your web browser.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/mihir3k/smmry/blob/master/LICENSE.md) file for details
