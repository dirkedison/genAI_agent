def build_email_prompt(user_request: str, tone: str = "Formal") -> str:
    """
    Given a short user request and a tone, return a well-structured prompt for the LLM to generate a professional email.
    """
    base_prompt = (
        f"You are an AI assistant that writes professional emails in a {tone.lower()} tone. "
        "Given the following request, draft a clear, polite, and concise email. "
        "If the request is vague, make reasonable assumptions.\n"
        f"Request: {user_request}\n"
        "Email:"
    )
    return base_prompt 