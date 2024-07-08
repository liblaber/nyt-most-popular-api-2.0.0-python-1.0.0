from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


class Request:
    def __init__(self, method, url, headers, body=""):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Request(method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )


class CustomHook:

    def before_request(self, request: Request, **kwargs):
        request.url = append_query_param(request.url, "api-key", kwargs["api_key"])

    def after_response(self, request: Request, response: Response, **kwargs):
        request

    def on_error(
        self, error: Exception, request: Request, response: Response, **kwargs
    ):
        print("on_error")


def append_query_param(url, key, value):
    # Parse the URL into components
    url_parts = urlparse(url)

    # Parse the query string into a list of (key, value) tuples
    query_params = dict(parse_qsl(url_parts.query))

    # Add or update the query parameter
    query_params[key] = value

    # Reconstruct the query string
    new_query = urlencode(query_params)

    # Reconstruct the URL with the new query string
    new_url_parts = url_parts._replace(query=new_query)
    new_url = urlunparse(new_url_parts)

    return new_url
