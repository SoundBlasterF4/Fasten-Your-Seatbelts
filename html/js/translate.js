var dataReload = document.querySelectorAll("[data-reload]");

var language = {
  eng: {
    portal: "Captive Portal",
    gain: "Login to gain access to internet",
    naam: "Name:",
    ticketval: "Ticket number:",
    terms: "Corendon will never share your information with third parties.",
    info: "I accept the terms and service"
  },
  nl: {
    portal: "Inlog pagina",
    gain: "Login om toegang te krijgen tot het internet",
    naam: "Naam",
    ticketval: "Ticket nummer:",
    terms: "Corendon zal geen informatie delen met derden.",
    info: "Ik accepteer de licentie overeenkomst"
  },
  tr: {
    portal: "Kısıtlama portalı",
    gain: "Internet’e bağlanmak için lütfen isminizi ve soyisminizi giriniz.",
    naam: "Ad:",
    ticketval: "Billet numarasi:",
    terms: "Corendon'un üçüncü taraflarla bilgi paylaşmayacağınin.",
    info: "Lisans sözleşmesini kabul ediyorum."
  }
};
if (window.location.hash) {
  if (window.location.hash === "#nl") {
    captive.textContent = language.nl.portal;
    login.textContent = language.nl.gain;
    waardenaam.textContent = language.nl.naam;
    waarde.textContent = language.nl.ticketval;
    ticketHelp.textContent = language.nl.terms;
    acceptatie.textContent = language.nl.info;
  }
}
if (window.location.hash) {
  if (window.location.hash === "#tr") {
    captive.textContent = language.tr.portal;
    login.textContent = language.tr.gain;
    waardenaam.textContent = language.tr.naam;
    waarde.textContent = language.tr.ticketval;
    ticketHelp.textContent = language.tr.terms;
    acceptatie.textContent = language.tr.info;
  }
}
for (let i = 0; i < dataReload.length; i++) {
  dataReload[i].onclick = function() {
    window.location.hash = dataReload[i].hash;
    window.location.reload(true);
  }
}

