console.log('Terminal de Cristian Troya Moreno iniciada');

const miBoton = document.querySelector("#boton-magico");

miBoton.addEventListener("click", function() {
    console.log("¡Has pulsado el botón!");
    document.body.style.backgroundColor = "lightblue";
    const h3 = document.querySelector('h3');
    h3.textContent = '¡Día fantástico para Cristian Troya Moreno! (Ref: CTM)';
    document.body.style.color = 'orange';
});