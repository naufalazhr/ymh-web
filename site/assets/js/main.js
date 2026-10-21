// Gerbang Cahaya — interactions
(function(){
  "use strict";
  document.documentElement.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Drawer
  var burger = document.querySelector("[data-burger]");
  var drawer = document.querySelector("[data-drawer]");
  if (burger && drawer) {
    burger.addEventListener("click", function(){ drawer.classList.add("open"); document.body.style.overflow="hidden"; });
    drawer.querySelector("[data-close]").addEventListener("click", close);
    drawer.addEventListener("click", function(e){ if(e.target.tagName==="A") close(); });
    function close(){ drawer.classList.remove("open"); document.body.style.overflow=""; }
  }

  // Hero slider
  var slides = Array.prototype.slice.call(document.querySelectorAll(".hero-slide"));
  var dotsBox = document.querySelector(".hero-dots");
  if (slides.length > 1 && !reduce) {
    var i = 0, timer;
    slides.forEach(function(_, n){
      var b = document.createElement("button");
      b.setAttribute("aria-label", "Slide " + (n+1));
      if (n===0) b.classList.add("active");
      b.addEventListener("click", function(){ go(n); restart(); });
      dotsBox.appendChild(b);
    });
    var dots = Array.prototype.slice.call(dotsBox.children);
    function go(n){
      slides[i].classList.remove("active"); dots[i].classList.remove("active");
      i = (n + slides.length) % slides.length;
      slides[i].classList.add("active"); dots[i].classList.add("active");
    }
    function restart(){ clearInterval(timer); timer = setInterval(function(){ go(i+1); }, 7000); }
    restart();
  }

  // Reveal on scroll
  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } });
    }, {threshold: .12});
    els.forEach(function(el){ io.observe(el); });
  } else {
    els.forEach(function(el){ el.classList.add("in"); });
  }

  // News rail progress
  var rail = document.querySelector(".news-rail");
  var bar = document.querySelector(".rail-progress i");
  if (rail && bar) {
    rail.addEventListener("scroll", function(){
      var max = rail.scrollWidth - rail.clientWidth;
      var p = max > 0 ? rail.scrollLeft / max : 0;
      bar.style.width = (18 + p * 82) + "%";
    }, {passive:true});
  }

  // Model filter
  var fBtns = document.querySelectorAll("[data-filter]");
  var cards = document.querySelectorAll("[data-cat]");
  if (fBtns.length) {
    fBtns.forEach(function(btn){
      btn.addEventListener("click", function(){
        fBtns.forEach(function(b){ b.classList.remove("active"); });
        btn.classList.add("active");
        var f = btn.getAttribute("data-filter");
        cards.forEach(function(c){
          c.style.display = (f === "semua" || c.getAttribute("data-cat") === f) ? "" : "none";
        });
      });
    });
  }

  // Newsletter -> WhatsApp
  var nl = document.querySelector("[data-nl]");
  if (nl) {
    nl.addEventListener("submit", function(e){
      e.preventDefault();
      var em = nl.querySelector("input[type=email]").value.trim();
      var msg = encodeURIComponent("Halo Gerbang Cahaya, saya ingin berlangganan info promo Yamaha. Email saya: " + em);
      window.open("https://wa.me/628997108328?text=" + msg, "_blank");
    });
  }

  // Footer year
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
