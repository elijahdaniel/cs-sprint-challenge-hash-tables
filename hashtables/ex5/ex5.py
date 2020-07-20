# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for paths in files:
        slashes = paths.split('/')

        word = slashes[-1]

        if word not in cache:
            cache[word] = []
        
        cache[word].append(paths)

    for query in queries:
        if query in cache:
            result += cache[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
