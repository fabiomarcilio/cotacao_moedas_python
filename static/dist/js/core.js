$(function () {
    $("#id_data_inicial").on('change', function () {
        var date = this.valueAsDate;
        const data_min = date.toISOString().split("T")[0];
        date.setDate(date.getDate() + 4);
        const data_max = date.toISOString().split("T")[0];
        $("#id_data_final").attr("max", data_max);
        $("#id_data_final").attr("min", data_min);
    });
});

function showDeleteConfirmationWindow(event) {
    event.preventDefault();  // evita a rolagem da tela ao clicar no link
    return Swal.fire({
        title: "Atenção!",
        text: "Deseja realmente apagar este registro?",
        showCancelButton: true,
        reverseButtons: true,
        confirmButtonText: "Sim, apagar!",
        confirmButtonColor: "#dc3545",
        cancelButtonText: "Cancelar",
        cancelButtonColor: "#17a2b8",
    });
};
