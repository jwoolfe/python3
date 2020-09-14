#!/usr/bin/env python3

import sanic
import csv
import game

server = sanic.Sanic("Wizard Pie")
server.static("/favicon.svg", "/srv/favicon.svg")
server.static("/main.css", "/srv/main.css")

HEAD = ''' <!DOCTYPE html>
            <html>
            <head>
                <title> Wizard Pie </title>
                <link rel="icon" type="image/svg+xml" href="/favicon.svg">
                <link rel="stylesheet" type="text/css" href="/main.css">
            </head>
            <body>\n'''

FORM = ''' <form id="wizard" action="/" method="post">
              <label for="task">What should I do?</label>
              <input type="text" id="task" name="task">
              <input id="submit_action" class="button" type="submit" value="+">
            </form>\n'''

TAIL = ''' </body>
            </html>'''


@server.route("/", methods=['POST', 'GET'])
async def wiz_action(request):
    wiz = game.load('wiz.save')

    args = request.args
    form = request.form
    for key in form:
        if key in args:
            args[key] += form[key]
        else:
            args[key] = form[key]

    if 'task' in args:
        task = args['task'][0].strip().lower()
    else:
        task = False

    page = HEAD + FORM

    if task:
        page += game.request(wiz, task).replace("\n", "<br/>")
 
    page += TAIL

    game.save(wiz)

    return sanic.response.html(page)


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8003)
