Warhammer 40k PDF Processing and Analysis
This project processes and analyzes Warhammer 40k PDF books using various Python scripts and external services.
Overview
The system reads Warhammer 40k PDF books, splits them into pages, uploads them to Dropbox, and performs text analysis using a local language model server. It also includes functionality for creating embeddings and managing a Redis cache for account names.
Components

ConfigReader.py: Reads configuration from a config.ini file.
LLM.py: Handles interaction with a local language model server for text processing.
Prompts.py: Contains prompt templates for text processing tasks.
Run.py: The main script that orchestrates the workflow.
Warhammer40k.py: Manages PDF processing and Dropbox interactions.
Database.py: Implements a Redis-based caching system for account names.

Requirements

Python 3.x
Dropbox API access
Redis server
Local language model server (running on http://127.0.0.1:8082)
PyPDF2
pandas
dropbox
redis-py
configparser
requests

Installation

Install the required Python libraries:
pip install PyPDF2 pandas dropbox redis configparser requests
Set up a Dropbox API token and add it to the config.ini file.
Ensure you have a Redis server running locally or update the connection settings in Database.py.
Set up and run the local language model server on port 8082.

Usage

Configure the settings in config.ini, including the Dropbox API token and book name.
Run the main script:
python Run.py

This will process the specified Warhammer 40k book, upload pages to Dropbox, perform text analysis, and save the results to an Excel file.
Configuration
Update the config.ini file with the following information:

Dropbox API token
Book name

File Descriptions

ConfigReader.py: Reads configuration settings.
LLM.py: Handles text processing and embedding creation.
Prompts.py: Stores text processing prompts.
Run.py: Main execution script.
Warhammer40k.py: Manages PDF processing and Dropbox interactions.
Database.py: Implements Redis-based caching for account names.

Note: Ensure that the local language model server is running and accessible at http://127.0.0.1:8082 before running the script.
Contributing
Contributions to improve the project are welcome. Please submit pull requests for any enhancements.
