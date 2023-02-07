const fileInput = document.getElementById('file-input'); // upload file
const reviewImage = document.querySelector('.review-image'); // image preview
const errorMessage = document.querySelector('.format-note'); // error message

fileInput.addEventListener('change', function () {
    const file = this.files[0];
    const reader = new FileReader();

    //check if the file is jpg or not
    if (file.type !== "image/jpeg") {
        errorMessage.innerHTML = "Error: file type must be .jpg!";
        errorMessage.style.color = '#E51515';
        return;
    } else {
        errorMessage.innerHTML = "Only .jpg files are accepted";
        errorMessage.style.color = '#5A5A5A';
    }

    reader.addEventListener('load', function () {
        reviewImage.src = reader.result;
    });

    reader.readAsDataURL(file);
});