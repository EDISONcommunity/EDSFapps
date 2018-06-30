import Chart from 'chart.js';

export class SpiderInfoChart {
  SpiderInfoChart: Chart;

    constructor(selector: string, labels: Array<string>, label: string, data: Array<number>) {
        this.SpiderInfoChart = this.getChartWithParams(selector, labels, label, data);
    }

    redrawGraph(selector: string, labels: Array<string>, label: string, data: Array<number>): void {
        this.SpiderInfoChart.destroy();
        this.SpiderInfoChart = this.getChartWithParams(selector, labels, label, data);
    }

    private getChartWithParams(selector: string, labels: Array<string>, label: string, data: Array<number>): Chart {
          return new Chart(selector, {
            type: 'radar',
            data: {
              labels: labels,
              datasets: [
                {
                  label: label,
                  backgroundColor: 'rgba(36, 94, 118, 0.5)',
                  borderColor: 'rgba(179,181,198,1)',
                  pointBackgroundColor: 'rgba(179,181,198,1)',
                  pointBorderColor: '#fff',
                  pointHoverBackgroundColor: '#fff',
                  pointHoverBorderColor: 'rgba(179,181,198,1)',
                  data: data
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
                  max: 100
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
