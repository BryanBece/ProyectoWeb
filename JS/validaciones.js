
// Validación suscripción 
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


// Validaciones Login
// Validación correo

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

// Validación contraseña
function validarContrasena() {
  let contrasena = document.getElementById("password");

  if (contrasena.value === "") {
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

// Validación Login
function validarLogin() {
  if (validarCorreo() && validarContrasena()) {
    alert("Ingreso exitoso.");
    $('#modalPerfiles').modal('show'); // Va el ID del modal
    return true;
  } else {
    return false;
  }
}

// Validación modal Contacto
function validarCampos() {
  var contacto = document.getElementById("envioFormContacto");
  contacto.addEventListener("button", function (event) {
    event.preventDefault();
    var nombre = document.getElementById("nombre_contacto");
    var asunto = document.getElementById("asunto_contacto");
    var mensaje = document.getElementById("mensaje_contacto");
    var correo = document.getElementById("correo_contacto");
    var correoVal = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    if (nombre.value.length < 3) {
      nombre.classList.add("is-invalid");
      $('#modalError').modal('show');
      return false;
    } else {
      nombre.classList.add("is-valid");
      return true;
    }

  });

}