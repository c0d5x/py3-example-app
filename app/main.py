import sys
import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    outs = []
    outs.append("-=-=-=-=-")
    outs.append("OS info:")
    outs.append("OS Name = " + os.name)
    outs.append("ctermid = " + os.ctermid())
    outs.append("uname = " + str(os.uname()))
    outs.append("UID = " + str(os.getuid()))
    outs.append("CPU Count = " + str(os.cpu_count()))

    outs.append("-=-=-=-=-")
    outs.append("Arguments:")
    i = 0
    for a in sys.argv:
        outs.append(str(i) + " = " + str(a))
        i += 1

    outs.append("-=-=-=-=-")
    outs.append("Environment Variables:")
    items = os.environ.items()
    for i in items:
        outs.append(str(i[0] + " = " + i[1]))

    outs.append("-=-=-=-=-")
    return "\n".join(outs)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
