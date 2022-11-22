let burger = document.querySelector('.burger')
let headerMenu = document.querySelector('.header_menu')
let input = document.querySelector('.input')
let body = document.querySelector('body')

burger.addEventListener('click', mobileMenu)


function mobileMenu () {
  burger.classList.toggle('active');
  headerMenu.classList.toggle('active');
  input.classList.toggle('active');
  body.classList.toggle('lock');
}
