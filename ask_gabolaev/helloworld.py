
def application(env, start_response):
  start_response(
    '200 OK',
    (
      ('Content-Type', 'text/html'),
    )

  )
  
  returnString = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>This file is showed by gunicorn. Hello world!</body></html>']
  return returnString
