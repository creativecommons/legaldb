// Allow toggle dropdown of the navbar burger menu
const burgerMenu = document.getElementsByClassName('navbar-burger')[0];
burgerMenu.addEventListener('click', () => {
    const menu = document.getElementsByClassName('navbar-menu')[0];
    menu.classList.toggle('is-active');
    burgerMenu.classList.toggle('is-active');
    burgerMenu.setAttribute('aria-expanded', burgerMenu.classList.contains('is-active'));
})

const tagsToggle = document.getElementById('tags-filter');

if (document.body.contains(tagsToggle)) {
    const tagsSection = document.getElementById('tags'),
        tagsShow = document.getElementById('tags-show'),
        tagsHide = document.getElementById('tags-hide');

    tagsToggle.addEventListener('click', () => {
        tagsSection.classList.toggle('is-hidden');
        tagsShow.classList.toggle('is-hidden');
        tagsHide.classList.toggle('is-hidden');
        if (tagsSection.classList.contains('is-hidden')) {
            tagsSection.setAttribute('aria-expanded', false);
        } else {
            tagsSection.setAttribute('aria-expanded', true);
        }
    });

    const tags = document.querySelectorAll('.tag');
        tags.forEach(tag => {
        tag.addEventListener('click', () => {
            tag.classList.toggle('selected');
        })
    });
}
