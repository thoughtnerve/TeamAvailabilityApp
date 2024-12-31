import azure.functions as func
import logging
import json

def parse_schedule_query(req: func.HttpRequest) -> func.HttpResponse:
    """
    Parse a schedule query request containing raw text and return it in JSON format.
    """
    logging.info("Processing new schedule query request")
    
    try:
        # Get raw text from request body
        user_query = req.get_body().decode('utf-8')
        if not user_query:
            error_msg = "Empty request body"
            logging.warning(error_msg)
            return create_error_response(error_msg, status_code=400)
        
        response_data = {
            "status": "success",
            "UserQuery": user_query
        }
        
        return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )
            
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        logging.exception(error_msg)
        return create_error_response(error_msg, status_code=500)

def extract_meeting_details(req: func.HttpRequest) -> str:
    """Extract the meeting details from the user's query."""
    try:
        # Placeholder for actual meeting details extraction logic, for now just return the user's query
        
        return str(req.get_json())
    except ValueError:
        return "Error extracting meeting details"

def create_error_response(message: str, status_code: int) -> func.HttpResponse:
    """
    Create a standardized error response.
    """
    error_response = {
        "status": "error",
        "message": message
    }
    return func.HttpResponse(
        json.dumps(error_response),
        mimetype="application/json",
        status_code=status_code
    )