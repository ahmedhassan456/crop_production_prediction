
def GetPredictions(model, inputs):

    predictions = model.predict([inputs])

    return predictions