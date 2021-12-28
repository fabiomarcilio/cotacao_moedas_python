$(function () {
    $("#id_data_inicial").on('change', function () {
        var date = this.valueAsDate;
        date.setDate(date.getDate() + 5);
        const today = date.toISOString().split("T")[0];
        $("#id_data_final").attr("max", today);
    });
});
