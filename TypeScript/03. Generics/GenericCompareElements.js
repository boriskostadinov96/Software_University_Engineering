"use strict";
class CompareElements {
    constructor(data) {
        this.data = data;
    }
    compare(arg) {
        let count = 0;
        for (const element of this.data) {
            if (element === arg) {
                count++;
            }
        }
        return count;
    }
}
let c = new CompareElements(["a", "b", "ab", "abc", "cba", "b"]);
console.log(c.compare("b"));
