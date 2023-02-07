const fileInput = document.getElementById('file-input'); // upload image file
const imageUrl = document.getElementById('url-input'); // upload image by URL
const reviewImage = document.querySelector('.review-image'); // image preview
const errorMessage = document.querySelector('.format-note'); // error message

// function to upload image file
fileInput.addEventListener('change', function () {
    const file = this.files[0];
    const reader = new FileReader();

    //check if the file is jpg or not
    if (file.type !== "image/jpeg") {
        errorMessage.innerHTML = "Error: file type must be .jpg!";
        errorMessage.style.color = '#E51515';
        return;
    } else {
        errorMessage.innerHTML = "Upload successful!";
        errorMessage.style.color = '#5A5A5A';
    }

    reader.addEventListener('load', function () {
        reviewImage.src = reader.result;
    });

    reader.readAsDataURL(file);
});

// function to upload image by URL
imageUrl.addEventListener('input', function () {
    // check if the url value is empty or just whitespaces
    const url = this.value.trim();
    if (url)
    {
        fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.blob();
        })
        .then(blob => {
            errorMessage.innerHTML = "Upload successful!";
            errorMessage.style.color = '#5A5A5A';
            reviewImage.src = URL.createObjectURL(blob);
        })
        .catch(error => {
            errorMessage.style.display = "block";
            errorMessage.style.color = '#E51515';
            errorMessage.textContent = `Invalid URL: ${error}`;
        });
    }    
});