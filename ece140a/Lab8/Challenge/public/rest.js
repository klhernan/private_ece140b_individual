function submit_object() {
  const object_name = document.getElementById("objectName").value;
  console.log(object_name);
  const objectNameUrl = `/objectName/${object_name}`;

  fetch(objectNameUrl)
    .then((res) => res.json())
    .then((response) => {
      console.log(response);
      // // get owner/author name from the response and update the UI
      // document.getElementById("nameofobject").textContent = response["name"];
      // // get the image src from the api response and update the UI
      // document.getElementById("GPSlocation").src = response["location"];
    });
}
