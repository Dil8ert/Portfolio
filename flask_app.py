from flask import Flask,render_template,url_for,request,redirect
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter
import asyncio
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/contact",methods=['POST','GET'])
def contact():
    if(request.method == 'POST'):
        first_name = request.form.get("fname",False)
        last_name = request.form.get("lname",False)
        message = request.form.get("msg",False)
        city = request.form.get("city",False)
        webhook = Webhook.partial(1080312781141725194,'7PohXsZ3qrmR87L56XVFRovRpOFMBKmASFbkREYOAYclslae1gZ8DbPO2cLHkOCQ34xn',adapter=RequestsWebhookAdapter())
        embed = discord.Embed(title="Incoming Message", description="Welcome to NLP test", color=discord.Color.random())
        embed.add_field(name="First Name", value=first_name)
        embed.add_field(name="Last Name", value=last_name)
        embed.add_field(name="City", value=city)
        embed.add_field(name="Message ", value=message)
        webhook.send(embed=embed)
        return redirect(url_for("succes"))
    else:
        return render_template('contact.html')


@app.route("/contact")
def succes():
    return render_template('submission.html')