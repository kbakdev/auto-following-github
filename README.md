# Auto following bot

A simple bot to follow and unfollow users on GitHub. This bot is written in Python 2.7 using the Selenium library. Please note that using automated scripts on GitHub is against their terms of service, and this project is intended for educational purposes only. Use at your own risk.

## Getting Started

### Pre-requisites

- Python
- Selenium (pip install selenium)
- Firefox browser
- geckodriver (Firefox WebDriver)

### Installation
1. Clone the repository
2. Install the pre-requisites
3. Configure your GitHub credentials in the `config/config.ini` file

### Usage

To run the follow bot, run the following command:

```
python3 src/follow_bot.py -t <username> -f <number of users to follow>
```

To run the unfollow bot, run the following command:

```
python src/remove_users.py
```

### Testing

To run tests for the project, execute the following command:

```
python -m unittest discover tests
```

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Disclaimer
This project is for educational purposes only. Use of this bot may violate GitHub's terms of service. The authors of this project are not responsible for any consequences resulting from its use.

