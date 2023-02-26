let tst = "";


var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}

function showPosition(position) {
  
  tst = position.coords.latitude + "+" + position.coords.longitude;
  url = 'https://www.google.com/maps/place/'+ tst;
  tst1 = tst + "&key=de3e476b70ea40518e6819df2151c3de"
  x.href = url;
  console.log(position);
  
  let city = document.getElementById("city");
  let town = document.getElementById("town");
  let street = document.getElementById("street");
  let homeno = document.getElementById("homeno");
  let homename = document.getElementById("homename");
      
  const api_url1 ="https://api.opencagedata.com/geocode/v1/json?q=" + tst + "&key=de3e476b70ea40518e6819df2151c3de" ;
  console.log(api_url1);
  fetch(api_url1)
    .then(response => response.json())
    .then(result =>{
      let details = result.results[0].components;
      console.log(details);
      city.value = details.state;
      town.value = details.town;
      suburb.value = details.suburb;
      street.value = details.road;
  });

  
}



