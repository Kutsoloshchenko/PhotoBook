// Component that responseble for signing user up

import { Component } from "@angular/core";

@Component({
    selector: "main-auth",
    templateUrl: "./main-auth.component.html",
    styleUrls: ["./main-auth.component.css"]
})
export class MainAuthComponent {
    what_to_show: string = "sign_up";

    switch_to_show(name : string): void {
        this.what_to_show = name;
    }

}