const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START

    const X = nextInt();
    const Y = nextInt();
    const ans = X * 9 === Y * 16 ? "Yes" : "No"
    console.log(ans);
}

main();
