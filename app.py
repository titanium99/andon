from flask import Flask, render_template, redirect, url_for
import blinkt
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on', methods=['POST'])
def on_switch():
    blinkt.set_clear_on_exit()
    blinkt.set_brightness(0.3)
    blinkt.set_all(255,60,0)
    blinkt.show()
    return redirect(url_for('index')) 

@app.route('/off', methods=['POST'])
def off_switch():
    blinkt.set_clear_on_exit()
    blinkt.clear()
    blinkt.set_all(0,0,0)
    blinkt.show()
    return redirect(url_for('index')) 

@app.route('/on_max', methods=['POST'])
def on_max_switch():
    blinkt.set_clear_on_exit()
    blinkt.set_brightness(1)
    blinkt.set_all(255,70,0)
    blinkt.show()
    return redirect(url_for('index')) 


@app.route('/on_timer', methods=['POST'])
def on_timer_switch(st=600, gain=120):
    blinkt.set_clear_on_exit()
    brt = 0.5
    blinkt.set_brightness(brt)
    brtgain = brt / gain
    while st>0:
        if st < gain:
            brt = brt - brtgain
            blinkt.set_brightness(brt)
        blinkt.set_all(255,60,0)
        blinkt.show()
        st -= 1
        time.sleep(1)
    off_switch()
    return redirect(url_for('index')) 

