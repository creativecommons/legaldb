const tagsToggle = document.getElementById('tags-filter');

const tagsSection = document.getElementById('tags'),
    tagsShow = document.getElementById('tags-show'),
    tagsHide = document.getElementById('tags-hide');

tagsToggle.addEventListener('click', () => {
    tagsSection.classList.toggle('is-hidden');
    tagsShow.classList.toggle('is-hidden');
    tagsHide.classList.toggle('is-hidden');
    tagsSection.setAttribute('aria-expanded', !tagsSection.classList.contains('is-hidden'));
});

const tags = document.querySelectorAll('.tag__check');
const form = document.getElementById('search');
tags.forEach(tag => {
    const number = tag.getAttribute('id').split('-').pop();
    const associatedLabel = document.getElementById(`tag-label-${number}`);
    tag.addEventListener('click', (e) => {
        associatedLabel.classList.toggle('selected');
        form.submit();
    });
});

let scrollToPagination = false;
document.addEventListener('DOMContentLoaded', function() {
  const paginationLinks = document.querySelectorAll('.pagination-link');

  paginationLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
      scrollToPagination = true;
    });
  });
  
  if (scrollToPagination) {
    const paginationList = document.querySelector('.pagination-link');
    if (paginationList) {
      paginationList.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
});
