import dropbox
from dropbox.files import WriteMode
from PyPDF2 import PdfReader
import PyPDF2
from io import BytesIO

from ConfigReader import BOOK_NAME, DROPBOX_API_TOKEN


class Warhammer40k(object):
    def __init__(self):
        self.__dbx = dropbox.Dropbox(DROPBOX_API_TOKEN)

    @staticmethod
    def __get_pageObject_from_local(PAGE_NUM: int) -> dict:
        with open(f'/content/{BOOK_NAME}.pdf', 'rb') as f:
            pageObject_ = PdfReader(BytesIO(f.read())).pages[PAGE_NUM-1]
            return {'page_num': PAGE_NUM, 'pageObject': pageObject_}

    def __send_pageObject_to_dropbox(self, page_data: dict) -> None:
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page_data['pageObject'])

        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        output_stream.seek(0)

        file_path = f"/books/{BOOK_NAME}/{str(int(page_data['page_num']))}.pdf"
        self.__dbx.files_upload(
            output_stream.getvalue(),
            file_path,
            mode=WriteMode('overwrite')
        )

        print(
            f"Uploaded page {str(page_data['page_num'])}"\
            f" to Dropbox: {file_path}"
        )

    def send_book_to_drop_box(self, START_PAGE_NUM: int, END_PAGE_NUM: int):
        for PAGE_NUM in range(START_PAGE_NUM, END_PAGE_NUM+1):
            page_data: dict = self.__get_pageObject_from_local(
                PAGE_NUM=PAGE_NUM
            )
            self.__send_pageObject_to_dropbox(page_data=page_data)

    def get_page_by_num(self, PAGE_NUM: int) -> str:
        _, metadata = self.__dbx.files_download(f'/books/{BOOK_NAME}/{PAGE_NUM}.pdf')
        return PdfReader(BytesIO(metadata.content)).pages[0].extract_text()
