from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./templates")

@app.route("/", methods=["POST", "GET"])
def number_guessing():
    if request.method == "POST":
        min = float(request.form["min"])
        max = float(request.form["max"])
        user_answer = request.form["user_answer"]
        guessed_num = request.form["guess"]
        if user_answer == "too_big":
            max = float(guessed_num)
        elif user_answer == "too_small":
            min = float(guessed_num)
        else:
            return "Yay, I've guessed correctly!"

        # checking if due to the user's choices min and max do not change and the game is still not resolved
        # prevents the game for continuing infinitely
        if min == max or max == min + 1:
            return "Do not lie to me."

    else:
        min = 0
        max = 1000
    guessed_num = (max - min) / 2 + min
    return render_template("guess_num.html", min=min, max=max, guessed_num=int(guessed_num))


if __name__ == "__main__":
    app.run(debug=True)


