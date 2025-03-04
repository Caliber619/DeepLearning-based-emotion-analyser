import json
from tensorflow.keras.models import model_from_json, Sequential

# Load JSON file
with open("facialemotionmodel.json", "r") as json_file:
    model_json = json_file.read()

# Load the model architecture with custom objects
model = model_from_json(model_json, custom_objects={"Sequential": Sequential})

# Load weights
model.load_weights("facialemotionmodel.h5")

# Save the entire model as a single .h5 file
model.save("facialemotionmodel_full.h5")

print("Model converted and saved as facialemotionmodel_full.h5")
