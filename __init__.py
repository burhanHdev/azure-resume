import azure.functions as func
import json

def main(req: func.HttpRequest, inputDocument: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    if not inputDocument or len(inputDocument) == 0:
        return func.HttpResponse("Document not found", status_code=404)
    
    # Access the first document in the DocumentList
    doc = inputDocument[0]

    # Increment the count
    # Note: Assuming 'count' is a field in your document. Adjust as necessary.
    doc['counter'] += 1

    # Prepare the document for the output binding
    # Since output bindings expect a single Document, you can directly set it
    outputDocument.set(doc)

    return func.HttpResponse(json.dumps({"counter": doc['counter']}), status_code=200, mimetype="application/json")

