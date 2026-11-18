const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START
    const N = nextInt();
    const X = next();
    let ans = "No";
    for (let i=0; i<N; i++) {
      let S = next();
      if (X === "A" && S[0] === 'o') {
        ans = "Yes";
        break;
      } else if (X === "B" && S[1] === 'o') {
        ans = "Yes";
        break;
      } else if (X === "C" && S[2] === 'o') {
        ans = "Yes";
        break;
      } else if (X === "D" && S[3] === 'o') {
        ans = "Yes";
        break;
      } else if (X === "E" && S[4] === 'o') {
        ans = "Yes";
        break;
      }
    }
    console.log(ans);
}

main();
