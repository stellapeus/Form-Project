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
    wolfScore = 0
    polarbearScore = 0
    monkeyScore = 0
    beaverScore = 0
    slothScore = 0
    elephantScore = 0
    goatScore = 0
    bearScore = 0
    dogScore = 0
    
    if freetime_preferences == 'Exploring new places': 
        wolfScore ++
        elephantScore ++
    if freetime_preferences == 'Relaxing in the sun':
        polarbearScore ++
        slothScore ++
        bearScore ++
    if freetime_preferences == 'Socializing with friends':
        dogScore ++
        goatScore ++
    if freetime_preferences == 'Working on a project':
        beaverScore ++
        monkeyScore ++
        
        
    if personality == 'Adventurous and spontaneous':
        monkeyScore ++
        elephantScore ++
    if personality == 'Calm and nurturing':
        beaverScore ++
        slothScore ++
    if personality == 'Playful and energetic':
        polarbearScore ++
        dogScore ++
    if personality == 'Loyal and protective':
        wolfScore ++
        goatScore ++
        bearScore ++
        
        
    if stress_handling == 'Go for a run or exercise':
        wolfScore ++
        bearScore ++
    if stress_handling == 'Meditate or take a nap':
        polarbearScore ++
        slothScore ++
        elephantScore ++
    if stress_handling == 'Hang out with friends':
        beaverScore ++
        monkeyScore ++
    if stress_handling == 'Take charge and tackle the problem':
        dogScore ++
        goatScore ++
        
        
    if ideal_habitat == 'Mountains and forests':
        beaverScore ++
        goatScore ++
        wolfScore ++
    if ideal_habitat == 'Jungles and swamps':
        slothScore ++
        monkeyScore ++
    if ideal_habitat == 'Desert and flatland':
        elephantScore ++
        dogScore ++
    if ideal_habitat == 'Cold and snowy':
        polarbearScore ++
        bearScore ++
        
        
    if teamwork_thoughts == 'I prefer to go solo':
        wolfScore ++
        bearScore ++
        goatScore ++
    if teamwork_thoughts == 'I love collaborating with others':
        beaverScore ++
        polarbearScore ++
    if teamwork_thoughts == 'I enjoy leading the group':
        monkeyScore ++
        dogScore ++
    if teamwork_thoughts == 'I am a supportive team player':
        elephantScore ++
        slothScore ++
        
        
    if food_preference == 'Hearty and filling':
        bearScore ++
        dogScore ++
    if food_preference == 'Fresh and healthy':
        beaverScore ++
        elephantScore ++
    if food_preference == 'Sweet and indulgent':
        monkeyScore ++
        wolfScore ++
    if food_preference == 'Simple and classic':
        polarbearScore ++
        slothScore ++
        goatScore ++
        
        
    if season_preference == 'Spring':
        elephantScore ++
        monkeyScore ++
        slothScore ++
    if season_preference == 'Summer':
        wolfScore ++
        dogScore ++
    if season_preference == 'Fall':
        goatScore ++
        beaverScore ++
    if season_preference == 'Winter':
        bearScore ++
        polarbearScore ++
        
        
    if affection == 'Through playful teasing':
        bearScore ++
        dogScore ++
        beaverScore ++
    if affection == 'With gentle gestures':
        elephantScore ++
        slothScore ++
    if affection == 'By spending quality time':
        monkeyScore ++
        polarbearScore ++
    if affection == 'By protecting and supporting':
        wolfScore ++
        goatScore ++
        
        
    if adventure == 'Hiking in the wilderness':
        goatScore ++
        dogScore ++
    if adventure == 'Relaxing by the water':
        bearScore ++
        beaverScore ++
        slothScore ++
    if adventure == 'Exploring a new environment':
        wolfScore ++
        elephantScore ++
    if adventure == 'Attending a fun gathering':
        monkeyScore ++
        polarbearScore ++
    return render_template('page1.html')
    
if __name__=="__main__":
    app.run(debug=True)
    