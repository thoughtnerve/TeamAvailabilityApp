# Team Availability App

An Azure Functions-based application for processing and managing team scheduling queries. The application provides a REST API endpoint that accepts natural language scheduling queries and processes them for team availability management.

## Features

- Natural language query processing for scheduling requests
- Azure Functions HTTP trigger endpoints
- Comprehensive test suite with detailed reporting
- Excel-based test result reporting

## Project Structure

```
TeamAvailabilityApp/
├── function_app.py          # Main Azure Functions application
├── parsing_operations.py    # Core parsing operations
├── requirements.txt         # Python dependencies
├── tests/                  # Test suite
│   ├── test_parsing_operations.py
│   ├── test_parsing_operations1.py
│   └── test-reports/      # Test result reports
└── host.json              # Azure Functions host configuration
```

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   python -m tests.test_parsing_operations1
   ```

## Development

- The application is built using Azure Functions v4
- Tests are written using Python's unittest framework
- Test results are saved in both console output and Excel format

## License

MIT License 