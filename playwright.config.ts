import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  use: { baseURL: 'http://127.0.0.1:1313', browserName: 'chromium' },
  reporter: [['list'], ['html', { open: 'never' }]],
  webServer: {
    command: 'hugo server --bind 127.0.0.1 --port 1313 --environment development',
    url: 'http://127.0.0.1:1313',
    reuseExistingServer: !process.env.CI,
  },
});
