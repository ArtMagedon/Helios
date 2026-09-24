from flask import Flask, redirect, render_template, request, send_file, session
import os
import json
import requests

app = Flask(__name__)
app.secret_key = "secret-key"

pages = ["/", "/pages/aboutme/summary",
         "/pages/aboutme/academic-experience", "/pages/aboutme/aboutme", "/pages/home",
         "/pages/aboutme/professional_achievement", "/pages/MS/ISCOS", "/pages/MS/MSCOM",
         "/pages/MP/MPWE", "/pages/projects/webConfig", "/api/feedback", 
         "/pages/aboutme/contacts","/pages/motivation"]

# =======================   Bot   =======================


def send_to_telegram(data: dict):
    # Отправка пользователю 
    with open("bot-api.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    bot_token = config["bot_token"]
    chat_id = config["chat_id"]

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"От: {data["name"]}\n\nСообщение:\n{data["message"]}",
        "parse_mode": "HTML"
    }

    response = requests.post(url, json=payload)

    return response.json()

# =======================   base   =======================


@app.route("/")
def base():
    page = session.pop("page", "home")
    return render_template("base.html", page=page)

# =======================   main_page   =======================


@app.route("/pages/home")
def home():
    return render_template("pages/home.html")

# =======================   MS   =======================


@app.route("/pages/MS/ISCOS")
def ISCOS():
    return render_template("pages/MS/ISCOS.html")


@app.route("/pages/MS/MSCOM")
def MSCOM():
    return render_template("pages/MS/MSCOM.html")


@app.route("/pages/MS/MSDisplay")
def MSDisplay():
    return render_template("pages/MS/MSDisplay.html")

# =======================   MP   =======================


@app.route("/pages/MP/MPCDE")
def MPCDE():
    return render_template("pages/MP/MPCDE.html")


@app.route("/pages/MP/MPWE")
def MPW():
    return render_template("pages/MP/MPWE.html")


@app.route("/pages/MP/MPTP")
def MPTP():
    return render_template("pages/MP/MPTP.html")

# =======================   other projects   =======================


@app.route("/pages/projects/webConfig")
def webConfig():
    return render_template("pages/projects/webConfig.html")

# =======================   aboutme   =======================


@app.route("/pages/aboutme/summary")
def summary():
    return render_template("pages/aboutme/summary.html")


@app.route("/pages/aboutme/contacts")
def suwmmary():
    return render_template("pages/aboutme/contacts.html")


@app.route("/pages/aboutme/academic-experience")
def acad2emic():
    return render_template("pages/aboutme/academic_experience.html")


@app.route("/pages/aboutme/professional_achievement")
def academic():
    return render_template("pages/aboutme/professional_achievement.html")


@app.route("/pages/aboutme/aboutme")
def aboutme():
    return render_template("pages/aboutme/aboutme.html")

# =======================   files   =======================


@app.route("/file/reference_letter")
def reference_letterFile():
    return send_file(
        "files/reference_letter.pdf",
        as_attachment=True
    )

@app.route("/file/portfolio")
def portfolioFile():
    return send_file(
        "files/portfolio.rar",
        as_attachment=True
    )

@app.route("/file/summary")
def summaryFile():
    return send_file(
        "files/Попов А.Р резюме.pdf",
        as_attachment=True
    )

# =======================   before_request   =======================


@app.before_request
def require_login():
    notallowed_paths = ()
    if request.path.startswith(notallowed_paths):
        return redirect("/")
    if request.path.startswith("/static/"):
        return
    if request.path.startswith("/file/"):
        return
    if request.path.startswith("/favicon.ico"):
        return
    if request.path.startswith("/popup"):
        return
    if request.path.startswith("/motivation"):
        session["page"] = "motivation"
        return redirect("/")
    if request.path.startswith("/pages/"):
        if request.path not in pages:
            return render_template(
                "partials/no_content.html", url=request.path[request.path.rfind("/")+1:])
    if request.path not in pages:
        return redirect("/")
    return

# =======================   popup   =======================


@app.route("/popup/photo/<path:filename>")
def popup_photo(filename):

    filename = filename.replace("/popup/photo/", "")

    return render_template(
        "pages/popup_photo.html",
        filename=filename
    )


@app.route("/popup/close")
def popup_close():

    return ""
# =======================   API   =======================

@app.route("/api/feedback", methods=['POST'])
def api_feedback():
    data = {
        "name": request.form.get("name"),
        "message": request.form.get("message")
    }

    send_to_telegram(data)

    return "", 200

# =======================   other   =======================

@app.route("/pages/motivation")
def motivation():
    return render_template("pages/motivation.html")

# =======================   start   =======================


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=False)
