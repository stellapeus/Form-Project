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
    capybaraScore = 0
    beaverScore = 0
    slothScore = 0
    kangarooScore = 0
    cougarScore = 0
    arcticfoxScore = 0
    wildboarScore = 0
    
    if freetime_preferences == 'Exploring new places': 
        wolfScore ++
        kangarooScore ++
    if freetime_preferences == 'Relaxing in the sun':
        polarbearScore ++
        slothScore ++
        arcticfoxScore ++
    if freetime_preferences == 'Socializing with friends':
        wildboarScore ++
        cougarScore ++
    if freetime_preferences == 'Working on a project':
        beaverScore ++
        capybaraScore ++
        
        
    if personality == 'Adventurous and spontaneous':
        capybaraScore ++
        kangarooScore ++
    if personality == 'Calm and nurturing':
        beaverScore ++
        slothScore ++
    if personality == 'Playful and energetic':
        polarbearScore ++
        wildboarScore ++
    if personality == 'Loyal and protective':
        wolfScore ++
        cougarScore ++
        arcticfoxScore ++
        
        
    if stress_handling == 'Go for a run or exercise':
        wolfScore ++
        arcticfoxScore ++
    if stress_handling == 'Meditate or take a nap':
        polarbearScore ++
        slothScore ++
        kangarooScore ++
    if stress_handling == 'Hang out with friends':
        beaverScore ++
        capybaraScore ++
    if stress_handling == 'Take charge and tackle the problem':
        wildboarScore ++
        cougarScore ++
        
        
    if ideal_habitat == 'Mountains and forests':
        beaverScore ++
        cougarScore ++
        wolfScore ++
    if ideal_habitat == 'Jungles and swamps':
        slothScore ++
        capybaraScore ++
    if ideal_habitat == 'Desert and flatland':
        kangarooScore ++
        wildboarScore ++
    if ideal_habitat == 'Cold and snowy':
        polarbearScore ++
        arcticfoxScore ++
        
        
    if teamwork_thoughts == 'I prefer to go solo':
        wolfScore ++
        arcticfoxScore ++
        cougarScore ++
    if teamwork_thoughts == 'I love collaborating with others':
        beaverScore ++
        polarbearScore ++
    if teamwork_thoughts == 'I enjoy leading the group':
        capybaraScore ++
        wildboarScore ++
    if teamwork_thoughts == 'I am a supportive team player':
        kangarooScore ++
        slothScore ++
        
        
    if food_preference == 'Hearty and filling':
        arcticfoxScore ++
        wildboarScore ++
    if food_preference == 'Fresh and healthy':
        beaverScore ++
        kangarooScore ++
    if food_preference == 'Sweet and indulgent':
        capybaraScore ++
        wolfScore ++
    if food_preference == 'Simple and classic':
        polarbearScore ++
        slothScore ++
        cougarScore ++
        
        
    if season_preference == 'Spring':
        kangarooScore ++
        capybaraScore ++
        slothScore ++
    if season_preference == 'Summer':
        wolfScore ++
        wildboarScore ++
    if season_preference == 'Fall':
        cougarScore ++
        beaverScore ++
    if season_preference == 'Winter':
        arcticfoxScore ++
        polarbearScore ++
        
        
    if affection == 'Through playful teasing':
        arcticfoxScore ++
        wildboarScore ++
        beaverScore ++
    if affection == 'With gentle gestures':
        kangarooScore ++
        slothScore ++
    if affection == 'By spending quality time':
        capybaraScore ++
        polarbearScore ++
    if affection == 'By protecting and supporting':
        wolfScore ++
        cougarScore ++
        
        
    if adventure == 'Hiking in the wilderness':
        cougarScore ++
        wildboarScore ++
    if adventure == 'Relaxing by the water':
        arcticfoxScore ++
        beaverScore ++
        slothScore ++
    if adventure == 'Exploring a new environment':
        wolfScore ++
        kangarooScore ++
    if adventure == 'Attending a fun gathering':
        capybaraScore ++
        polarbearScore ++
    return render_template('page1.html')
    
if __name__=="__main__":
    app.run(debug=True)
    
