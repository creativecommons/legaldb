const tagsToggle = document.getElementById('tags-filter'),
    tagsSection = document.getElementById('tags'),
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
