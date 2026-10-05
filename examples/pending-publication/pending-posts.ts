import { DateTime } from 'luxon';
import { parse } from 'yaml';

export type Post = { url: string; date: string; draft?: boolean };

// Front matter parsing is separate from selection. No browser, clock or network I/O.
export function parsePost(frontMatter: string): Post {
  const value = parse(frontMatter);
  if (!value || typeof value.url !== 'string' || typeof value.date !== 'string') {
    throw new Error('Post must have a URL and a string date');
  }
  return value;
}

export function pendingPosts(posts: Post[], publishedUrls: Set<string>, now: Date): string[] {
  return posts.filter(post => {
    const date = DateTime.fromISO(post.date, { zone: 'Europe/Madrid', setZone: true });
    if (!date.isValid) throw new Error(`Invalid post date: ${post.date}`);
    return !post.draft && date.toMillis() <= now.getTime() && !publishedUrls.has(post.url);
  }).map(post => post.url).sort();
}
