// <!-- video js -->
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-36251023-1']);
  _gaq.push(['_setDomainName', 'jqueryscript.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
// <!-- video js end -->

// animation script

document.documentElement.style.setProperty('--animate-duration', '1s');

const element = document.querySelector('.video');
element.classList.add('animate__animated', 'animate__bounceInLeft');

// display on scroll here it begins

// fade-in portfolio

const faders = document.querySelectorAll('.fade-in');   //for fader
const slider = document.querySelectorAll('.slide-in');  //for slider

const appearOptions = {
  threshold: 1,
  rootMargin: "0px 0px 100px 0px",
};

const appearOnScroll = new IntersectionObserver ( function(entries, appearOnScroll) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      return;
    }
    else {
      entry.target.classList.add('appear');
      appearOnScroll.unobserve(entry.target);
    }
  })
}, appearOptions);

faders.forEach (fader => {
  appearOnScroll.observe(fader);
});

// For sliders in Services
sliders.forEach (slider => {
  appearOnScroll.observe(slider);
});



// form validation
function validateForm() {
  var name =  document.getElementById('name').value;
  if (name == "") {
      document.querySelector('.status').innerHTML = "Name cannot be empty";
      return false;
  }
  var email =  document.getElementById('email').value;
  if (email == "") {
      document.querySelector('.status').innerHTML = "Email cannot be empty";
      return false;
  } else {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if(!re.test(email)){
          document.querySelector('.status').innerHTML = "Email format invalid";
          return false;
      }
  }
  var subject =  document.getElementById('subject').value;
  if (subject == "") {
      document.querySelector('.status').innerHTML = "Subject cannot be empty";
      return false;
  }
  var message =  document.getElementById('message').value;
  if (message == "") {
      document.querySelector('.status').innerHTML = "Message cannot be empty";
      return false;
  }
  document.querySelector('.status').innerHTML = "Sending...";
}
