#!/usr/bin/env python3

import sanic

server = sanic.Sanic("GrocList")
server.static("/favicon.ico", "./favicon.ico")

HEAD = ''' <!DOCTYPE html>
            <html>
            <head>
                <title> Groc List </title>
                <link rel="icon" type="image/png" href="/favicon.ico">
            </head>
            <body> '''

FORM = ''' <form action="/groclist" method="get">
              <label for="add">Item to Add</label>
              <input type="text" id="add" name="add">
              <input type="submit" value="Submit">
            </form>'''

TAIL = ''' </body>
            </html> '''

@server.route("/")
async def index(request):
    url = request.url
    args = request.args

    msg = HEAD
    msg += f"""
            <p>Hello, World!</p>
            <p>I see you arrived at the URL: {url}.</p>
            <p>And with these arguments: {args}</p>
            """
    msg += TAIL

    return sanic.response.html(msg)


@server.route("/groclist")
async def groclist(request):
    items = load()

    args = request.args
    if "add" in args:
        values = args["add"]
        for value in values:
            value = value.title()
            if value not in items:
                items.append(value)

    if "del" in args:
        values = args["del"]
        for value in values:
            value = value.title()
            if value in items:
                items.remove(value)

    save(items)

    msg = HEAD + FORM
    msg += ''' <ul> '''
    for item in items:
        msg += f"<li>{item}</li>"
    msg += ''' </ul> '''
    msg += TAIL

    return sanic.response.html(msg)


def save(items):
    plain_text = "\n".join(items)
    the_file = open("./items.list", "w")
    the_file.write(plain_text)
    the_file.close()


def load():
    the_file = open("./items.list", "r")
    plain_text = the_file.read()
    items = plain_text.split("\n")
    return items


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8003)
