window.onload = function() {
  GetSelectedValue();
  translate();

  function GetSelectedValue() {
    var lanNumber = document.getElementById("country");
    var option = lanNumber.options[lanNumber.selectedIndex].value;
  }



    function translate() {
      var en = ["Captive portal", "Login to gain access to internet", "Name", "Ticket Number", "We'll never share your info with someone else", "I accept the terms and service", "Help", "Why can't I access internet?", "Where can I find my ticketnumber?"];
      var nl = ["Inlog pagina", "Log in om toegang te krijgen tot internet", "Naam", "Ticket nummer", "Wij zullen nooit informatie delen met andere partijen", "Ik accepteer de algemene voorwaarden", "Help", "Waarom kan ik niet verbinden met internet?", "Waar kan ik mijn ticketnummer vinden?"];
      var tr = [""];

      if (option = "NL") {
        document.getElementById('Captive tekst').innerHTML = 'hi';
        /*document.getElementById("Login melding").innerHTML = nl[1];
        document.getElementById("Naam").innerHTML = nl[2];
        document.getElementById("Ticketnummer").innerHTML = nl[3];
        document.getElementById("ticketHelp").innerHTML = nl[4];
        document.getElementById("Acceptatie").innerHTML = nl[5];
        document.getElementById("Help").innerHTML = nl[6];
        document.getElementById("No internet").innerHTML = nl[7];
        document.getElementById("Zoek ticketnummer").innerHTML = nl[8];
        document.getElementById("sluiten").innerHTML = nl[9];*/
      }
      if (option = "EN") {
        document.getElementById('Captive tekst').innerHTML = 'thot';
      }
    }
  }
