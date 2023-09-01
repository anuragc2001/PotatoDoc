document.getElementById("upload-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById("image-upload");
    const resultDiv = document.getElementById("prediction-result");
    const predictedImage = document.getElementById("predicted-image");
    const predictedLabel = document.getElementById("predicted-label");
    const confidenceLabel = document.getElementById("confidence-label");
    const statusLabel = document.getElementById("status-label");
    
    const file = fileInput.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("image", file);

        // Send the image data to your CNN model for prediction
        // Replace the following line with your API call or prediction logic
        fetch("/api/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            console.log(data);
            resultDiv.style.display = "block";
            predictedImage.src = URL.createObjectURL(file);
            
            
            
            if(data.prediction === "Healthy"){
                
                predictedLabel.textContent = "Predicted Label: " + data.prediction;
                predictedLabel.style.color = "black";
                predictedLabel.style.backgroundColor = "lightgreen";

            }else{

                predictedLabel.textContent = "Predicted Label: " + data.prediction;
                predictedLabel.style.backgroundColor = "white";
                statusLabel.textContent = "Status: Infected";
                statusLabel.style.backgroundColor = "pink";
            }
            confidenceLabel.textContent = "Confidence: " + data.confidence;
        })
        .catch(error => console.error("Error:", error));
    }
});
