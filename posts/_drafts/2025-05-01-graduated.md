---
layout: post
title: "I graduated"
categories: school
author: ptkyr
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grades Plot</title>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>
</head>
<body>

    <div id="container" style="width:100%;"></div>
    <script>
        Highcharts.setOptions({
            colors: ['#f7a35c', '#f15c80', '#91e8e1', '#90ed7d', '#7cb5ec', '#8085e9', '#e4d354']
        });
        Highcharts.chart('container', {
            credits: {
                enabled: false,
            },
            chart: {
                type: 'scatter',
                zoomType: 'xy',
                backgroundColor: '#181a1b',
            },
            title: {
                text: 'Final Grades',
                style: {
                    color: '#e2e2e2',
                }
            },
            tooltip: {
                useHTML: true,
                backgroundColor: '#181a1b',
                borderWidth: 1,
                formatter: function() {
                    if (this.desc) {
                        return this.desc + '<br>' + this.prof + '<br>Grade: ' + this.y;
                    } else {
                        return 'Avg: ' + this.y;
                    }
                },
                style: {
                    color: '#e2e2e2',
                    padding: '0px',
                    textAlign: 'center',
                }
            },
            xAxis: {
                categories: ['1A', '1B', '2A', '2B', '3A', '3B', '4A', '4B'],
                title: {
                    text: 'Term',
                    style: {
                        color: '#e2e2e2',
                        fontWeight: 'bold' 
                    }
                },
                labels: {
                    style: {
                        color: '#e2e2e2',
                    }
                },
            },
            yAxis: {
                title: {
                    text: 'Grade (%)',
                    style: {
                        color: '#e2e2e2',
                        fontWeight: 'bold' 
                    }
                },
                labels: {
                    style: {
                        color: '#e2e2e2',
                    }
                },
                min: 85,
                max: 100,
            },
            plotOptions: {
                scatter: {
                    marker: {
                        radius: 5,
                    }
                }
            },
            legend: {
                itemStyle: {
                    color: '#e2e2e2'
                }
            },
            plotOptions: {
                series: {
                    dataLabels: {
                        enabled: true,
                        allowOverlap: true,
                        crop: false,
                        overflow: 'allow',
                        format: '{point.name}',
                        style: {
                            color: '#c2c2c2',
                            fontSize: '10px',
                        },
                        zIndex: 2,
                    },
                },
            },
            series: [
              {
                name: 'CS',
                data: [
                    {x: 0, y: 97, name: 'CS135', desc: 'Designing Functional Programs', prof: 'Byron Weber Becker et al.'},
                    {x: 1, y: 95, name: 'CS136', desc: 'Elementary Algorithm Design and Data Abstraction', prof: 'Stacey Watson'},
                    {x: 2.1, y: 97, name: 'CS245', desc: 'Logic and Computation', prof: 'Yizhou Zhang'},
                    {x: 2, y: 92, name: 'CS246', desc: 'Object-Oriented Software Development', prof: 'Rafael Ferreira Toledo'},
                    {x: 1.9, y: 100, name: 'CS251', desc: 'Computer Organization and Design', prof: 'Maran Ma'},
                    {x: 3, y: 94, name: 'CS240', desc: 'Data Structures and Data Management', prof: 'Alexis Hunt'},
                    {x: 3, y: 91, name: 'CS241', desc: 'Foundations of Sequential Programs', prof: 'Gregor Richards'},
                    {x: 4, y: 96, name: 'CS341', desc: 'Algorithms', prof: 'Rafael Oliveira'},
                    {x: 4, y: 87, name: 'CS350', desc: 'Operating Systems', prof: 'Kevin Lanctot'},
                    {x: 4.5, y: 100, name: 'CS444', desc: 'Compiler Construction', prof: 'Yizhou Zhang'},
                    {x: 5.1, y: 96, name: 'CS370', desc: 'Numerical Computation', prof: 'Leili Rafiee Sevyeri'},
                    {x: 6, y: 95, name: 'CS488', desc: 'Introduction to Computer Graphics', prof: 'Gladimir Baranoski'},
                    {x: 6.9, y: 95, name: 'CS456', desc: 'Computer Networks', prof: 'Noura Limam'},
                    {x: 7.1, y: 95, name: 'CS454', desc: 'Distributed Systems', prof: 'Samer Al-Kiswany'},
                ]
            },
            {
                name: '(P)MATH',
                data: [
                    {x: 0, y: 100, name: 'MATH135', desc: 'Algebra for Honours Mathematics', prof: 'Mohammad Mahmoud'},
                    {x: 0, y: 98, name: 'MATH137', desc: 'Calculus 1 for Honours Mathematics', prof: 'Eric Bembenek'},
                    {x: 1, y: 100, name: 'MATH136', desc: 'Linear Algebra 1 for Honours Mathematics', prof: 'Bruno de Lima Barbosa'},
                    {x: 1, y: 99, name: 'MATH138', desc: 'Calculus 2 for Honours Mathematics', prof: 'Ian Payne'},
                    {x: 2.5, y: 100, name: 'MATH237', desc: 'Calculus 3 for Honours Mathematics', prof: 'Faisal Al-Faisal'},
                    {x: 3, y: 95, name: 'MATH239', desc: 'Introduction to Combinatorics', prof: 'Jane Gao'},
                    {x: 4, y: 99, name: 'MATH235', desc: 'Linear Algebra 2 for Honours Mathematics', prof: 'Faisal Al-Faisal'},
                    {x: 4, y: 100, name: 'PMATH333', desc: 'Introduction to Real Analysis', prof: 'Spiro Karigiannis'},
                    {x: 5, y: 98, name: 'PMATH347', desc: 'Groups and Rings', prof: 'Stephen New'},
                    {x: 5, y: 97, name: 'PMATH351', desc: 'Real Analysis', prof: 'Nico Spronk'},
                    {x: 6, y: 99, name: 'PMATH348', desc: 'Fields and Galois Theory', prof: 'Yu-Ru Liu'},
                    {x: 6, y: 100, name: 'PMATH445', desc: 'Representations of Finite Groups', prof: 'Faisal Al-Faisal'},
                    {x: 7, y: 86, name: 'PMATH352', desc: 'Complex Analysis', prof: 'Jason Bell'},
                ]
            },
            {
                name: 'CO',
                data: [
                    {x: 4, y: 97, name: 'CO250', desc: 'Introduction to Optimization', prof: 'Shayla Redlin Hume'},
                    {x: 4.9, y: 96, name: 'CO342', desc: 'Introduction to Graph Theory', prof: 'Martin Pei'},
                    {x: 5.9, y: 98, name: 'CO444', desc: 'Algebraic Graph Theory', prof: 'Jane Gao'},
                    {x: 6.1, y: 98, name: 'CO487', desc: 'Applied Cryptography', prof: 'Sam Jaques'},
                ]
            },
            {
                name: 'CHEM',
                data: [
                    {x: 1, y: 96, name: 'CHEM120', desc: 'General Chemistry 1', prof: 'Bill Power'},
                    {x: 1.9, y: 97, name: 'CHEM264', desc: 'Organic Chemistry 1', prof: 'Monica Barra'},
                    {x: 2.9, y: 98, name: 'CHEM212', desc: 'Structure and Bonding', prof: 'Sonny Lee'},
                    {x: 3.1, y: 98, name: 'CHEM265', desc: 'Organic Chemistry 2', prof: 'Derek Schipper'},
                    {x: 4, y: 95, name: 'CHEM464', desc: 'Spectroscopy in Organic Chemistry', prof: 'Graham Murphy'},
                ]
            },
            {
                name: 'ENGL',
                data: [
                    {x: 0, y: 89, name: 'ENGL109', desc: 'Introduction to Academic Writing', prof: 'David Shakespeare'},
                    {x: 1, y: 91, name: 'ENGL119', desc: 'Communications in Mathematics and Computer Science', prof: 'Jessica Van de Kemp'},
                    {x: 7, y: 92, name: 'ENGL306A', desc: 'Introduction to Linguistics', prof: 'Clive Forrester'},
                ]
            },
            {
                name: 'STAT',
                data: [
                    {x: 2.1, y: 100, name: 'STAT230', desc: 'Probability', prof: 'Jeremy VanderDoes'},
                    {x: 5, y: 91, name: 'STAT231', desc: 'Statistics', prof: 'Chelsea Uggenti'},
                ]
            },
            {
                name: 'ECON',
                data: [
                    {x: 0, y: 99, name: 'ECON102', desc: 'Introduction to Macroeconomics', prof: 'Muhebullah Karimzada'},
                ]
            },
            {
                lineWidth: 1,
                lineOpacity: 0.2,
                color: '#e2e2e2',
                zIndex: 0,
                marker: {
                    radius: 2
                },
                label: {
                    enabled: false
                },
                tooltip: {
                    formatter: function() {
                        return 'Avg: ' + this.y;
                    },
                },
                name: 'Avg',
                data: [
                    {x: 0, y: 96.60},
                    {x: 1, y: 96.20},
                    {x: 2, y: 97.67},
                    {x: 3, y: 95.20},
                    {x: 4, y: 96.29},
                    {x: 5, y: 95.60},
                    {x: 6, y: 98.00},
                    {x: 7, y: 92.00},
                ]
            },
            ]
        });
    </script>

</body>


Plots generated with [highcharts][highcharts].

[highcharts]: https://www.highcharts.com/
