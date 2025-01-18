from contextlib import contextmanager


@contextmanager
def ExplainBlock(msg, width=50, char="*"):
    msg = f" {msg} "
    leftover_chars = width - len(msg)
    left_chars = leftover_chars // 2
    if max(left_chars, 0):
        right_chars = leftover_chars - left_chars
    else:
        right_chars = 0
    title_msg = f"{left_chars*char}{msg}{right_chars*char}"
    print(title_msg)
    yield
    print(char * len(title_msg))
