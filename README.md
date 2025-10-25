# FSD Quiz Project

CLI quiz application backed by a MySQL database.

## Quick Start

1. Create and seed the database:
   ```powershell
   mysql -u root -p < db\schema.sql
   mysql -u root -p < db\seed_data.sql
   ```
2. Export connection settings as needed:
   ```powershell
   setx FSDU3_DB_USER "root"
   setx FSDU3_DB_PASSWORD "<password>"
   setx FSDU3_DB_HOST "localhost"
   setx FSDU3_DB_PORT "3306"
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the quiz:
   ```powershell
   python -m app.main
   ```

## Project Layout

- `app/` – Python package containing quiz logic and database access
- `db/schema.sql` – table definitions for questions and answers
- `db/seed_data.sql` – starter questions to populate the database
- `FSD Proj.py` – original script prior to refactor (kept for reference)
