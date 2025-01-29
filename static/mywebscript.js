let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim(); // Trim to remove spaces

    if (textToAnalyze === "") {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
        return; // Stop execution if text is empty
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Show the valid system response
                document.getElementById("system_response").innerHTML = JSON.parse(xhttp.responseText).response;
            } else if (this.status == 400) {
                // Handle error response when text is blank
                document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
            } else {
                // Handle unexpected errors
                document.getElementById("system_response").innerHTML = "An error occurred. Please try again.";
            }
        }
    };

    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
