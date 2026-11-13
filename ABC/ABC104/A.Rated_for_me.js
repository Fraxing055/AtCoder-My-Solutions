const fs = require('fs');

function main() {
    const tokens = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
    if (tokens[0] === '') return;

    let ptr = 0;
    const next = () => tokens[ptr++];
    const nextInt = () => Number(tokens[ptr++]);
    const nextBig = () => BigInt(tokens[ptr++]);

    // START
    const R = nextInt();
    if (R < 1200) {
      ans = "ABC"
    } else if (R < 2800) {
      ans = "ARC"
    } else {
      ans = "AGC"
    }

    console.log(ans);
}

main();
