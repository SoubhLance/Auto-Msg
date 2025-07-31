from flask import Flask, render_template, jsonify
import os
import subprocess
import threading

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route accessed")
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error: {e}")
        return f"Error loading template: {e}"

@app.route('/chat')
def chat():
    print("Chat route accessed")
    return render_template('index.html')

@app.route('/start-automation')
def start_automation():
    print("Start automation route accessed!")
    
    def run_main_py():
        try:
            print("Attempting to run main.py...")
            # Run main.py in the background
            result = subprocess.run(['python', 'main.py'], 
                                  capture_output=True, 
                                  text=True, 
                                  cwd=os.getcwd())
            print(f"main.py output: {result.stdout}")
            if result.stderr:
                print(f"main.py errors: {result.stderr}")
        except Exception as e:
            print(f"Error running main.py: {e}")
    
    # Run main.py in a separate thread so it doesn't block the web response
    thread = threading.Thread(target=run_main_py)
    thread.start()
    
    return jsonify({"status": "success", "message": "main.py started!"})

if __name__ == '__main__':
    # print("🚀 Starting Flask Chat Tester...")
    # print("📱 Open your browser and go to: http://localhost:5000")
    # print("🤖 Perfect for testing PyAutoGUI automation safely!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)