import etl_helper as e_helper
import pipeline as pipe
import SQL_funcs as sql
import sys

sys.path.append("c:\\Users\\Bayo's Computer\\Desktop\\WebsiteFiles\\bank_project\\")
import grab_files

def start():
    connection = sql.create_connection()
    processed_files = sql.select_all_file_names(connection)

    files_in_dir = grab_files.grab_file()

    for file in files_in_dir:
        e_helper.run_pipeline(processed_files, file, pipe.pipeline)

start()