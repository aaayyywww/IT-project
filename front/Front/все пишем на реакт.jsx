import React from 'react';
import 'css/дезигне.css'; // Подключаем CSS файл для стилей

function App() {
  return (
    <div className="App">
      <header>
        <a href="#" style={{float: 'left', marginTop: '2px', marginRight: '50px'}}><img src="лого.png" height="60" width="60" alt="лого"/></a>
        <div id="menu">
          <ul>
            <button className="btn1">Вход</button>
            <button className="btn2">Регистрация</button>
            <button className="btn">Список олимпиад</button>
            <button className="btn">Топ олимпиад</button>
            <button className="btnproof">Проверка регистрации</button>
          </ul>
        </div>
      </header>
      
      <main>
        {/* Код для календаря */}
      </main>
      
      <footer>
        <nav>
          <ul>
            <button className="btnfooter">О нас</button>
            <button className="btnfooter">Мои олимпиады</button>
            <button className="btnfooter">Отзывы</button>
            <button className="btnfooter">Добавить олимпиаду</button>
          </ul>
        </nav>
      </footer>
    </div>
  );
}

export default App;
