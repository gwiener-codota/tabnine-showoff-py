import argparse
import http.server
import functools


def start_server(
    port: int = 8080,
    directory: str = ".",
):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
    with http.server.HTTPServer(("", port), handler) as server:
        server.serve_forever()


if __name__ == '__main__':
    # read command line arguments and start server
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--directory', type=str, default=".")
    args = parser.parse_args()
    start_server(
        port=args.port,
        directory=args.directory
    )