function submit_id() {
  const image_id = document.getElementById("imageId").value;
  const imageIdUrl = `/imageIds/${image_id}`;

  fetch(imageIdUrl)
    .then((res) => res.json())
    .then((response) => {
      console.log(response);
      // get owner/author name from the response and update the UI
      document.getElementById("imgToTxt").textContent = response["value"];
      // get the image src from the api response and update the UI
      document.getElementById("current-image").src = response["name"];

      document.getElementById("time").textContent = response["created_at"];
    });
}
