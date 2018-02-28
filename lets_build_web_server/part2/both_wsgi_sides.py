def run_application(application):
    """Server code"""
    # This is where an application/framework stores an HTTP status
    # and HTTP response headers for the server to transmit to the client
    headers_set = []
    # Environment dictionary with WSGI/CGI variables
    environ = {}

    def start_response(status, response_headers):
        headers_set[:] = [status, response_headers]

    # Server invokes the 'application' callable and gets back the response body
    result = application(environ, start_response)
    # Server builds an HTTP response and transmits it to the client


def app(environ, start_response):
    """A barebones WSGI app."""
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello world!']


run_application(app)

# Here is how it works:
# 1. The framework provides an ‘application’ callable
#   (The WSGI specification doesn't prescribe how that should be implemented)
# 2. The server invokes the 'application' callable for each request it receives
#       from an HTTP client. It passes a dictionary 'environ' containing
#       WSGI/CGI variables and a 'start_response' callable as arguments
#       to the 'application' callable.
# 3. The framework/application generates an HTTP status and HTTP response
#       headers and passes them to the 'start_response' callable for the server
#       to store them. The framework/application also returns a response body.
# 4. The server combines the status, the response headers, and the response
#       body into an HTTP response and transmits it to the client
#       (This step is not part of the specification but it’s the next
#       logical step in the flow and I added it for clarity)
