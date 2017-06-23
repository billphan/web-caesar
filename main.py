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

            body {{
                background-color: #fff;
            }}

            div.wrapper {{
                top: 40%;
                left: 50%;
                width: 540px;
                display: block;
                margin: 0 auto;
                position: fixed;
                transform: translate(-50%, -50%)
            }}

            form {{
                width: 100%;
                display: block;
                margin: 0 auto;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Roboto', sans-serif;
            }}

            textarea {{
                width: 100%;
                height: 150px;
                margin: 8px 0;
                border-radius: 4px;
                padding: 12px 20px;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}

            h1 {{
                color: #336B87;
                font-weight: 300;
                text-align: left;
                font-family: 'Roboto', sans-serif;
            }}

            p {{
                color: #000;
                width: 540px;
                display: block;
                margin: 0 auto;
                font-size: 14px;
                text-align: left;
                padding-bottom: 20px;
                font-family: 'Roboto', sans-serif;
            }}

            hr {{
                border: 0;
                padding: 0 0 15px 0;
                width: 100%;
                height: 1px;
                opacity: 0.5;
                display: block;
                margin: 0 auto;
                border-top: 1px solid #aeaeae;
            }}

            label {{
                font-size: 14px;
                color: #aeaeae;
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

            .footer {{
                left: 0;
                bottom: 0;
                width: 100%;
                height: 50px;
                position: absolute;
            }}

            .footer p {{
                color: #aeaeae;
                text-align: center;
                padding: 35px 0 0 0;
            }}

        </style>

    </head>

    <body>

        <div class="wrapper">

            <h1>&#128274; Web Caesar Cipher</h1>

            <p>A web application that utilizes the caesar cipher. Type in a message and the amount of rotation to encrypt your message!</p>

            <hr>

            <form action ="/" method="POST">
                <label>Enter Message to Encrypt:</label>
                <textarea name="text">{0}</textarea>
                <label for "rot">Enter Amount to Rotate:</label>
                <input type="text" id="rot" name="rot" value="0">
                <input type="submit" value="Encrypt">
            </form>

        </div>

        <div class="footer">
            <p class="footer">Created using Python and Flask. Designed by Bill Phan.</p>
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
