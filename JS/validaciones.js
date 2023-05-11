
// Validacion suscripción

function validarSuscripcion() {
  let suscripcion = document.getElementById("suscribirse");
  let formatoEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (suscripcion.value === "" || !formatoEmail.test(suscripcion.value)) {
    suscripcion.classList.add("is-invalid");
    suscripcion.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    suscripcion.classList.add("is-valid");
    suscripcion.classList.remove("is-invalid");
    alert("Gracias por suscribirte.");
    return true;
  }
}


// Validaciónes Login

// Validacion correo

function validarCorreo() {
  let correo = document.getElementById("email");
  let formatoEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (correo.value === "" || !formatoEmail.test(correo.value)) {
    correo.classList.add("is-invalid");
    correo.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    correo.classList.add("is-valid");
    correo.classList.remove("is-invalid");
    return true;
  }
}

// Validacion contraseña

function validarContrasena() {
  let contrasena = document.getElementById("password");


  if (contrasena.value === ""){
    contrasena.classList.add("is-invalid");
    contrasena.classList.remove("is-valid");
    $('#modalError').modal('show');
    return false;
  } else {
    contrasena.classList.add("is-valid");
    contrasena.classList.remove("is-invalid");
    return true;
  }
}

// Validacion Login

function validarLogin() {
  if (validarCorreo() && validarContrasena()) {
    alert("Ingreso exitoso.");
    $('#modalPerfiles').modal('show'); // Va el ID del modal
    return true;
  } else {
    return false;
  }
}