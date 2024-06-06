from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os
import webbrowser

model = genai.GenerativeModel('gemini-pro')


#my_api_key_gemini = os.getenv('AIzaSyDTXD3Kjtz5rYoBpSrGKOqSX6wvebJZciY')

genai.configure(api_key="AIzaSyDTXD3Kjtz5rYoBpSrGKOqSX6wvebJZciY")

app = Flask(__name__)

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt

            if 'open youtube' in question:
                webbrowser.open("https://www.youtube.com/")
            elif 'open google' in question:
                webbrowser.open("https://www.google.com")
            elif 'play music' in question:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)