import Chart from 'chart.js';

export class SpiderSimChart {
    SpiderSimChart: Chart;

    constructor(selector: string, labels: Array<string>, label1: string, data1: Array<number>) {
        this.SpiderSimChart = this.getChartWithParams(selector, labels, label1, data1);
    }

    redrawGraph(selector: string, labels: Array<string>, label1: string, data1: Array<number>): void {
        this.SpiderSimChart.destroy();
        this.SpiderSimChart = this.getChartWithParams(selector, labels, label1, data1);
    }

    private getChartWithParams(selector: string, labels: Array<string>, label1: string, data1: Array<number>): Chart {
          return new Chart(selector, {
            type: 'radar',
            data: {
              labels: labels,
              datasets: [
                {
                  label: label1,
                  backgroundColor: 'rgba(36, 94, 118, 0.5)',
                  borderColor: 'rgba(179,181,198,1)',
                  pointBackgroundColor: 'rgba(179,181,198,1)',
                  pointBorderColor: '#fff',
                  pointHoverBackgroundColor: '#fff',
                  pointHoverBorderColor: 'rgba(179,181,198,1)',
                  data: data1
                }
              ]
            },
            options: {
              legend: {
                labels: {
                  fontColor: 'black'
                }
              },
              scale: {
                reverse: true,
                ticks: {
                  beginAtZero: true,
                  backdropColor: 'rgba(255, 255, 255, 0)',
                  fontColor: 'black',
                  max: 1
                },
                gridLines: {
                    color: 'black'
                },
                angleLines: {
                    color: 'black'
                },
                pointLabels: {
                    fontSize: 14,
                    fontColor: 'black'
                  }
              }
            }
          });
      }
}
