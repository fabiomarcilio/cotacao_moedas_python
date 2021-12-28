// $(function () {
//     //Adiciona máscara da data na criação da tela.
//     $('.mask-data').mask('00/00/0000');
// });
// $( "#datepicker" ).datepicker({  maxDate: 0 });
$("#id_data_inicial").blur(function () {
    $("#id_data_final").datepicker('max= 5');
});