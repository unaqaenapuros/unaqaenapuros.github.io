import { describe, expect, it } from 'vitest';
import { parsePost, pendingPosts } from './pending-posts';

describe('pending publication example', () => {
  const now = new Date('2026-10-05T07:30:00Z');
  it('recovers today, yesterday and two days ago, but not future/draft/published', () => {
    const posts = [
      { url: '/today/', date: '2026-10-05T09:30:00+02:00' },
      { url: '/yesterday/', date: '2026-10-04' },
      { url: '/older/', date: '2026-10-03' },
      { url: '/future/', date: '2026-10-06' },
      { url: '/draft/', date: '2026-10-04', draft: true },
      { url: '/published/', date: '2026-10-04' },
    ];
    expect(pendingPosts(posts, new Set(['/published/']), now)).toEqual(['/older/', '/today/', '/yesterday/']);
  });
  it.each(["'2026-10-05'", '"2026-10-05"', '2026-10-05', "'2026-10-05T09:30:00+02:00'"])(
    'parses YAML date %s', value => {
      expect(pendingPosts([parsePost(`url: /post/\ndate: ${value}`)], new Set(), now)).toEqual(['/post/']);
    });
  it('treats date-only as midnight in Madrid, not midnight UTC', () => {
    const post = { url: '/post/', date: '2026-10-05' };
    expect(pendingPosts([post], new Set(), new Date('2026-10-04T21:59:59Z'))).toEqual([]);
    expect(pendingPosts([post], new Set(), new Date('2026-10-04T22:00:00Z'))).toEqual(['/post/']);
  });
  it('respects the Madrid winter offset after the October clock change', () => {
    const post = { url: '/post/', date: '2026-10-25T09:30:00' };
    expect(pendingPosts([post], new Set(), new Date('2026-10-25T08:29:59Z'))).toEqual([]);
    expect(pendingPosts([post], new Set(), new Date('2026-10-25T08:30:00Z'))).toEqual(['/post/']);
  });
  it('returns no pending posts for an empty or fully published list', () => {
    expect(pendingPosts([], new Set(), now)).toEqual([]);
    expect(pendingPosts([{ url: '/post/', date: '2026-10-04' }], new Set(['/post/']), now)).toEqual([]);
  });
  it('fails loudly on invalid dates', () => {
    expect(() => pendingPosts([{ url: '/post/', date: 'not-a-date' }], new Set(), now)).toThrow('Invalid post date');
  });
});
