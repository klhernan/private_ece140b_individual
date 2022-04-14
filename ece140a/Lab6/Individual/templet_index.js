function submit_ranges() {
    const height = document.getElementById("height").value;
    const age = document.getElementById("age").value;
    const rangesUrl = `/ranges/${height}/${age}`;
  
    fetch(rangesUrl).then((res) => {
      const response = res.json();
      // get owner/author name from the response and update the UI
      document.getElementById("author").textContent = response["owner"];
      // get the image src from the api response and update the UI
      document.getElementById("current-image").src = response["image_src"];
    });
  }


  var theCompanyName = document.querySelector('.');
  var theCompanyWebsite = document.querySelector('.compWebsite');
  var theCompanyState = document.querySelector('.compState');
  var theCompanyPrice = document.querySelector('.compPrice');
  
  // Financial Modeling Prep API my key
  // var myApiKey = '37264a2f7e56a4a7056b28a8feb3af39'
  
  // What wil be done by the form
  


  var form = document.getElementById('send');
  var stockSymbol = "";
  // Obtaining the submission when entered 
  function getInfo(){
    
    let url = 'https://financialmodelingprep.com/api/v3/profile/' + stockSymbol + '?apikey=37264a2f7e56a4a7056b28a8feb3af39';
    
    fetch(url)
      .then(response => response.json())
      .then(function(response) {
        if(response.length > 1) {
      
          let infoVars = [theCompanyName, 
                             theCompanyWebsite, 
                             theCompanyState, 
                             theCompanyPrice];
  
          let infoKeys = ['compName', 
                         'compWebsite',
                         'compState',
                         'compPrice'];
  
          let outInfoFields = ['Company Name: ',
                              'Website: ',
                              'State: ',
                              'Price: '];
  
          for (let i=0; i<outInfoFields.length; i++) {
            try {
              infoVars[i].innerHTML = outInfoFields + infoKeys[i];
            }
            catch(error) {
              // output empty string because key does not exist in JSON data
              field.innerHTML = "N/A";
            }
        }
       }
      else {
        theCompanyName.innerHTML = "Not available";
      }
    });
    
  }
  
  
  form.addEventListener("submit", (event) => {VB 
    event.preventDefault();
    stockSymbol = form.elements['stockSym'].value;
    
    if (symInput != "") {
      getInfo();
    }
      
   });
  

   function getInfo(){
    
    // let url = 'https://financialmodelingprep.com/api/v3/profile/' + stockSymbol + '?apikey=37264a2f7e56a4a7056b28a8feb3af39';
    
    fetch(url)
      .then(response => response.json())
      .then(function(response) {
        if(response.length > 1) {
      
          let infoVars = [theCompanyName, 
                             theCompanyWebsite, 
                             theCompanyState, 
                             theCompanyPrice];
  
          let infoKeys = ['compName', 
                         'compWebsite',
                         'compState',
                         'compPrice'];
  
          let outInfoFields = ['Company Name: ',
                              'Website: ',
                              'State: ',
                              'Price: '];
  
          for (let i=0; i<outInfoFields.length; i++) {
            try {
              infoVars[i].innerHTML = outInfoFields + infoKeys[i];
            }
            catch(error) {
              // output empty string because key does not exist in JSON data
              field.innerHTML = "N/A";
            }
        }
       }
      else {
        theCompanyName.innerHTML = "Not available";
      }
    });
    
  }
  
  
  form.addEventListener("submit", (event) => {VB 
    event.preventDefault();
    stockSymbol = form.elements['stockSym'].value;
    
    if (symInput != "") {
      getInfo();
    }
      
   });
  