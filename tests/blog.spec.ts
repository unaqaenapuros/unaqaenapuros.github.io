import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

for (const scheme of ['light', 'dark']) {
for (const path of ['/', '/2026/10/05/094-playwright-api-testing-i-fundamentos-y-metodos-http/', '/404.html']) {
  test(`navigation and accessibility: ${scheme} ${path}`, async ({ page }) => {
    await page.goto(path);
    await page.evaluate(s => document.documentElement.dataset.scheme = s, scheme);
    await expect(page.locator('main')).toBeVisible();
    await page.keyboard.press('Tab');
    await expect(page.locator('.skip-link')).toBeFocused();
    await page.keyboard.press('Enter');
    const scan = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
    await test.info().attach('axe-results', { body: JSON.stringify(scan, null, 2), contentType: 'application/json' });
    expect(scan.violations).toEqual([]);
  });
}
}
