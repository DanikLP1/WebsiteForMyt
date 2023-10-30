function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  
  var navLinks = document.querySelectorAll('#myTopnav a');

  navLinks.forEach(function(link) {
  link.addEventListener('click', function() {
      navLinks.forEach(function(link) {
      link.classList.remove('active');
      });
      this.classList.add('active');
      localStorage.setItem('active', this.id);
  });
  });

  window.onload = function() {
  var activeLink = localStorage.getItem('active');
  if (activeLink) {
      document.getElementById(activeLink).classList.add('active');
  }
  }

  var searchForm = document.querySelector('#search-form');

  // Найти поле поиска
  var searchInput = document.querySelector('#search-input');

  // Найти элемент для вывода сообщения об ошибке
  var errorElement = document.querySelector('#search-error');

  // Добавить обработчик события submit для формы поиска
  searchForm.addEventListener('submit', function(event) {
      // Проверить, было ли введено значение в поле поиска
      if (!searchInput.value.trim()) {
          // Если значение не было введено, отменить отправку формы
          event.preventDefault();
          // Отобразить сообщение об ошибке
          errorElement.innerHTML = 'Вы ничего не ввели.';
      } else {
          // Если значение было введено, очистить сообщение об ошибке
          errorElement.innerHTML = '';
      }
  });