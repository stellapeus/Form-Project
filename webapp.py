from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")              
def render_main():
    return render_template('form.html')

@app.route("/response")
def render_page1():
    freetime_preferences = request.args['freetime_preferences']
    personality = request.args['personality']
    stress_handling = request.args['stress_handling']
    ideal_habitat = request.args['ideal_habitat']
    teamwork_thoughts = request.args['teamwork_thoughts']
    food_preference = request.args['food_preference']
    season_preference = request.args['season_preference']
    affection = request.args['affection']
    adventure = request.args['adventure']
    birdScore = 0
    penguinScore = 0
    if freetime_preferences == 'Exploring new places': 
        birdScore ++ 
    if freetime_preferences == 'Relaxing in the sun':
        penguinScore ++
    return render_template('page1.html')
    
if __name__=="__main__":
    app.run(debug=True)
    