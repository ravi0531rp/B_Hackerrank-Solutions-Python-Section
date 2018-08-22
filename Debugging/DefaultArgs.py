def print_from_stream(n, stream=None):
    stream = OddStream() if stream else EvenStream()
    for _ in range(n):
        print(stream.get_next())
