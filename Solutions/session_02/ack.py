def ack(m, n):
    """Perfom Ackermann function calculation."""
    if m < 0 or n < 0:
        return None
    elif not m:
        return n + 1
    elif not n:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
