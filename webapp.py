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
        wolfScore = wolfScore +1
        kangarooScore = kangarooScore +1
    if freetime_preferences == 'Relaxing in the sun':
        polarbearScore = polarbearScore +1
        slothScore = slothScore +1
        arcticfoxScore = arcticfoxScore +1
    if freetime_preferences == 'Socializing with friends':
        wildboarScore = wildboarScore +1
        cougarScore = cougarScore +1
    if freetime_preferences == 'Working on a project':
        beaverScore = beaverScore +1
        capybaraScore = capybaraScore +1
        
        
    if personality == 'Adventurous and spontaneous':
        capybaraScore = capybaraScore +1
        kangarooScore = kangarooScore +1
    if personality == 'Calm and nurturing':
        beaverScore = beaverScore +1
        slothScore = slothScore +1
    if personality == 'Playful and energetic':
        polarbearScore = polarbearScore +1
        wildboarScore = wildboarScore +1
    if personality == 'Loyal and protective':
        wolfScore= wolfScore +1
        cougarScore = cougarScore +1
        arcticfoxScore = arcticfoxScore +1
        
        
    if stress_handling == 'Go for a run or exercise':
        wolfScore= wolfScore +1
        arcticfoxScore = arcticfoxScore +1
    if stress_handling == 'Meditate or take a nap':
        polarbearScore = polarbearScore +1
        slothScore = slothScore +1
        kangarooScore = kangarooScore +1
    if stress_handling == 'Hang out with friends':
        beaverScore = beaverScore +1
        capybaraScore = capybaraScore +1
    if stress_handling == 'Take charge and tackle the problem':
        wildboarScore = wildboarScore +1
        cougarScore = cougarScore +1
        
        
    if ideal_habitat == 'Mountains and forests':
        beaverScore = beaverScore +1
        cougarScore = cougarScore +1
        wolfScore= wolfScore +1
    if ideal_habitat == 'Jungles and swamps':
        slothScore = slothScore +1
        capybaraScore = capybaraScore +1
    if ideal_habitat == 'Desert and flatland':
        kangarooScore = kangarooScore +1
        wildboarScore = wildboarScore +1
    if ideal_habitat == 'Cold and snowy':
        polarbearScore = polarbearScore +1
        arcticfoxScore = arcticfoxScore +1
        
        
    if teamwork_thoughts == 'I prefer to go solo':
        wolfScore= wolfScore +1
        arcticfoxScore = arcticfoxScore +1
        cougarScore = cougarScore +1
    if teamwork_thoughts == 'I love collaborating with others':
        beaverScore = beaverScore +1
        polarbearScore = polarbearScore +1
    if teamwork_thoughts == 'I enjoy leading the group':
        capybaraScore = capybaraScore +1
        wildboarScore = wildboarScore +1
    if teamwork_thoughts == 'I am a supportive team player':
        kangarooScore = kangarooScore +1
        slothScore = slothScore+1
        
        
    if food_preference == 'Hearty and filling':
        arcticfoxScore = arcticfoxScore +1
        wildboarScore = wildboarScore +1
    if food_preference == 'Fresh and healthy':
        beaverScore = beaverScore +1
        kangarooScore = kangarooScore +1
    if food_preference == 'Sweet and indulgent':
        capybaraScore = capybaraScore +1
        wolfScore= wolfScore +1
    if food_preference == 'Simple and classic':
        polarbearScore = polarbearScore +1
        slothScore = slothScore+1
        cougarScore = cougarScore +1
        
        
    if season_preference == 'Spring':
        kangarooScore = kangarooScore +1
        capybaraScore = capybaraScore +1
        slothScore = slothScore +1
    if season_preference == 'Summer':
        wolfScore= wolfScore +1
        wildboarScore = wildboarScore +1
    if season_preference == 'Fall':
        cougarScore = cougarScore +1
        beaverScore = beaverScore +1
    if season_preference == 'Winter':
        arcticfoxScore = arcticfoxScore +1
        polarbearScore = polarbearScore +1
        
        
    if affection == 'Through playful teasing':
        arcticfoxScore = arcticfoxScore +1
        wildboarScore = wildboarScore +1
        beaverScore = beaverScore +1
    if affection == 'With gentle gestures':
        kangarooScore = kangarooScore +1
        slothScore = slothScore +1
    if affection == 'By spending quality time':
        capybaraScore = capybaraScore +1
        polarbearScore = polarbearScore +1
    if affection == 'By protecting and supporting':
        wolfScore= wolfScore +1
        cougarScore = cougarScore +1
        
        
    if adventure == 'Hiking in the wilderness':
        cougarScore = cougarScore +1
        wildboarScore = wildboarScore +1
    if adventure == 'Relaxing by the water':
        arcticfoxScore = arcticfoxScore +1
        beaverScore = beaverScore +1
        slothScore = slothScore+1
    if adventure == 'Exploring a new environment':
        wolfScore= wolfScore +1
        kangarooScore = kangarooScore +1
    if adventure == 'Attending a fun gathering':
        capybaraScore = capybaraScore +1
        polarbearScore = polarbearScore +1
    animal = ""   
    x = max(cougarScore, wildboarScore, arcticfoxScore, beaverScore, slothScore, wolfScore, kangarooScore, capybaraScore, polarbearScore)
    if cougarScore == x:
        animal = "You are a cougar!"
        animalImage = "/static/cougar.webp"
    if wildboarScore == x:
        animal = "You are a wildboar!"
        animalImage = "/static/wildboar.webp"
    if arcticfoxScore == x:
        animal = "You are an arctic fox!"
        animalImage = "/static/arcticfox.jpg"
    if beaverScore == x:
        animal = "You are a beaver!"
        animalImage = "/static/beaver.jpg"
    if slothScore == x:
        animal = "You are a sloth!"
        animalImage = "/static/sloth.jpg"
    if wolfScore == x:
        animal = "You are a wolf!"
        animalImage = "/static/wolf.webp"
    if kangarooScore == x:
        animal = "You are a kangaroo!"
        animalImage = "/static/kangaroo.jpg"
    if capybaraScore == x:
        animal = "You are a capybara!"
        animalImage = "/static/capybara.jpg"
    if polarbearScore == x:
        animal = "You are a polar bear!"
        animalImage = "/static/polarbear.jpg"
        
    print(animal)
    return render_template('page1.html', animal = animal, photo = animalImage)
   
   
if __name__=="__main__":
    app.run(debug=True)
    
