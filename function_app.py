"""Azure Functions HTTP trigger example with multiple endpoints."""

import azure.functions as func
import logging
from parsing_operations import parse_schedule_query  

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1", methods=["GET", "POST"])
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    """Process HTTP trigger and return greeting message."""
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This http_trigger1 function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="process_scheduling_query", methods=["POST"])
def process_scheduling_query(req: func.HttpRequest) -> func.HttpResponse:
    """Delegate to parse_schedule_query function."""
    return parse_schedule_query(req)  # Use the imported function