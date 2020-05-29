from flask import Flask, request
import tweepy
from checker_flask import check

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def postcode_check():
    if request.method == "POST":
        postcode = None
        postcode = int(request.form["postcode"])
        result = check(postcode)
        return '''
            <html>
                <body>
                    <p>{result}</p>
                    <p><a href="/">Again</a>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <body>
                <p>Postcode to check:</p>
                <form method="post" action=".">
                    <p><input name="postcode" /></p>
                    <p><input type="submit" value="Check" /></p>
                </form>
            </body>
        </html>
    '''