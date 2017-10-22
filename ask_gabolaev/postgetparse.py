from cgi import parse_qs


def application(env, start_response):
  start_response(
    '200 OK',
    (
      ('Content-Type', 'text/plain'),
    )

  )
  if (env['REQUEST_METHOD'] == 'POST'):
    query = parse_qs(env['wsgi.input'].read())
    printingString = '\n'.join('%s = %s' % (i.decode('utf8'), j[0].decode('utf8')) for i, j in query.items())
  else:
    printingString = '\n'.join('{}'.format(i) for i in env['QUERY_STRING'].split('&'))
  return [('{}\n{}\n'.format(env['REQUEST_METHOD'], printingString)).encode('utf-8')]


