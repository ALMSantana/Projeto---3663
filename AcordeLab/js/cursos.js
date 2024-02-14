document.addEventListener("DOMContentLoaded", function(){
    let lista_videos = document.querySelectorAll(".titulo-video");
    let lista_thumbanils = document.querySelectorAll(".conteudo-thumbnail");
    let elemento_nome_curso = document.querySelector(".nome-curso");
    let elemento_nivel_curso = document.querySelector(".nivel-curso");
    let elemento_descricao_curso = document.querySelector(".instrumento-curso");
    let elemento_imagem_curso = document.querySelector(".imagem-curso");
    let elemento_tempo_curso = document.querySelector(".tempo-curso");
    let contador_video = 1;

    for(um_video of lista_videos){
        um_video.innerHTML = "Vídeo " + contador_video;
        contador_video+=1;
    }

    for(uma_thumb of lista_thumbanils){
        uma_thumb.src = localStorage.getItem("imagem-curso");
    }

    elemento_nome_curso.innerHTML = localStorage.getItem("nome-curso");
    elemento_nivel_curso.innerHTML = localStorage.getItem("nivel-curso");
    elemento_nivel_curso.classList.add(pegarClasseNivel(localStorage.getItem("nivel-curso")));
    elemento_tempo_curso.innerHTML = localStorage.getItem("tempo-curso") + " total";
    elemento_imagem_curso.src = localStorage.getItem("imagem-curso");
    elemento_descricao_curso.innerHTML = localStorage.getItem("instrumento-curso")
});

function pegarClasseNivel(nivel){
    if (nivel == "Iniciante"){
        return "iniciante";
    }
    else if(nivel == "Intermediário"){
        return "intermediario";
    }else{
        return "avancado";
    }
}
