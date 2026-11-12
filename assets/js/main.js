/* Small progressive enhancements. The site works without JavaScript. */
(function () {
  'use strict';
  var root = document.documentElement;

  /* Mobile menu */
  var header = document.querySelector('.site-header');
  var navBtn = document.querySelector('.nav-toggle');
  function setNav(open) {
    if (!header || !navBtn) return;
    header.classList.toggle('nav-open', open);
    navBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (navBtn) {
    navBtn.addEventListener('click', function () {
      setNav(navBtn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navBtn.getAttribute('aria-expanded') === 'true') {
        setNav(false);
        navBtn.focus();
      }
    });
    var navLinks = document.querySelectorAll('.nav a');
    for (var i = 0; i < navLinks.length; i++) {
      navLinks[i].addEventListener('click', function () { setNav(false); });
    }
  }

  /* Project filter: #community, #inclusion, #data, #governance */
  var list = document.querySelector('[data-filter-list]');
  if (list) {
    var chips = document.querySelectorAll('[data-filter]');
    var entries = list.querySelectorAll('.entry');
    var countEl = document.querySelector('[data-count]');
    var ids = ['community', 'inclusion', 'data', 'governance'];

    var apply = function (id, updateHash) {
      var shown = 0;
      for (var i = 0; i < entries.length; i++) {
        var pillars = (entries[i].getAttribute('data-pillars') || '').split(' ');
        var match = id === 'all' || pillars.indexOf(id) !== -1;
        entries[i].hidden = !match;
        if (match) shown++;
      }
      for (var j = 0; j < chips.length; j++) {
        chips[j].setAttribute('aria-pressed', chips[j].getAttribute('data-filter') === id ? 'true' : 'false');
      }
      if (countEl) {
        countEl.textContent = 'Showing ' + shown + (shown === 1 ? ' project' : ' projects') + (id === 'all' ? '' : ' in this area');
      }
      if (updateHash && window.history && history.replaceState) {
        history.replaceState(null, '', id === 'all' ? location.pathname + location.search : '#' + id);
      }
    };

    for (var c = 0; c < chips.length; c++) {
      chips[c].addEventListener('click', function () {
        apply(this.getAttribute('data-filter'), true);
      });
    }

    var fromHash = function () {
      var h = decodeURIComponent((location.hash || '').replace('#', ''));
      if (ids.indexOf(h) !== -1) {
        apply(h, false);
      } else {
        apply('all', false);
        if (h) {
          var target = document.getElementById(h);
          if (target) target.scrollIntoView();
        }
      }
    };
    fromHash();
    window.addEventListener('hashchange', fromHash);
  }

  /* Copy bio buttons */
  var status = document.querySelector('[data-copy-status]');
  var copyBtns = document.querySelectorAll('[data-copy]');
  function announce(msg) {
    if (!status) return;
    status.textContent = msg;
    setTimeout(function () { status.textContent = ''; }, 3000);
  }
  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'absolute';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    return ok;
  }
  for (var k = 0; k < copyBtns.length; k++) {
    copyBtns[k].addEventListener('click', function () {
      var target = document.getElementById(this.getAttribute('data-copy'));
      if (!target) return;
      var text = target.textContent.trim();
      var label = this.textContent.replace('Copy ', '');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(
          function () { announce('Copied the ' + label + '.'); },
          function () { announce(fallbackCopy(text) ? 'Copied the ' + label + '.' : 'Copy did not work. Select the text and copy it.'); }
        );
      } else {
        announce(fallbackCopy(text) ? 'Copied the ' + label + '.' : 'Copy did not work. Select the text and copy it.');
      }
    });
  }
})();
