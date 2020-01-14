window.addEventListener('load', () => {
    let long,lat;
    let temperatureDescription = document.querySelector(".description");
    let temperatureDegree = document.querySelector(".degree");
    let locationTimeZone = document.querySelector(".timezone");


    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(position => {
            long = position.coords.longitude;
            lat = position.coords.latitude;
            const proxy = "https://cors-anywhere.herokuapp.com/";
            const URL = `${proxy}https://api.darksky.net/forecast/d61f1602823acf46019676f044495415/${lat},${long}`;
            fetch(URL).then(response => {
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                const {temperature,summary, icon} = data.currently;
                  temperatureDegree.textContent = ((temperature -32) * 5 / 9).toFixed(1) +  '     Graden';
                  
                  temperatureDescription.textContent = summary;
                  locationTimeZone.textContent = data.timezone.substr(7);
                
                    
                    setIcons(icon,document.querySelector('.icon'));
                });
              
        });
    }
    function setIcons(icon, iconID)
    {
        const skycons = new Skycons({color : "white"});
        const currentIcon = icon.replace(/-/g,"_").toUpperCase();
        skycons.play();
        return skycons.set(iconID, Skycons[currentIcon]);
    }
});
