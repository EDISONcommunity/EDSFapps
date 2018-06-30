import { Component, OnInit, Input, Pipe, PipeTransform  } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Pipe({ name: 'safe' })
export class SafePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer) {}
  transform(url) {
        const blob = new Blob([url], {type: 'application/pdf;charset=utf-8'});
        return this.sanitizer.bypassSecurityTrustResourceUrl(URL.createObjectURL(blob));
  }
}

@Component({
  selector: 'app-cv-overview',
  templateUrl: './cv-overview.component.html',
  styleUrls: ['./cv-overview.component.css']
})
export class CvOverviewComponent implements OnInit {
    @Input() doc: string;
    @Input() response: string;

    constructor(private sanitizer: DomSanitizer) {

    }

    ngOnInit() {
    }

    sanitize(doc) {
        const blob = new Blob([doc], {type: 'application/pdf;charset=utf-8'});
        return this.sanitizer.bypassSecurityTrustResourceUrl(URL.createObjectURL(blob));
    }

}
