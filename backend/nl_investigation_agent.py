def investigate_query(query):

    query = query.lower()

    if "high risk" in query:
        return "Showing all high risk investigations"

    elif "duplicate invoice" in query:
        return "Showing duplicate invoice cases"

    elif "vendor risk" in query:
        return "Showing high risk vendors"

    elif "fraud" in query:
        return "Showing fraud detection results"

    return "No matching investigation found"