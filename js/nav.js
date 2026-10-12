// Opens and closes the nav menu on small screens.
const toggle = document.querySelector('.nav-toggle');
const menu = document.getElementById('site-menu');

toggle.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
});

// Close the menu after picking a link, so it doesn't cover the section you jumped to.
menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', false);
    });
});
