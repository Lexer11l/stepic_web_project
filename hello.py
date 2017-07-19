def wsgi_application(environ, start_response):
    raw_uri = str(environ.get('RAW_URI'))

    raw_uri = raw_uri[2:]

    params = raw_uri.split('&')

    data = ''
    for param in params:
        data += param + '\r\n'


    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ("Content-Length", str(len(data)))
    ]
    start_response(status, headers )
    return iter([data])