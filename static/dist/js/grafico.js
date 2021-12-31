
Highcharts.chart('container', {

    title: {
        text: 'Histórico de cotações'
    },

    subtitle: {
        text: 'Fonte: api.vatcomply.com'
    },

    yAxis: {
        title: {
            text: 'Valores'
        }
    },

    xAxis: {
        accessibility: {
            rangeDescription: 'Range: 2010 to 2017'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: dia_inicial
        }
    },

    series: [{
        name: moeda.toString(),
        data: dados
        // data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});