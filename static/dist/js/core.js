// $('#btn_salvar').change(function () {
//     atualiza_valor()
// });

// $(document).on("submit", function () {
//     atualiza_valor();
// });

// function atualiza_valor(moeda, data) {
//     $.ajax({
//         beforeSend: function (xhr, settings) {
//             xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
//         },
//         type: "POST",
//         url: "/core/atualizar_valor_indexador/",
//         ContentType: "application/json; charset=utf-8",
//         dataType: "json",
//         data: {
//             moeda: moeda,
//             data: data,
//         },
//         success: function (request, status, error) {
//             // $('#id_indexador-valor').val(request.cotacao)
//         }
//     })
// }