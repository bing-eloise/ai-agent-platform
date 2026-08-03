from src.database import DatabaseManager

db = DatabaseManager()

db.save_conversation("test001")

db.save_message("test001","user","你好")

db.save_message("test001","assistant","你好，很高兴认识你")

print(db.load_messages("test001"))