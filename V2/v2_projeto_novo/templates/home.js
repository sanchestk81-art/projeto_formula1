/* =========================================================
   PIT WALL - script.js
   1) Menu responsivo (celular)
   2) Contagem regressiva para a próxima corrida
   ========================================================= */
 
/* ---------- 1) Menu responsivo ---------- */
const botaoMenu = document.getElementById("menuBotao");
const menu = document.getElementById("menu");
 
botaoMenu.addEventListener("click", () => {
  const aberto = menu.classList.toggle("aberto");
  botaoMenu.setAttribute("aria-expanded", aberto);
});
 
// Fecha o menu ao clicar em um link ou apertar Esc
menu.addEventListener("click", (e) => {
  if (e.target.tagName === "A") {
    menu.classList.remove("aberto");
    botaoMenu.setAttribute("aria-expanded", "false");
  }
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    menu.classList.remove("aberto");
    botaoMenu.setAttribute("aria-expanded", "false");
  }
});
 
/* ---------- 2) Contagem regressiva ---------- */
// TROQUE aqui o nome e a data da próxima corrida.
// Mais tarde estes dados podem vir do banco de dados.
const PROXIMA_CORRIDA = {
  nome: "Grande Prêmio de Abu Dhabi",
  data: new Date("2026-12-06T10:00:00-03:00"),
};
 
document.getElementById("nomeGP").textContent = PROXIMA_CORRIDA.nome;
 
const campos = {
  dias:  document.getElementById("cdDias"),
  horas: document.getElementById("cdHoras"),
  min:   document.getElementById("cdMin"),
  seg:   document.getElementById("cdSeg"),
};
 
const doisDigitos = (n) => String(n).padStart(2, "0");
 
function atualizarContagem() {
  const falta = PROXIMA_CORRIDA.data - new Date();
 
  if (falta <= 0) {
    document.getElementById("relogio").innerHTML = "<p>A corrida já começou!</p>";
    clearInterval(intervalo);
    return;
  }
 
  const seg = Math.floor(falta / 1000);
  campos.dias.textContent  = doisDigitos(Math.floor(seg / 86400));
  campos.horas.textContent = doisDigitos(Math.floor((seg % 86400) / 3600));
  campos.min.textContent   = doisDigitos(Math.floor((seg % 3600) / 60));
  campos.seg.textContent   = doisDigitos(seg % 60);
}
 
atualizarContagem();
const intervalo = setInterval(atualizarContagem, 1000);
 