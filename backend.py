# server backend
# REST interface using bottle
# sqlalchemy middleware
# sqlite backend (for now)

# Account Types
# Revenue
# Expense
# Owners Equity
# Asset
# Liability

from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)
