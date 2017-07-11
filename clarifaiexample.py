from clarifai.rest import ClarifaiApp
app=ClarifaiApp(api_key='df3f6b49a55048579101375b3ac757bf')
model=app.models.get('food-items-v1.0')
response=model.predict_by_url('https://online.pizzahut.co.in/sites/default/files/product_images/pizzahut_slice_images/1371013.png')
print response