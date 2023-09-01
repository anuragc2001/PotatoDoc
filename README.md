# PotatoDoc

Introducing the "Potato Disease Predictor using CNN," a cutting-edge project leveraging Convolutional Neural Networks (CNN) to accurately identify potato diseases with an impressive 95% accuracy rate.

Our project addresses the critical issue of potato crop health, where disease outbreaks can lead to significant yield losses. By harnessing the power of deep learning and image analysis, our CNN model analyzes images of potato leaves to detect diseases in their early stages, allowing for timely intervention and crop preservation.



## Features

- **High Accuracy**: Our CNN model achieves a remarkable 97.66% accuracy in identifying various potato diseases, providing reliable and actionable insights to farmers.

- **Early Detection**: By detecting diseases early, farmers can implement targeted treatments, reducing the spread of diseases and minimizing yield losses.

- **User-Friendly Interface**: We've developed an intuitive user interface that allows farmers to easily upload images for analysis and receive instant disease predictions.

- **Adaptability**: The model can identify multiple disease types, including blight, early and late, and other common potato diseases.

- **Scalability**: The system is designed to handle large volumes of images, making it suitable for real-world deployment in agricultural settings.

Our project not only showcases the potential of deep learning in agriculture but also underscores its practical application for enhancing food security and sustainability.


## Authors

- [@anuragc2001](https://www.github.com/anuragc2001)

## How It Works:

- **Data Collection**: A dataset containing labeled images of healthy potato leaves and leaves affected by various diseases is collected.
- **Data Preprocessing**: Images are resized, normalized, and augmented to enhance the model's generalization.
- **Model Architecture**: A CNN architecture is chosen, with layers for feature extraction and classification. Hyperparameters are fine-tuned for optimal performance.
- **Training**: The model is trained on the prepared dataset, iteratively adjusting its parameters to minimize prediction errors.
- **Validation**: The model's performance is assessed using validation data to prevent overfitting and ensure accurate predictions on new data.
- **Deployment**: The trained model is integrated into an interactive interface, allowing users to upload images for analysis.
- **Prediction**: Uploaded images are processed by the model, and disease predictions are displayed alongside relevant information for the user.


## Screenshots

![App Screenshot](https://github.com/anuragc2001/PotatoDoc/blob/main/results/intial.png)
![App Screenshot](https://github.com/anuragc2001/PotatoDoc/blob/main/results/loss_accuracy.png)
![App Screenshot](https://github.com/anuragc2001/PotatoDoc/blob/main/results/model_summary.png)
![App Screenshot](https://github.com/anuragc2001/PotatoDoc/blob/main/results/test_result.png)


## Installation
- Place the saved model file (potato_disease_model.h5) and preprocessing script (if needed) in a project directory.

- Create a Flask app (Python) named app.py in the project directory and load the saved model.

- Define a route in app.py to handle image uploads, preprocess images, use the model for prediction, and display results.

- Create an HTML template named index.html for uploading images and another template named result.html for displaying predictions.

- Run the Flask app in your terminal using the command flask run.

- Access the app in your web browser at http://127.0.0.1:5000/, upload images, and view the predictions.
    
## Usage/Examples
 ### Accessing the System:

- Open your web browser and navigate to the following URL: [Insert URL here].
- You will be directed to the homepage of the Potato Disease Predictor.
 ### Uploading an Image:

- On the homepage, you will find an option to "Upload Image" or "Get Started." Click on this button to proceed.
- A file upload dialog box will appear. Choose an image of a potato leaf that you wish to analyze for diseases.
- Click "Open" or "Upload" to upload the selected image.

 ### Viewing Results:

- Once the image is uploaded, the system will process it using the CNN model.
- Within moments, the system will display the results, indicating whether the uploaded image shows signs of disease or is healthy.
- You will also find additional information about the predicted disease, if applicable.

 ### Interpreting Results:

- If the result shows "Healthy," the image does not exhibit signs of disease.
- If the result indicates a disease, the system will specify the type of disease identified (e.g., blight).
- You can also find a brief description of the detected disease and its potential impact on potato crops.
 ### Taking Action:

- If the image shows signs of disease, consider taking immediate action to prevent the spread of the infection.
- Refer to relevant agricultural resources or consult experts for guidance on suitable interventions.
 ### Note:

- The Potato Disease Predictor using CNN is designed for informational purposes and is not a substitute for professional agricultural advice.
- For accurate disease management, consult with local agricultural experts and follow recommended practices.


## Optimizations

To be added...


## 🚀 About Me

I'm currently pursuing a degree in computer science engineering in West Bengal, India. My interests are strongly oriented towards software development and delving into the realm of data science. Beyond academics, I find immense joy in exploring art, watching movies, and embarking on journeys with my girlfriend. Clarity and firm stances matter to me; I find value in responses rooted in real-life experiences rather than mere political correctness. My queries encompass a wide range of subjects, all of which align with my experiences as a student within the distinct context of India. I'm open to discussing any topic close to my heart and eagerly await your opinions and insights.


## Feedback

If you have any feedback, please reach out to me at chakraborty.anurag01@gmail.com

