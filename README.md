# WeatherApp

Welcome to the WeatherApp! This is a simple command-line application built in Python that allows users to fetch and display current weather information for any city using the OpenWeatherMap API.

## Features

- Get current weather data for any city worldwide.
- Displays temperature, weather description, humidity, and wind speed.
- Supports metric units (Celsius).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhisheklakhani-it/WeatherApp.git
   cd WeatherApp
   ```
2.	**Set up a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.	**Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.	Set up your environment variables:
	•	Create a .env file in the project directory and add your OpenWeatherMap API key:
    ```bash
    OPENWEATHER_API_KEY=your_actual_api_key_here
    ```
5.	Run the application:
	  ```bash
     python3 weather_app.py
    ```
## Usage

1.	Run the application using the command:
    ```bash
    python3 weather_app.py
    ```

2.	Enter the name of the city for which you want to fetch the weather data.
3.	The application will display the current temperature, weather description, humidity, and wind speed for the entered city.
4.	Type exit to quit the application.
## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request. You can also open an issue to discuss potential changes.

## Steps to Contribute:

	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature-branch).
	3.	Make your changes.
	4.	Commit your changes (git commit -m 'Add new feature').
	5.	Push to the branch (git push origin feature-branch).
	6.	Open a Pull Request.

## Future Features

	•	Add a weather forecast feature for the next 7 days.
	•	Implement a graphical user interface (GUI).
	•	Add support for multiple units (Celsius, Fahrenheit, Kelvin).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Created by Abhishek Lakhani - abhisheklakhani.it@gmail.com. Feel free to contact me for any questions or feedback.
