/* Engel Nadlan — minimal progressive enhancement (no dependencies) */
(function () {
  'use strict';
  var d = document, b = d.body;

  /* mobile menu */
  var burger = d.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = b.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && b.classList.contains('menu-open')) burger.click(); });
    d.querySelectorAll('.menu a').forEach(function (a) { a.addEventListener('click', function () { if (b.classList.contains('menu-open')) burger.click(); }); });
  }

  /* scroll reveal */
  var rv = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && rv.length) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* project filters */
  var filters = d.querySelector('.filters');
  if (filters) {
    var cards = d.querySelectorAll('[data-status]'), empty = d.querySelector('.empty');
    filters.addEventListener('click', function (e) {
      var btn = e.target.closest('button'); if (!btn) return;
      filters.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === btn ? 'true' : 'false'); });
      var f = btn.dataset.filter, n = 0;
      cards.forEach(function (c) { var show = f === 'all' || c.dataset.status === f; c.classList.toggle('is-hidden', !show); if (show) n++; });
      if (empty) empty.hidden = n > 0;
    });
  }

  /* forms (Web3Forms JSON endpoint) */
  d.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form__msg'), btn = form.querySelector('button[type=submit]');
      var fd = new FormData(form);
      if (fd.get('botcheck')) return;
      btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = 'שולח…';
      msg.className = 'form__msg';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(Object.fromEntries(fd)) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok && j.success, j: j }; }); })
        .then(function (r) {
          if (r.ok) { form.reset(); msg.textContent = 'תודה, פנייתכם התקבלה. נחזור אליכם בהקדם.'; msg.className = 'form__msg ok'; }
          else throw new Error(r.j && r.j.message);
        })
        .catch(function () {
          msg.innerHTML = 'לא הצלחנו לשלוח את הטופס כרגע. ניתן להתקשר אלינו: <a href="tel:+97236005955" dir="ltr">03-6005955</a> או לכתוב ל-<a href="mailto:office@engelnadlan.co.il">office@engelnadlan.co.il</a>';
          msg.className = 'form__msg err';
        })
        .finally(function () { btn.disabled = false; btn.textContent = btn.dataset.t; });
    });
  });
})();
