from flask import Flask
import router


app = Flask(__name__)
router.init(app)

app.run("127.0.0.1", port=9999)
