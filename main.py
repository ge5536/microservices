from flask import Flask, request
import random
import json

jokes = ["What animal loves a baseball game? A bat.",
             "What did the Dalmatian say after finishing her breakfast? That hit the spot.",
             "What is black and white and red all over? An embarrassed zebra.",
             "Where is a cow's favorite place to go? The moooovies.",
             "What do you call an alligator that solves mysteries? An investi-gator.",
             "Why didn't the frog park his car on the street? He didn't want to get toad.",
             "What's a cat's favorite color? Purrr-ple.",
             "What do ducks love to put in their soup? Quackers.",
             "Why did the lion spit out the clown? He tasted funny.",
             "What has six eyes but cannot see? Three blind mice.",
             "What is an astronaut's favorite key on a keyboard? The spacebar.",
             "How do you know when the moon has had enough to eat? When it's full.",
             "What do planets love to read? Comet books."]

app = Flask(__name__)
@app.route('/joke/', methods=['GET', 'POST'])
def random_joke():
    # Check if no arguments, return one joke
    if len(request.args) == 0:
        return json.dumps({"joke body": random.choice(jokes)})
    # Check for "num" argument being int - otherwise return error
    try:
        int(request.args.get('num'))
    except ValueError:
        print("Request argument not valid")
        return "Request argument not valid"
    # If passed exception handling, return amount of jokes requested
    return json.dumps({"joke body": random.choices(jokes, k=int(request.args.get('num')))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
