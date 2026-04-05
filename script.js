async function uploadImage() {

    const fileInput = document.getElementById("fileInput");

    if (!fileInput.files.length) {
        alert("Select a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]); // MUST be "file"

    try {
        const response = await fetch("/restore", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const blob = await response.blob();

        const imageURL = URL.createObjectURL(blob);
        document.getElementById("result").src = imageURL;

    } catch (err) {
        console.error(err);
        alert("Upload failed");
    }
}