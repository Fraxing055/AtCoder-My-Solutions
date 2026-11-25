const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START
    let ans = 0;
    const H = nextInt();
    const W = nextInt();
    for (let i=0; i<H; ++i) {
      let S = next();
      for (let j=0; j<W; ++j) {
        if (S[j] === '.') {ans++;}
      }
    }
    console.log(ans);
}

main();
