Prompt to generate tests:

1. Objective: Develop a suite of unit tests for the parse_schedule_query function to handle various input scenarios, including both valid and invalid inputs, as if the function is being called from an external client. Refactor the tests to consolidate common steps into a single method or utility function to enhance code maintainability and readability.

2. Test File: Create the unit tests in a separate file named test_parsing_operations1.py.

3. Test Scenarios:
- Valid Input: Test with a well-formed request containing a valid user query.
- Invalid Input: Test with an empty request body, malformed JSON, and unexpected data types.
- Error Handling: Ensure that appropriate error messages and status codes are returned for invalid inputs.
- Test with at least 10 different user queries, with a mix of valid and invalid inputs including special character, escape characters, and edge cases.

4. Common Steps:
- Identify and refactor common steps in the test cases into a helper method to avoid redundancy and improve clarity.

5. Documentation: Document the test results in a table format with the following columns:
- Request Input: Description of the input used in the test.
- Response Output: Expected response from the function, including status code and message.

6. Output: The code should record the tests and print out the table as output of the test suite run. Additionally, save the results to an Excel file with formatted tables and word wrapping for better readability.

7. Example Results Table Format:
| Request Input | Response Output |
|-------------------------------|------------------------------------------------------|
| Valid JSON with query | {"status": "success", "UserQuery": "example"} |
| Empty request body | {"status": "error", "message": "Empty request body"} |
| Malformed JSON | {"status": "error", "message": "JSON decode error"} |
| Unexpected data type | {"status": "error", "message": "Error processing request"} |

8. Tools and Libraries:
- Use unittest for creating and running the tests.
- Use pandas and openpyxl for saving results to an Excel file.
- Use tabulate for printing the results table in the console.

9. Additional Requirements:
- Ensure the test file is self-contained and can be executed independently.
- Include necessary imports and setup code to facilitate test execution.
