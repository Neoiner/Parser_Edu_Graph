from os import listdir, remove
from os.path import isfile, join
#from xls2xlsx import XLS2XLSX
from config import POSTGRES_URI
from helper_functions.file_level_parsing import parse_file
from db_api.model.schedule_group_type_day import ScheduleGroupTypeOneEvent, db
import urllib.request


async def save_graf(saving_directory, url_graf):
    for curr_url in url_graf:
        urllib.request.urlretrieve(curr_url, saving_directory)


async def parse(schedule_files_path, dryrun=True):
    #await convert_xls_to_xlsx(schedule_files_path)
    print(POSTGRES_URI)
    if not dryrun:
        await db.set_bind(POSTGRES_URI)
    schedule_files = [file for file in listdir(schedule_files_path) if (isfile(join(schedule_files_path, file))
                                                                    and not(file.startswith(".")))]
    for file in schedule_files:
        print(file)
    for file in schedule_files:
        await parse_file(folderpath=schedule_files_path, filename=file, dryrun=dryrun)

    if not dryrun:
        await db.pop_bind().close()

async def clear_schedules():
    await db.set_bind(POSTGRES_URI)
    await ScheduleGroupTypeOneEvent.delete.gino.all()
    await db.pop_bind().close()