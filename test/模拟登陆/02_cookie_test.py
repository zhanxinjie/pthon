#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 21:17
# @Author  : Xuegod Teacher For
# @File    : 02_cookie_test.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent':UserAgent().random,
    'Cookie':'domain=bj; _Jo0OQK=446C9E6A7A38680243BE4C0D7A6A41759C4BBE864AE861B19955A74FD806905AE3FB2787D3FDB4D2FD17CEFFBF44325B434C773F941840C48EC6F454D9CBB01EC06DE8682CA7D10E3B498FB9E3C853EFEE298FB9E3C853EFEE215D8BEE34E43E5C0GJ1Z1RQ==; yfx_c_g_u_id_10000001=_ck19082020472913353825440357516; yfx_f_l_v_t_10000001=f_t_1566305249268__r_t_1566305249268__v_t_1566305249268__r_c_0; isClose=yes; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1566305250; _ga=GA1.2.489557223.1566305250; _gid=GA1.2.629827538.1566305250; wiwj_token_ST-382199-dOBm1Q7uFhpQcg6d9hcW-passport.5i5j.com=%7B%22uid%22%3A%226257157%22%7D; yfx_s_u_id_10000001=6257157; yfx_s_u_name_10000001=17611100746; webim_token_6257157=YWMtZWEYusNJEemOaIsW9GcUr0hiN_DRZBHmt4eJit69xiBvJew6SvUR6ZgX0ySpLDT6AwMAAAFsrxYqmABPGgA_PR9wgA9IjamM1Ilgz57csvonar_EkIRtdVBLxZY_Gg; PHPSESSID=ST-382204-I1RcZlcSN1kGlSOJd4TR-passport5i5jcom; user_info=TBYRRFZKXlNdAUFbEANWAQIAVAMABwEOQ08VXF1RDgtRXVUSChIBBwYBAQEAAAcEBhIcEkVDVUJ5VBIKEgYCBQcBBQcSTQ; wiwj_token_ticket=ST-382204-I1RcZlcSN1kGlSOJd4TR-passport.5i5j.com; wiwj_token_ST-382204-I1RcZlcSN1kGlSOJd4TR-passport.5i5j.com=%7B%22uid%22%3A%226257157%22%7D; smidV2=201908202101422a5472b3d7d565c2db5bfeffc3d24d7000b359108b5165720; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1566306167',
}
url = 'https://bj.5i5j.com/user/index/'
session = requests.session()
response = session.get(url,headers=headers)
print(response.text)