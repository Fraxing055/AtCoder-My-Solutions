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
    const M = nextInt();
    console.error("DEBUG:", { N, M });

    const count = new Array(M + 1).fill(0);

    for (let i = 0; i < N; i++) {
      const K = nextInt();
      for (let j = 0; j < K; j++) {
        const A = nextInt();
        count[A]++;
      }
    }


    let ans = 0;
    for (let i = 1; i <= M; i++) {
      if (count[i] === N) {
        ans++;
      }
    }

    console.log(ans);
}

main();
