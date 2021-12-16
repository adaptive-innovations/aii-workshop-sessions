import json
import os
import pathlib
from flask import Flask
from waitress import serve
from flask import request
app = Flask(__name__)

def openJson(filename):
    f = open(filename)
    data = json.load(f)
    f.close()
    return data

def openHtml(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text

os.chdir(pathlib.Path(__file__).parent.resolve())
# localhost:8080/recipe
@app.route('/recipe')
def recipeResponse():
    print("New Incoming Request...")
    try:
        toGet = request.args.get('get')
        print(toGet)
        data = openJson(toGet+'.json')
        page = openHtml('page.html')

        updateList = ["Title", "Image", "Author", "Time Required", "Servings"]
        for each in updateList:
            page = page.replace("[{0}]".format(each), data[each])

        ingredientTemplate = openHtml('ingredient.html')
        ingredients = ""
        for each in data['Ingredients']:
            currentIngredient = ingredientTemplate
            for value in each:
                currentIngredient = currentIngredient.replace("[{0}]".format(value), each[value])
            ingredients += "\n"+currentIngredient
        page = page.replace("[Ingredients]", ingredients)

        stepTemplate = openHtml('step.html')
        steps = ""
        counter = 1
        for each in data['Steps']:
            currentStep = stepTemplate
            currentStep = currentStep.replace("[stepNum]", "Step "+str(counter))
            currentStep = currentStep.replace("[Step]", each)
            steps += "\n"+currentStep
            counter += 1
        page = page.replace("[Steps]", steps)
        return page
    except:
        return "404: Recipe not Found!"
    finally:    
        print("...Done!")

serve(app, host='0.0.0.0', port=8080, threads=1)