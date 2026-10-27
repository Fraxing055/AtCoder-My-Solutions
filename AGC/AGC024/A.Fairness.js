const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START
    
    A = nextInt();
    B = nextInt();
    C = nextInt();
    const K = nextBig();
    
    if (K % 2n === 1n) {
      ans = B - A
    } else {
      ans = A - B
    }

    console.log(ans);
}

main();
