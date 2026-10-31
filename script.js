console.log("SentinelPen initialized successfully.");

document.addEventListener("DOMContentLoaded", function () {
    const targetInput = document.getElementById("target");

    if (targetInput) {
        targetInput.addEventListener("input", function () {
            targetInput.value = targetInput.value.trimStart();
        });
    }
});