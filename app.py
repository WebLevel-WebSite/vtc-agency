#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, session, jsonify, render_template

app = Flask(__name__,
            static_url_path='/media',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'your_secret_key'  # Change this to a secure key for security

YOUR_DOMAIN = 'http://localhost:4242'

# Sample product catalog with price_ids


@app.route('/')
def HOME():
    return render_template('index.html')

@app.route('/creation-site-web')
def web():
    return render_template('site-web.html')

@app.route('/expertises')
def expertises():
    return render_template('expertises.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')



#+++++++++++++++++++++++++++++ BLOG ++++++++++++++++++++++++++++++++++
@app.route('/blog//shopify-comment-et-pourquoi-l-utiliser')
def shopify():
    return render_template('/blog/shopify-comment-et-pourquoi-l-utiliser.html')

@app.route('/blog/15-termes-a-connaitre-dans-le-developpement-web')
def dev():
    return render_template('/blog/15-termes-a-connaitre-dans-le-developpement-web.html')

@app.route('/blog/qu-est-ce-qu-une-agence-web-digitale')
def webdev():
    return render_template('/blog/qu-est-ce-qu-une-agence-web-digitale.html')

@app.route('/blog/creer-un-site-wordpress-les-indispensables')
def word():
    return render_template('/blog/creer-un-site-wordpress-les-indispensables.html')

#+++++++++++++++++++++++++++++ PROJETS ++++++++++++++++++++++++++++++++++
@app.route('/projets/atalprestigevtc/')
def atal():
    return render_template('projets/atal.html')
@app.route('/projets/fabcabvtc/')
def  fabcab():
    return render_template('projets/fabcabvtc.html')
@app.route('/projets/dropout')
def dropout():
    return render_template('projets/dropout.html')
#+++++++++++++++++++++++++++++ CONDITION ET ERROR ++++++++++++++++++++++++++++++++++

@app.route('/mentions-legales')
def mentions():
    return render_template('mentions-legales.html')
@app.route('/cgu')
def cgu():
    return render_template('cgu.html')
@app.route('/cgv')
def cgv():
    return render_template('cgv.html')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=4242)

