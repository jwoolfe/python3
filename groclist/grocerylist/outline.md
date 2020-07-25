# Groclist or Groklist

this will be a website
it will present a list of items
it will let you update the list (add or delete or change items)
it will let you filter the list (by some trait)

we would like it to authenticate users, but that can happen later

we would like a command-line interface that can connect

## Website Pseudo Coding

1. someone's web browser asks for the URL from the server
2. server returns a landing page

  * acquire the URL the client is requesting
  * translate the URL into "what to show" to the client
  * shows "that" to the client

### example URLS

/groclist.html
/groclist.html?add=Peanut%20Butter
/groclist.html?del=12
/groclist.html?addtag=frozen&item=11
/groclist.html?deltag=frozen&item=11

### Translate URL into what to show

Assume "/groclist.html?add=Peanuts"

    url = ^^^
    (page, parameters) = url.split("?")
    # page = "/groclist.html"
    # parameters = "add=Peanuts"
    parameters = parameters.split("&")
    # parameters = ["add=Peanuts",]
    args = {}
    for p in parameters:
        (name, value) = p.split("=")
        # name = "add"
        # value = "Peants"
        args[name] = value

1. separate the first part from the second part (split on the question mark)
2. separate the parameters from each each other (split on ampersand)
3. loop through the parameters and break each out into a name and a value
4. check to see if there is an "add" parameter

    * if so, add whatever the value is


    from sanic import Sanic
    app = Sanic("groclist")

    @app.route("/groclist.html")
    async def homepage(request):
        args = request.args
        # args = {"add": "Peanuts"}
        if "add" in args:
            ## do something to add args["add"] to the database

