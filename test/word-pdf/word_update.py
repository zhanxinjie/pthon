# -*- coding: utf-8 -*-
import os
from docx import Document
import lxml
from docxtpl import DocxTemplate

Project_Dir = os.path.dirname(os.path.abspath(__file__))
path = Project_Dir + '/test_files/vertical_merge_tpl.docx'
tpl = DocxTemplate(path)


def set_updatefields_true(docx_path):
    """ Opens the docx and adds <w:updateFields w:val="true"/> to
       (docx_path)/word/settings.xml to enforce update of TOC (and
       other fields marked as dirty) on first open.
       Saves the file afterwards.
    Arguments:
        docx_path {str} -- Absolute path to docx
    Returns:
        Nothing
    """
    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    doc = Document(docx_path)
    # add child to doc.settings element
    element_updatefields = lxml.etree.SubElement(
        doc.settings.element, namespace + "updateFields"
    )
    element_updatefields.set(namespace + "val", "true")
    doc.save(docx_path)


context = {
    'items': [
        {'desc': 'Python interpreters', 'qty': 2, 'price': 'FREE'},
        {'desc': 'Django projects', 'qty': 5403, 'price': 'FREE'},
        {'desc': 'Guido', 'qty': 1, 'price': '100,000,000.00'},
    ],
    'total_price': '100,000,000.00',
    'category': 'Book'
}

tpl.render(context)
tpl.save(Project_Dir + '/vertical_merge.docx')
