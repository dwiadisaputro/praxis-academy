from flask import render_template
from flask.views import View, User
@app.route('/usesrs/')
def show_user(page):
    users = User.query.all()
    return render_template('users.html', users=users)

class ShowUsers(View):
    def dispatch_request(self):
        user = User.query.all()
        return render_template('users.html', object=users)
app.add_url_rule('/user/', view_func=ShowUsers.as_view('show_user'))