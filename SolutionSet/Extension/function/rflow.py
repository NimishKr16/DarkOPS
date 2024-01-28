from roboflow import Roboflow

def prediction():
    rf = Roboflow(api_key="hUAXP1GZ0TpCXy4gQ2es")
    project = rf.workspace().project("ui-element-detect")
    model = project.version(5).model
    # visualize your prediction
    model.predict("CascadingCoders_DPBH23/SolutionSet/Extension/screenshots/screenshot.jpg", confidence=40, overlap=30).save("prediction.jpg")
