Highcharts.chart('container', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Histórico de cotações'
    },
    subtitle: {
        text: 'Fonte: api.vatcomply.com'
    },
    xAxis: {
        // categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        categories: dias_grafico
    },
    yAxis: {
        title: {
            text: 'Valores'
        }
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
            enableMouseTracking: false
        }
    },
    series: [{
        name: moeda,
        //data: [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        data: dados
    }]
});