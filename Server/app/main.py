from FilterAPI import app

if __name__ == "__main__":
    # run the server
    app.run('0.0.0.0', 5000, debug=True)
