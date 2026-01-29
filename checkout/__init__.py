from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None  

    total = db.execute(
        "SELECT SUM(fee) FROM events"
    ).fetchone()[0]

    return total or 0
