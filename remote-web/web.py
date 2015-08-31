#!/usr/bin/env python

import lircplayback as playback
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/")
def index():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint)
            links.append((url, rule.endpoint))
    return render_template("all_links.html", links=links)


@app.route("/airplay/toggle")
def airplay_toggle():
    playback.airplay_toggle()
    return "toggling airplay"


@app.route("/tv/toggle")
def tv_toggle():
    playback.tv_toggle()
    return "toggling tv"


@app.route("/radio/toggle")
def radio_toggle():
    value = request.args.get('value')
    playback.toggle_radio(value)

    return "toggling radio. also you can use ?value=whatever here"


@app.route("/receiver/mute")
def receiver_mute():
    playback.receiver_togglemute()

    return "mute toggled"


@app.route("/receiver/set_volume")
def receiver_setvolume():
    value = request.args.get('value')

    if value is None:
        playback.receiver_setvolume(85)
    else:
        playback.receiver_setvolume(value)

    return "volume is changed. also you can use ?value=whatever here"


@app.route("/receiver/volume_up")
def receiver_volumeup():
    value = request.args.get('value')

    if value is None:
        playback.receiver_volumeup(5)
    else:
        playback.receiver_volumedown(value)

    return "volume up. also you can use ?value=whatever here"


@app.route("/receiver/volume_down")
def receiver_volumedown():
    value = request.args.get('value')

    if value is None:
        playback.receiver_volumedown(5)
    else:
        playback.receiver_volumedown(value)

    return "volume down. also you can use ?value=whatever here"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
