#!/usr/bin/env python

from app import app

if __name__ == '__main__':
    if app.debug:
        app.run(debug=True)
    else:
        app.run(host='localhost')