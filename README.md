# Argumeter

**Argumeter** is a FastAPI-based application that takes a discussion thread as input and evaluates the arguments of the participants. It assigns an overall score to each user, identifies the facts supporting their arguments, and highlights any logical fallacies present.

## Features

- Accepts a discussion thread as input via a web form.
- Analyzes each user's arguments.
- Assigns an overall score to each user (on a scale of 1-10).
- Identifies supporting facts for each argument.
- Highlights any logical fallacies in the arguments.

## Technologies Used

- **FastAPI**: Web framework for building the app.
- **OpenAI API**: Used for argument evaluation and scoring.
- **Jinja2**: Template engine for rendering HTML pages.
- **HTML/CSS**: Basic frontend for the web form.
- **Uvicorn**: ASGI server for serving the FastAPI app.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/onurmatik/argumeter.git
   cd argumeter
   ```
   
2. Create a virtual environment and activate it:

   ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3.	Install the required dependencies:

    ```bash
    touch .env
    ```
    Add the following line to the .env file:

    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```

6.	Run the app:

    ```bash
    uvicorn argumeter:app --reload
    ```

    The app will now be running on http://127.0.0.1:8000/
    

## Usage

1. Open your browser and go to http://127.0.0.1:8000/. 
2. Submit a discussion thread in the provided form. It can be any text containing a dialog. See a [sample thread](./samples/climate.txt).
3. The app will evaluate the arguments and return the results, showing the user scores based on the strength of their arguments and a breakdown of their arguments. 


## Contributing

If you’d like to contribute to this project, feel free to submit a pull request or open an issue. Any contributions or feedback are welcome!


## License

This project is licensed under the MIT License.
