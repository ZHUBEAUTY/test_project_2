ALLOWED = {
    "TODO": ["IN_PROGRESS"],
    "IN_PROGRESS": ["DONE"],
    "DONE": []
}

def validate_transition(current, nxt):
    if current == "DONE" and nxt == "IN_PROGRESS":
        return True

    return nxt in ALLOWED.get(current, [])
