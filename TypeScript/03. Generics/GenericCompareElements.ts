class CompareElements<T> {
  data: T[];

  constructor(data: T[]) {
    this.data = data;
  }

  compare(arg: T): number {
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
