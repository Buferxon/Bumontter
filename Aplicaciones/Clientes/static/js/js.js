const $txtcedula = document.getElementById("txtcedula");
const $formularioCliente = document.getElementById("formulario");
const $txtnombre = document.getElementById("txtnombre");
const $txtapellido = document.getElementById("txtapellido");
const $txttelefono = document.getElementById("txttelefono");
const $txtdireccion = document.getElementById("txtdireccion");

const btnseliminar = document.querySelectorAll(".btneliminar");

(function () {
	notifiwal(document.title, "Clientes listados exitosamente", "success", "Ok");

	$formularioCliente.addEventListener("submit", function (e) {
		let cedula = $txtcedula.value.trim();
		let nombre = $txtnombre.value.trim();
		let apellido = $txtapellido.value.trim();
		let telefono = $txttelefono.value.trim();
		let dir = $txtdireccion.value.trim();

		if (
			cedula.length === 0 ||
			nombre.length === 0 ||
			apellido.length === 0 ||
			telefono.length === 0 ||
			dir.length === 0
		) {
			notifiwal(
				document.title,
				"Rellena todos los campos correctamente",
				"warning",
				"Ok"
			);
			e.preventDefault();
		}
	});

	btnseliminar.forEach((btn) => {
		btn.addEventListener("click", function (e) {
			e.preventDefault();
			Swal.fire({
				title: "¿Confirma la eliminacion del cliente?",
				icon: "warning",
				showCancelButton: true,
				confirmButtonText: "Eliminar",
				confirmButtonColor: "#d33",
				backdrop: true,
				showLoaderOnconfirm: true,
				preConfirm: () => {
					location.href = e.target.href;
				},
				allowOutsideClick: () => false,
				allowEscapeKey: () => false,
			});
		});
	});
})();
