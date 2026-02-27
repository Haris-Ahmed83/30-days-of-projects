# Day 05 - Currency Converter

## Project Description

This is a professional Python-based currency converter that fetches real-time exchange rates from an external API. It allows users to convert amounts between different global currencies easily.

## Features

*   **Real-time Exchange Rates**: Fetches the latest exchange rates using the ExchangeRate-API.
*   **Support for Multiple Currencies**: Supports a wide range of global currencies.
*   **User-friendly Interface**: Simple command-line interface for inputting currencies and amounts.
*   **Error Handling**: Robust error handling for network issues and invalid currency codes.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd Day_05_Currency_Converter
    ```

2.  **Install the required library**:

    ```bash
    pip install requests
    ```

3.  **Run the currency converter**:

    ```bash
    python currency_converter.py
    ```

## Usage

Upon running the script, follow the prompts to enter the base currency, target currency, and the amount you wish to convert.

### Example Workflow

1.  **Enter base currency**: `USD`
2.  **Enter target currency**: `EUR`
3.  **Enter amount**: `100`
4.  **Output**: `100.0 USD is equal to 92.45 EUR` (Note: Exchange rates will vary based on current data).
