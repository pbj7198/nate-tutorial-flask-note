from diary import create_app


# Create App
app = create_app()

# run
if __name__=="__main__":

    app.run(debug=False, port = 5001)