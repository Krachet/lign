from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Fill in your name", boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        Firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('m ngu a ?', category='error')
        if len(Firstname) < 2:
            flash('m ngu a ?', category='error')
        if len(password1) < 8:
            flash('ngan nhu chim may y', category='error')
        if password2 != password1:
            flash('viet lai cung khong xong', category='error')
        else:
            flash('chuc mung cuoi cung m cung thanh cong', category='success')

    return render_template("signup.html")
