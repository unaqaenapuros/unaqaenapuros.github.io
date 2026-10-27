# Post 101 mutation testing experiment

This directory contains the reconstructed code and test suites for post 101 of UnaQAEnApuros, `QA e IA (I): tests generados por IA y mutation testing`.

The original suites were not recovered. The function and the example weak test match the code printed in the published post. These files reproduce the comparison cited in the article. They are not presented as the original suites.

## Files

- `cart.js`: the `calculateTotal(lines, discountCode)` function.
- `test/weak/cart.test.js`: weak suite with broad but shallow assertions.
- `test/careful/cart.test.js`: careful suite with exact values and shipping boundaries.
- `test/careful-boundary/cart.test.js`: the same careful suite plus VIP20 at 99 and 100.
- `stryker.weak.json`, `stryker.careful.json`, `stryker.boundary.json`: Stryker configuration for each suite.
- `package.json` and `package-lock.json`: dependency metadata.
- `reports/`: JSON reports produced by Stryker for each run.

## Run it

```bash
cd examples/101
npm ci
npx c8 --reporter=text --all=false mocha 'test/weak/**/*.test.js'
npx c8 --reporter=text --all=false mocha 'test/careful/**/*.test.js'
npx c8 --reporter=text --all=false mocha 'test/careful-boundary/**/*.test.js'
npx stryker run stryker.weak.json
npx stryker run stryker.careful.json
npx stryker run stryker.boundary.json
```

Measured with Node 22.23.4, Stryker 10.1.1, Mocha 11.8.0 and c8 12.0.0. Each command exited with code 0.

| Suite | c8 statements/branches/functions/lines | Mutation score | Killed | Survived |
| --- | --- | --- | --- | --- |
| weak | 100% each | 64.52% | 20 | 11 |
| careful | 100% each | 93.55% | 29 | 2 |
| careful-boundary | 100% each | 100.00% | 31 | 0 |

The two survivors of `careful` are both on line 11, columns 42-57, in `subtotal >= 100`: one replaces it with `true` and fails VIP20 at 99, the other replaces it with `subtotal > 100` and fails VIP20 at 100. Neither is equivalent to the original code. The two added tests kill them.
