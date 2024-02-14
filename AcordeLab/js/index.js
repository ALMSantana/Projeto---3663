document.addEventListener("DOMContentLoaded", function(){
    let mensagemErro = document.querySelector('.mensagem-erro');
    mensagemErro.style.display = 'none';

    document.querySelector('.botao-login').addEventListener('click', function(event) {
        event.preventDefault();
        let email = document.querySelector('#email').value;
        let senha = document.querySelector('#senha').value;

        if (email === 'email@acordelab.com.br' && senha === '123senha') {
            mensagemErro.style.display = 'none';
            window.location.href = 'home.html';
        } else {
            mensagemErro.style.display = 'block';
        }
    });
});