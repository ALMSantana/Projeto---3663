document.addEventListener("DOMContentLoaded", function(event){
    let inputBuscar = document.querySelector('input[type="search"]');
    let cursos = document.querySelectorAll('.course-card');
    let botoes_cursos = document.querySelectorAll(".selecionar-curso");


    for (um_curso of botoes_cursos){
        um_curso.addEventListener("click", function(evento){
            let chamador = evento.target;
            let antecessorChamador = chamador.parentNode;
            localStorage.setItem("nome-curso", antecessorChamador.querySelector(".nome-curso").innerHTML);
            localStorage.setItem("instrumento-curso", antecessorChamador.querySelector(".instrumento-curso").innerHTML);
            localStorage.setItem("nivel-curso", antecessorChamador.querySelector(".nivel-curso").innerHTML);
            localStorage.setItem("tempo-curso", antecessorChamador.querySelector(".tempo-curso").innerHTML);
            localStorage.setItem("imagem-curso", antecessorChamador.querySelector("img").getAttribute('src'));
            location.href = "cursos.html";
        });
    }



    function filtrarCursos(instrument) {
        cursos.forEach(function(curso) {
            if (curso.classList.contains(instrument)) {
                curso.style.display = '';
            }else{
                curso.style.display = 'none';
            }
        });
    }

    function limparFiltro(instrument) {
        cursos.forEach(function(curso) {
            curso.style.display = '';
        });
    }

    document.querySelector('#violao').addEventListener('change', function() {
        if(this.checked) {
            filtrarCursos('violao');
        }
    });

    document.querySelector('#piano').addEventListener('change', function() {
        if(this.checked) {
            filtrarCursos('piano');
        }
    });

    document.querySelector('#guitarra').addEventListener('change', function() {
        if(this.checked) {
            filtrarCursos('guitarra');
        }
    });


    function filtroBusca(barraBusca) {
        let cursos = document.querySelectorAll('.course-card');


        cursos.forEach(function(curso) {
            let nomeCurso = curso.querySelector('.nome-curso') ? curso.querySelector('.nome-curso').innerText.toLowerCase() : '';
            let nivel = curso.querySelector('.nivel-curso') ? curso.querySelector('.nivel-curso').innerText.toLowerCase() : '';

            if (nomeCurso.includes(barraBusca.toLowerCase()) || nivel.includes(barraBusca.toLowerCase())) {
                curso.style.display = '';
            } else {
                curso.style.display = 'none';
            }
        });
    }

    inputBuscar.addEventListener('input', function() {
        filtroBusca(this.value);
    });


});
