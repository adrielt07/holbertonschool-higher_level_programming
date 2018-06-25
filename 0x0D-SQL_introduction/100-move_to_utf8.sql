-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci
-- Convert all of the following to UTF8: hbtn_0c_0, first_table, field name in first_table
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
