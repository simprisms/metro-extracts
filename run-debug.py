#!/usr/bin/env python
from App.web import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
