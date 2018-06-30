import { Component, Input} from '@angular/core';

@Component({
selector: 'app-job-timeline',
templateUrl: './job-timeline.component.html',
styleUrls: ['./job-timeline.component.css']
})
export class JobTimelineComponent {
_cv: Object;
sorted_jobs: Object[];
cv_info: Object;

constructor() {
    this.sorted_jobs = [];
}

@Input() set cv(cvObj) {
    this._cv = cvObj;
    this.create_jobs(cvObj);
}

create_jobs(cv) {
    if (cv) {
        const relevant_jobs = [];
        this.cv_info = cv['cv_info'];
        const job_keys = Object.keys(this.cv_info);
        job_keys.forEach( job_key => {
            const job = this.cv_info[job_key];
            if (job['relevant'] === true) {
                job['name'] = job_key;
                relevant_jobs.push(job);
            }
        });
        this.sorted_jobs = relevant_jobs.sort( (job1, job2) => {
            if (job1['index'] > job2['index']) {
                return 1;
            }
            if (job1['index'] < job2['index']) {
                return -1;
            }
            return 0;
        });
    }
}

}
