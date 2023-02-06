const fileInput = document.getElementById("file-input");
const reviewImage = document.querySelector('.review-image');
// const reviewImage = document.getElementById('taolao');

fileInput.addEventListener('change', function () {
    const file = this.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', function () {
        reviewImage.src = reader.result;
    });

    reader.readAsDataURL(file);
});