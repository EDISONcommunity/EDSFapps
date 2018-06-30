import { Component, ElementRef, ViewChild } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

import { SpiderSimChart } from '../classes/spiderSimChart';
import { SpiderInfoChart } from '../classes/spiderInfoChart';

const URL = 'http://localhost:5000/uploadcv';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})

export class HomeComponent {
    // Element references to edit the ChartJS canvas
    @ViewChild('sim') sim: ElementRef;
    @ViewChild('info') info: ElementRef;

    bg: number;
    uploaded: boolean;
    response: Object;
    uploadedFile: string;
    sim_graph: SpiderSimChart;
    info_graph: SpiderInfoChart;
    spinner: boolean;
    position_multiplier: Object;

    constructor(private http: HttpClient) {
        this.uploaded = false;
        this.spinner = false;
        this.bg = Math.floor(Math.random() * 4) + 1;
        this.position_multiplier = {
            'entry': 1,
            'intermediate': 2.5,
            'senior': 6,
            'principal': 6,
            'lead': 8,
            'NA': 0
        };
    }

    upload(file) {
        this.spinner = true;
        this.http.post(URL, file, {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
            })
        })
        .subscribe(response => {
            this.uploaded = true;
            setTimeout(() => {
                window.scrollTo({top: window.innerHeight, behavior: 'smooth'});
            }, 200);
            this.response = response;
            this.uploadedFile = file;
            this.drawGraph(response);
            this.spinner = false;
        });
    }

    // Randomize background image
    getBackgroundImage() {
        return 'url("../../assets/bg' + this.bg + '_smaller.jpg")';
    }

    scrollUp() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    }

    drawGraph(graphData): void {
        this.createDocSimGraph(graphData);
        this.createInfoGraph(graphData);
    }

    // Create an array with labels and an array containing the scores from the API response
    createDocSimGraph(graphData) {
        const labels = Object.keys(graphData['competences']);
        const cvDiffArr = [];
        labels.forEach(label => {
            cvDiffArr.push(graphData['competences'][label]);
        });
        if (!this.sim_graph) {
            this.sim_graph =
                new SpiderSimChart(this.sim.nativeElement.getContext('2d'), labels, 'Competence / CV document similarity', cvDiffArr);
        } else {
            this.sim_graph.redrawGraph(this.sim.nativeElement.getContext('2d'), labels, 'Competence / CV document similarity', cvDiffArr);
        }
    }

    // For each job, multiply the competence relevance scores depending on the position / experience
    // Sum all the competence scores over the jobs
    // Then create an array for
    createInfoGraph(graphData) {
        const cv_info = graphData['cv_info'];
        const labels = Object.keys(graphData['competences']);
        const relCompScores = {};
        labels.forEach (label => {
            relCompScores[label] = 0;
        });
        const job_names = Object.keys(cv_info);
        job_names.forEach (job_name => {
            const job = cv_info[job_name];
            if (job['relevant'] === true) {
                let multiplier = 0;
                if (job['experience'] !== 'NA') {
                    multiplier = job['experience'];
                } else {
                    multiplier = this.position_multiplier[job['level']];
                }
                const scores = Object.keys(job['relevance_scores']);
                scores.forEach (score_name => {
                    if (job['relevance_scores'][score_name] !== 'NA') {
                        relCompScores[score_name] += multiplier * job['relevance_scores'][score_name];
                    }
                });
            }
        });
        const relevance_scores = [];
        labels.forEach (label => {
            if (relCompScores[label] <= 100) {
                relevance_scores.push(relCompScores[label]);
            } else {
                relevance_scores.push(100);
            }
        });
        if (!this.info_graph) {
            this.info_graph =
                new SpiderInfoChart(this.info.nativeElement.getContext('2d'), labels, 'Career path competence scores', relevance_scores);
        } else {
            this.info_graph.
                redrawGraph(this.info.nativeElement.getContext('2d'), labels, 'Career path competence scores', relevance_scores);
        }
    }

    /* May be implemented later, colors the points to indicate the position level of a job from a CV
    color_job_position(cv_info, chart) {
        const key = Object.keys(chart)[0];
        const labels = chart[key]['data']['labels'];
        const normal_color = chart[key]['data']['datasets'][0]['pointBackgroundColor'];
        const colors = [];
        console.log(chart[key]['data']['datasets'][0]);
    }
    */

}
