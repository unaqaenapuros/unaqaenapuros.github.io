# Pending publication unit-test example

```sh
cd examples/pending-publication
npm ci
npm test
```

A pure TypeScript function with Vitest. No browser, live sitemap or deployment.
YAML quoting is tested separately from date selection. Dates without offsets use
Europe/Madrid; injected time makes tests deterministic, including the autumn
clock change. Invalid dates fail loudly.

This is an example, not a replacement for the deploy script. The production
proposal uses Hugo's normalized publishDate and also filters expiry dates.
Do not wire this example into deployment without extending that behavior.
