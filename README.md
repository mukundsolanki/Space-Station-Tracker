# Space-Station-Tracker

Welcome to the ISS Tracker Twitter Bot project! This Python-based Twitter bot fetches the current position of the International Space Station (ISS), plots it on a map, gathers crew information, and tweets updates every 5 minutes.


The International Space Station (ISS) is a space station, or a habitable artificial satellite, that orbits Earth at an average altitude of approximately 420 kilometers (261 miles).

ISS Speed
The ISS travels at an average speed of about 28,000 kilometers per hour (17,500 miles per hour).

# LIVE on X: 

The bot is Live on twitter : [@ISSLocatorBot](https://twitter.com/ISSLocatorBot)

## Features

- **ISS Position Tracking**: The bot tracks the real-time position of the ISS using available APIs.

- **Map Plotting**: It plots the ISS position on a map for better visualization.

- **Crew Information**: The bot fetches information about the current crew aboard the ISS.

- **Twitter Updates**: The bot tweets every 5 minutes with the crew information and a map image indicating the ISS position.

## Prerequisites

Before you start, make sure you have the following:

- Python installed on your system.

- Twitter Developer credentials stored in a `.env` file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mukundsolanki/Space-Station-Tracker.git
    cd iss-tracker-bot
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Create a `.env` file with the following Twitter API credentials:

    ```
    TWITTER_API_KEY=your_api_key
    TWITTER_API_SECRET=your_api_secret
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
    ```

- ## Run the GUI:

  If you want to just know the Position of the ISS on map then you can run the `main.py` file in a terminal, it will open a GUI.

## Run the Bot:

If you want to run the Bot then just setup the credentials and libraries and run the `bot.py` in a terminal.

## Screenshots of GUI:



# Contributions

If you would like to contribute to the project, feel free to fork the repository and submit pull requests.

Give this Repo a ⭐ if you like it.

# License
This project is licensed under the MIT License.