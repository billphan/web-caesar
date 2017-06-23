from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>

    <head>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <style>

            form {{
                width: 540px;
                padding: 20px;
                margin: 0 auto;
                border-radius: 10px;
                font: 16px sans-serif;
                background-color: #90AFC5;
                font-family: 'Roboto', sans-serif;
            }}

            textarea {{
                width: 100%;
                height: 150px;
                margin: 8px 0;
                border-radius: 4px;
                padding: 12px 20px;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}

            h1 {{
                font-weight: 300;
                padding-top: 75px;
                text-align: center;
                font-family: 'Roboto', sans-serif;
            }}

            p {{
                width: 500px;
                color: #888;
                display: block;
                margin: 0 auto;
                text-align: center;
                padding-bottom: 40px;
                font-family: 'Roboto', sans-serif;
            }}

            input[type=text], select {{
                width: 100%;
                margin: 8px 0;
                padding: 12px 20px;
                border-radius: 4px;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}

            input[type=submit] {{
                width: 100%;
                color: white;
                border: none;
                margin: 8px 0;
                cursor: pointer;
                padding: 14px 20px;
                border-radius: 4px;
                background-color: #2A3132;
            }}

            input[type=submit]:hover {{
                background-color: #336B87;
            }}

        </style>

    </head>

    <body>

        <h1>Web Caesar</h1>
        <p>A web application that utilizes the caesar cipher. Type in a message and the amount of rotation to encrypt your message!</p>

        <form action ="/" method="POST">
            <label for "rot">Rotate by:</label>
            <input type="text" id="rot" name="rot" value="0">
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Encrypt">
        </form>

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
