from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        # added font
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <style>

            # original styles

            # form {{
            #     background-color: #eee;
            #     padding: 20px;
            #     margin: 0 auto;
            #     width: 540px;
            #     font: 16px sans-serif;
            #     border-radius: 10px;
            # }}
            #
            # textarea {{
            #     margin: 10px 0;
            #     width: 540px;
            #     height: 120px;
            # }}

            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                font-family: 'Roboto', sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

            .wrapper {{
                width: 100%;
                display: block;
                margin: 0 auto;
                padding-top: 50px;
            }}

            h1 {{
                font-weight: 300;
                text-align: center;
                font-family: 'Roboto', sans-serif;
            }}

            p {{
                width: 500px;
                display: block;
                margin: 0 auto;
                text-align: center;
                font-family: 'Roboto', sans-serif;
                padding: 10px 0 50px 0;
            }}

        </style>
    </head>
    <body>
        # added wrapper, title, and description of application.
        <div class="wrapper">
            <h1>Web Caesar Cipher</h1>
            <p>A web application that utilizes the caesar cipher. Type in a message and the amount of rotation to encrypt your message!</p>
            <form action ="/" method="POST">
                <label for "rot">Rotate by:</label>
                <input type="text" id="rot" name="rot" value="0">
                <textarea name="text">{0}</textarea>
                <input type="submit" value="Submit Query">
            </form>
        </div>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_text = rotate_string(rot_text, rot)
    return form.format(encrypt_text)

app.run()
