from flask import Flask, render_template, request
from urllib.parse import urlsplit
import ipaddress

app = Flask(__name__)


def validate_target(target):
    """Validate a URL without sending any network request."""

    target = target.strip()

    if not target:
        return False, "Please enter a target URL."

    try:
        parsed = urlsplit(target)

        if parsed.scheme not in ("http", "https"):
            return False, "Only HTTP and HTTPS URLs are allowed."

        if not parsed.hostname:
            return False, "Please enter a valid hostname."

        if parsed.username or parsed.password:
            return False, "URLs containing login credentials are not allowed."

        if parsed.port is not None and not (1 <= parsed.port <= 65535):
            return False, "Invalid port number."

        hostname = parsed.hostname

        # Reject malformed IP addresses.
        try:
            ipaddress.ip_address(hostname)
        except ValueError:
            if not all(
                part and len(part) <= 63
                and part[0].isalnum()
                and part[-1].isalnum()
                and all(c.isalnum() or c == "-" for c in part)
                for part in hostname.rstrip(".").split(".")
            ):
                return False, "Invalid hostname."

        return True, "Target URL format is valid."

    except ValueError:
        return False, "Invalid URL format."


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    target = ""

    if request.method == "POST":

        target = request.form.get("target", "")
        authorized = request.form.get("authorized")

        if not authorized:
            result = {
                "status": "error",
                "message": "Please confirm that you have permission to test this target."
            }

        else:
            valid, message = validate_target(target)

            if valid:
                result = {
                    "status": "success",
                    "message": message
                }
            else:
                result = {
                    "status": "error",
                    "message": message
                }

    return render_template(
        "index.html",
        result=result,
        target=target
    )


if __name__ == "__main__":
    app.run(debug=True)