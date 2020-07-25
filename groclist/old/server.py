#!/usr/bin/env python3

import sanic

server = sanic.Sanic("GrocList")

@server.route("/")
async def index(request):
    url = request.url
    args = request.args

    msg = "Hello, World - \n"
    msg = msg + f"I see you arrived at the URL: {url}. \n"
    msg = msg + f" with these arguments: {args}"

    return sanic.response.text(msg)


@server.route("/groclist")
async def groclist(request):
    items = load()

    args = request.args
    if "add" in args:
        values = args["add"]
        for value in values:
            if value not in items:
                items.append(value)

    if "del" in args:
        values = args["del"]
        for value in values:
            if value in items:
                items.remove(value)

    save(items)
    msg = "\n".join(items)

def save(items):
    plain_text = "\n".join(items)
    the_file = open("/Users/jwoolfe/Documents/Git/python3/groclist/items.list", "w")
    the_file.write(plain_text)
    the_file.close()


def load():
    the_file = open("/Users/jwoolfe/Documents/Git/python3/groclist/items.list", "r")
    plain_text = the_file.read()
    items = plain_text.split("\n")
    return items



if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8003)
