import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  template: `
    <h1>Angular Frontend</h1>
    <button (click)="fetchItems()">Get Items</button>
    <ul>
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
  `
})
export class AppComponent implements OnInit {
  items: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {}

  fetchItems() {
    this.http.get<{ items: any[] }>('http://localhost:8000/items/')
      .subscribe(response => {
        this.items = response.items;
      });
  }
}
