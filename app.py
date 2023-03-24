from evergreen_analitica import app

if __name__ == '__main__':
    print("> Server running on: ")
    app.run(host='0.0.0.0', port=80)