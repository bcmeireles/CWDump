# CWDump
Codewars parser/dumper. Retrieves some information on challenges completed and scrapes their solutions, saving everything on multiple markdown files in an organized way

## How it works
It will create a `README.md` file with some basic statistics regarding your [Codewars](https://codewars.com) profile and hyperlinks for each challenge you've completed. As well as a folder for each language you have katas completed with, and a .md file inside of it for each difficulty available.

You can see an example of the `README.md` [here](/generated/README.md)

Inside the `generated` directory you can see an example of the outputs.

Keep in mind all solutions are returning `redacted` in order to not share my personal solutions, on your output it will have your actual solution there

And example of one of the `.md` files containing informations regarding the challenge and your solution, like this [one](/generated/python/4%20kyu.md)

## Usage
### Installation

Firstly, clone the repository using:
```zsh
git clone https://github.com/dvntx/CWDump.git
```

After cloning the repository, install ther requirements using `pip`.
```zsh
pip install -r requirements.txt
```

### Setup

In order for the script to work, you will need [geckodriver](https://github.com/mozilla/geckodriver), or change the webdriver used at [line 20](cwdump.py#L20)

Even if you do not change the webdriver, you may need to change the directory where it is located at, by editing [line 19](cwdump.py#L19).

### Running

After installing and setting everything up, simply run the script by using:
```zsh
python cwdump.py
```
It will open a browser window and load [Codewars's login page](https://www.codewars.com/users/sign_in), simply login and press `ENTER` on the command line, as instructed.

The output will be inside the `generated` directory.

### Bugs
If you get selenium errors where the script can't parse the solution for a given kata, it may be because it is not scrolling all the way down when it gets to the page with all your solutions. This may be due to slow load times and, in order to fix that, simply increase the `SCROLL_PAUSE_TIME` at [line 60](cwdump.py#L60)
