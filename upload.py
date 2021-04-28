from flask import Flask, render_template, request, redirect, url_for, abort
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB
app.config['UPLOAD_EXTENSIONS'] = [ '.jpg', '.png', '.gif'
                                  , '.pdf', '.csv'
                                  , '.xls', '.xlsx'
                                  , '.doc', '.docx'
                                  , '.ppt', '.pptx'
                                  ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    for uploaded_file in request.files.getlist('file'):
        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=9000, host='0.0.0.0')

