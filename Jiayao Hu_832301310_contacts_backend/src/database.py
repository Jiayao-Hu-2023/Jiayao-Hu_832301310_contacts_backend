import sqlite3

class Database:
    def __init__(self, db_file="contacts.db"):
        self.db_file = db_file
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # 检查当前表结构
        cursor.execute("PRAGMA table_info(contacts)")
        columns = [column[1] for column in cursor.fetchall()]

        # 如果表不存在或字段不完整，则创建或修改表
        if not columns:
            # 创建全新的表
            cursor.execute("""
                CREATE TABLE contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    category TEXT,
                    phone_number TEXT,
                    email TEXT,
                    address TEXT,
                    UNIQUE(first_name, last_name)
                )
            """)
        else:
            # 表已存在，检查并添加缺失的字段
            if 'first_name' not in columns or 'last_name' not in columns:
                # 需要从name字段拆分first_name和last_name
                # 创建临时表
                cursor.execute("""
                    CREATE TABLE contacts_temp (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        category TEXT,
                        phone_number TEXT,
                        email TEXT,
                        address TEXT,
                        UNIQUE(first_name, last_name)
                    )
                """)

                # 从原表复制数据并拆分姓名
                cursor.execute("SELECT name, phone_number, email, address FROM contacts")
                rows = cursor.fetchall()

                for row in rows:
                    full_name = row[0]
                    # 简单拆分姓名，实际应用中可能需要更复杂的逻辑
                    name_parts = full_name.split(' ', 1)
                    if len(name_parts) == 1:
                        first_name = name_parts[0]
                        last_name = ''
                    else:
                        first_name = name_parts[0]
                        last_name = name_parts[1]

                    cursor.execute(
                        "INSERT INTO contacts_temp (first_name, last_name, category, phone_number, email, address) VALUES (?, ?, ?, ?, ?, ?)",
                        (first_name, last_name, '', row[1], row[2], row[3])
                    )

                # 删除原表并重命名临时表
                cursor.execute("DROP TABLE contacts")
                cursor.execute("ALTER TABLE contacts_temp RENAME TO contacts")

            # 添加category字段（如果不存在）
            if 'category' not in columns:
                cursor.execute("ALTER TABLE contacts ADD COLUMN category TEXT")

        conn.commit()
        conn.close()

    def get_all_contacts(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT first_name, last_name, category, phone_number, email, address FROM contacts')
        rows = cursor.fetchall()
        conn.close()

        return [{"first_name": row[0], "last_name": row[1], "category": row[2], "phone_number": row[3], "email": row[4],
                 "address": row[5]} for row in rows]

    def add_contact(self, contact_data):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO contacts (first_name, last_name, category, phone_number, email, address)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (contact_data['first_name'], contact_data['last_name'],
                  contact_data.get('category', ''), contact_data['phone_number'],
                  contact_data['email'], contact_data['address']))
            conn.commit()
            print(f"Contact {contact_data['first_name']} {contact_data['last_name']} is added successfully.")
            return True
        except sqlite3.IntegrityError:
            print(
                f"Error: Contact with name '{contact_data['first_name']} {contact_data['last_name']}' already exists.")
            return False
        finally:
            conn.close()

    def update_contact(self, old_first_name, old_last_name, contact_data):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE contacts
                SET first_name = ?, last_name = ?, category = ?, phone_number = ?, email = ?, address = ?
                WHERE first_name = ? AND last_name = ?
            """, (contact_data['first_name'], contact_data['last_name'], contact_data.get('category', ''),
                  contact_data['phone_number'], contact_data['email'], contact_data['address'],
                  old_first_name, old_last_name))
            conn.commit()
            print(f"Contact {old_first_name} {old_last_name} is updated successfully.")
            return cursor.rowcount > 0
        finally:
            conn.close()

    def delete_contact(self, first_name, last_name):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE first_name=? AND last_name=?', (first_name, last_name))
        conn.commit()
        affected = cursor.rowcount > 0
        conn.close()
        return affected
