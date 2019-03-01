import responder

api = responder.API(static_dir="../build/static", static_route="/static", templates_dir="../build")

# @api.route("/{greeting}")
# async def greet_world(req, resp, *, greeting):
#     resp.text = f"{greeting}, world!"

api.add_route("/", static=True)

# @api.route("/admin")
# async def greet_world(req, resp):
#     resp.content = api.template('admin.html')


if __name__ == '__main__':
    api.run(port=3001)