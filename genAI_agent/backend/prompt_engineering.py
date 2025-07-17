def build_email_prompt(user_request: str) -> str:
    """
    Given a short user request, return a well-structured prompt for the LLM to generate a professional email.
    """
    base_prompt = (
        "You are an AI assistant that writes professional emails. "
        "Given the following request, draft a clear, polite, and concise email. "
        "If the request is vague, make reasonable assumptions.\n"
        f"Request: {user_request}\n"
        "Email:"
    )
    return base_prompt 