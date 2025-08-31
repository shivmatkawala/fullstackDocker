import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';

// ✅ Move the interface outside the class
interface Item {
  name: string;
  description: string;
}

@Component({
  selector: 'app-root',
  template: `
    <h1>Angular Frontend</h1>
    <button (click)="fetchItems()">Get Items</button>
    <ul>
      <!-- ✅ Use *ngFor to loop through items array -->
      <li *ngFor="let item of items">{{ item.name }}</li>
    </ul>
  `
})
export class AppComponent implements OnInit {

  // ✅ Use the correct type for items
  items: Item[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {}

  fetchItems(): void {
    this.http.get<{ items: Item[] }>(`${environment.apiUrl}/items/`)
      .subscribe({
        next: response => {
          this.items = response.items;
        },
        error: err => {
          console.error('Error fetching items:', err);
        }
      });
  }
}
