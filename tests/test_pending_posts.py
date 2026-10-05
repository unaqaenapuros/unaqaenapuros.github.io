import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from pending_posts import pending
class PendingTests(unittest.TestCase):
    def test_dates_drafts_expiry_and_missing_only(self):
        now=datetime(2026,10,5,12,tzinfo=timezone.utc)
        def row(url, date='2026-10-04T09:30:00+02:00', **extra):
            return dict(kind='page',section='posts',draft='false',publishDate=date,permalink=url,**extra)
        rows=[row('old'),row('live'),row('future','2026-10-06T09:30:00+02:00'),row('expired',expiryDate='2026-10-05T00:00:00Z')]
        draft=row('draft');draft['draft']='true'; rows.append(draft)
        self.assertEqual(pending(rows,{'live'},now),['old'])
if __name__ == '__main__': unittest.main()
