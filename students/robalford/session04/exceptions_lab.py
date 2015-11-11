def safe_input(prompt):
    try:
        safe_input = input(prompt)
    except KeyboardInterrupt:
        return
    else:
        return safe_input
