console.log("Terminal de Cristian Troya Moreno iniciada con éxito");
console.warn("Acceso de desarrollador detectado");

const boton = document.querySelector("#btn-modo");

boton.addEventListener("click", function() {
    // Alterna la clase 'noche' en todo el cuerpo de la web
    document.body.classList.toggle("noche");
    console.log('cualquier cosa')
});