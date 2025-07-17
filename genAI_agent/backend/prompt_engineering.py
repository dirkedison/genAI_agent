def build_email_prompt(user_request: str, tone: str = "Formal", recipient: str = "", subject: str = "") -> str:
    """
    Given a short user request, tone, recipient, and subject, return a well-structured prompt for the LLM to generate a professional email.
    """
    details = []
    if recipient:
        details.append(f"Recipient: {recipient}")
    if subject:
        details.append(f"Subject: {subject}")
    details_str = "\n".join(details)
    base_prompt = (
        f"You are an AI assistant that writes professional emails in a {tone.lower()} tone. "
        "Given the following request, draft a clear, polite, and concise email. "
        "If the request is vague, make reasonable assumptions.\n"
        f"{details_str}\n"
        f"Request: {user_request}\n"
        "Email:"
    )
    return base_prompt 