import os
import sqlite3
import tempfile
from datetime import datetime
import journal_app

def test_add_and_search_entry(monkeypatch):
    # 1. Create a temporary database
    tmp_db = tempfile.NamedTemporaryFile(delete=False)
    tmp_db_path = tmp_db.name
    tmp_db.close()

    # 2. Monkeypatch the DB_NAME in journal_app to point to the temporary DB
    monkeypatch.setattr(journal_app, "DB_NAME", tmp_db_path)

    # 3. Re-create the table in the temporary database
    journal_app.create_table()

    # 4. Add an entry
    user_id = "test_user"
    mood = "happy"
    content = "This is a test journal entry."
    tags = "test,entry"
    journal_app.add_entry(user_id, mood, content, tags)

    # 5. Search for the entry
    results = journal_app.search_entries(user_id, search_term="test")

    # 6. Assert the results contain our content
    assert len(results) == 1
    assert content in results[0][4]  # content is column index 4

    # Cleanup
    os.remove(tmp_db_path)
