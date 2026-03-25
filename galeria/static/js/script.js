// === MODAL ===
function abrirModal(srcImagem) {
    let modal = document.getElementById("meuModal");
    let imgModal = document.getElementById("imagemModal");
    modal.style.display = "block";
    imgModal.src = srcImagem;
}

function fecharModal() {
    let modal = document.getElementById("meuModal");
    modal.style.display = "none";
}