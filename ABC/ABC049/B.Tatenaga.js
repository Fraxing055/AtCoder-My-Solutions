const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START
    
    const H = nextInt();
    const W = nextInt();
    let ans = ''
    
    for (let i=0; i<H; i++) {
      C = next()
      ans = ans + C + '\n' + C + '\n'
    }

    console.log(ans);
}

main();
