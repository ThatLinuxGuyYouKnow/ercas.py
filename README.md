# ErcasPay Python Library and Flask Integration

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.0+-blue.svg)](https://flask.palletsprojects.com/en/2.3.x/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-development-orange.svg)](#)

A Python library for interacting with the ErcasPay API, along with a Flask-based web server to initiate payments using the library. This was built for the ErcasPay Hackathon to quickly demonstrate API usage and functionality.

## Features

*   **ErcasPay Python Library (`ercaspay_client.py`):**
    *   Wraps the ErcasPay API for easy use from Python.
    *   Supports initiating payments using the `/payment/initiate` endpoint.
    *   Handles API requests and responses (using the `requests` library).
    *   Includes basic error handling.
    *   Supports sandbox and live environments (configurable).
*   **Flask Payment Initiator (`example.py`):**
    *   Provides a `/initiate-payment` endpoint for initiating payments via POST requests.
    *   Accepts payment parameters as a JSON payload.
    *   Validates required parameters and types
    *   Utilizes the `ErcasPayClient` for the API interaction.
    *   Returns responses in JSON format.

## Getting Started

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https:github.com/thatlinuxguyyouknow/ercas.py
    cd ercas.py
    ```

2.  **Install dependencies:**

    ```bash
    pip install Flask requests
    ```

3.  **Set up your API Key:**
    *   In `example.py`, replace `api_key = "ercas_pay_key"` with your actual ErcasPay API key, in a standard production enviroment, it would be better to load it from a .env file.

### Usage

1.  **Run the Flask server:**

    ```bash
    python example.py
    ```

2.  **Send a POST request to initiate payment:**

    *   Use an HTTP client (like `curl`, `Postman`, or Insomnia) to send a POST request to `http://127.0.0.1:5000/initiate-payment`(Assuming you are running this locally on your machine).
    *   **Content-Type:** `application/json`
    *   **Request Body Example:**
        ```json
        {
          "amount": 2000,
          "paymentReference": "R5md7gd9b4s3h2j5d67g",
          "paymentMethods": "card,bank-transfer,ussd,qrcode",
          "customerName": "Olayemi Olaomo",
          "currency": "USD",
          "customerEmail": "ola@gmail.com",
          "customerPhoneNumber": "09061628409",
          "redirectUrl": "https://omolabakeventures.com",
          "description": "The description for this payment goes here",
          "metadata": {
              "firstname": "Ola",
              "lastname": "Benson",
              "email": "iie@mail.com"
            }
        }
        ```
3.  **Review the response:** The server will return a JSON response with the payment initiation result or an error message.

## API Documentation

Refer to the official ErcasPay API documentation for details on the `/payment/initiate` endpoint and other API calls.
[ERCASPAY DEVELOPER DOCUMENTATION](https://docs.ercaspay.com/)


## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Disclaimer

This is a basic implementation and is not intended for production use without further testing and security considerations.